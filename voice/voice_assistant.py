"""
Voice Assistant - STT -> RAG -> TTS Pipeline
"""

import os
from datetime import datetime
import speech_recognition as sr
from gtts import gTTS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_classic.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()


# ============== STEP 1: SPEECH-TO-TEXT ==============

def record_and_transcribe(duration: int = 25) -> str:
    """
    Record audio from microphone and convert to text

    Args:
        duration: Recording duration in seconds

    Returns:
        Transcribed text
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print(f"Recording for {duration} seconds... (speak now)")
        # record() captures exactly N seconds - no early cutoff
        audio = recognizer.record(source, duration=duration)

        print("Processing...")

    try:
        # Using Google's free speech recognition API
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "[Could not understand audio]"
    except sr.RequestError as e:
        return f"[API Error: {e}]"


# This function can be used to transcribe pre-recorded audio files
def transcribe_file(audio_path: str) -> str:
    """
    Transcribe audio from a file

    Args:
        audio_path: Path to audio file (wav, flac, aiff)

    Returns:
        Transcribed text
    """
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "[Could not understand audio]"
    except sr.RequestError as e:
        return f"[API Error: {e}]"


# ============== STEP 2: RAG PIPELINE ==============

# Global variable to store the QA chain (initialize once, reuse)
qa_chain = None


def initialize_rag(knowledge_path: str = "knowledge_base.txt"):
    """
    Initialize RAG pipeline: Load → Split → Embed → Store

    Args:
        knowledge_path: Path to knowledge base text file

    Returns:
        RetrievalQA chain
    """
    global qa_chain

    # 1. Load document
    loader = TextLoader(knowledge_path, encoding="utf-8") 
    # text loader instead of PyPDFLoader for simplicity and to avoid extra dependencies
    documents = loader.load()

    # 2. Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    # 3. Create embeddings and vector store
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(chunks, embeddings)

    # 4. Create retriever
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # 5. Create QA chain
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )

    print("RAG pipeline initialized!")
    return qa_chain


def get_response(query: str) -> str:
    """
    Get response from RAG pipeline

    Args:
        query: User question (from STT)

    Returns:
        Response text (to be sent to TTS)
    """
    global qa_chain

    if qa_chain is None:
        initialize_rag()

    response = qa_chain.invoke(query)
    return response["result"]


# ============== STEP 3: TEXT-TO-SPEECH ==============

# Create folder for audio responses
AUDIO_DIR = "audio_responses"
os.makedirs(AUDIO_DIR, exist_ok=True)


def text_to_speech(text: str) -> str:
    """
    Convert text to speech using Google TTS
    Saves with timestamp to preserve all responses

    Args:
        text: Text to convert to speech

    Returns:
        Path to generated audio file
    """
    # Generate unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(AUDIO_DIR, f"response_{timestamp}.mp3")

    tts = gTTS(text=text, lang='en')
    tts.save(output_path)
    print(f"Audio saved: {output_path}")
    return output_path


def play_audio(audio_path: str):
    """Play audio file (Windows)"""
    os.system(f'start {audio_path}')


# ============== FULL PIPELINE ==============

def voice_assistant():
    """
    Complete pipeline: STT -> RAG -> TTS
    """
    print("\n" + "=" * 40)
    print("Voice Assistant Ready")
    print("=" * 40)

    # Initialize RAG once
    initialize_rag()

    while True:
        # Ask user to speak
        input("\nPress ENTER when ready to speak, then ask your question...")

        # Step 1: STT - Listen and transcribe
        user_text = record_and_transcribe(duration=20)
        print(f"You said: {user_text}")

        if user_text.startswith("["):  # Error message
            print("Couldn't understand. Try again.")
            continue

        # Step 2: RAG - Get response
        print("Thinking...")
        response_text = get_response(user_text)
        print(f"Assistant: {response_text}")

        # Step 3: TTS - Speak response
        print("Speaking...")
        audio_file = text_to_speech(response_text)
        play_audio(audio_file)

        # Ask if user wants to continue
        another = input("\nAsk another question? (y/n): ").strip().lower()
        if another != 'y':
            print("Goodbye!")
            break


# ============== TEST ==============

if __name__ == "__main__":
    voice_assistant()
