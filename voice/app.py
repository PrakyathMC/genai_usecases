"""
FastAPI Voice Assistant API
Endpoints to interact with the voice assistant via HTTP requests
"""

# ===== IMPORTS =====

from fastapi import FastAPI, UploadFile, File, HTTPException
# FileResponse - to send audio files back to the client
from fastapi.responses import FileResponse
from pydantic import BaseModel

# tempfile - to create temporary files for audio processing
import tempfile
import os

# Import our existing voice assistant functions
from voice_assistant import (
    initialize_rag,      # Sets up the RAG pipeline
    get_response,        # Gets answer from RAG
    text_to_speech,      # Converts text to audio
    transcribe_file      # Converts audio to text
)


# ===== APP SETUP =====
app = FastAPI(
    title="Voice Assistant API",
    description="STT → RAG → TTS Pipeline via REST API"
)

# Initialize RAG when the app starts (not on every request)
# This runs once when the server boots up
@app.on_event("startup")
def startup_event():
    """Initialize RAG pipeline on server startup"""
    print("Starting up... Initializing RAG pipeline...")
    initialize_rag()
    print("Ready to accept requests!")


# ===== REQUEST/RESPONSE MODELS =====

# Define what a text request looks like
class TextRequest(BaseModel):
    question: str  # The user's question as text

class TextResponse(BaseModel):
    question: str   # Echo back the original question
    answer: str     # The RAG-generated answer


# ===== ENDPOINTS =====
# GET request to /health
@app.get("/health")
def health_check():
    """Check if API is running"""
    return {"status": "ok", "message": "Voice Assistant API is running"}


# ----- Text-to-Text (Simplest) -----
# Send text question, get text answer
# POST request to /ask/text
@app.post("/ask/text", response_model=TextResponse)
def ask_text(request: TextRequest):
    """
    Text-only endpoint (no audio)

    - Send: {"question": "What are store hours?"}
    - Receive: {"question": "...", "answer": "..."}
    """
    # Get response from RAG pipeline
    answer = get_response(request.question)

    # Return both question and answer
    return TextResponse(question=request.question, answer=answer)


# ----- Text-to-Audio -----
# Send text question, get audio response back
# POST request to /ask/text-to-audio
@app.post("/ask/text-to-audio")
def ask_text_get_audio(request: TextRequest):
    """
    Send text, receive audio response

    - Send: {"question": "What are store hours?"}
    - Receive: MP3 audio file
    """
    answer = get_response(request.question)

    # Step 2: Convert response to speech (saves to audio_responses/ folder)
    audio_path = text_to_speech(answer)


    return FileResponse(
        audio_path,
        media_type="audio/mpeg",
        filename="response.mp3"
    )


# ----- Audio-to-Text -----
# Send audio file, get text response back
# POST request to /ask/audio-to-text
@app.post("/ask/audio-to-text", response_model=TextResponse)
async def ask_audio_get_text(audio: UploadFile = File(...)):
    """
    Send audio question, receive text response

    - Send: Audio file (wav, mp3, flac)
    - Receive: {"question": "transcribed text", "answer": "..."}
    """
    # Step 1: Save uploaded audio to a temporary file
    # We need a file on disk for speech_recognition to process
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        content = await audio.read()
        # Write it to the temp file
        tmp.write(content)
        tmp_path = tmp.name

    try:
        # Step 2: Transcribe audio to text (STT)
        question = transcribe_file(tmp_path)

        # Check if transcription failed
        if question.startswith("["):
            raise HTTPException(status_code=400, detail=question)

        answer = get_response(question)
        return TextResponse(question=question, answer=answer)

    finally:
        # Clean up: delete the temporary file
        os.unlink(tmp_path)


# ----- Full Pipeline: Audio-to-Audio -----
# Send audio file, get audio response back (complete voice assistant)
# POST request to /ask/audio
@app.post("/ask/audio")
async def ask_audio_get_audio(audio: UploadFile = File(...)):
    """
    Full voice pipeline: Audio in → Audio out

    - Send: Audio file with your question
    - Receive: MP3 audio file with the answer
    """
    # Step 1: Save uploaded audio to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        content = await audio.read()
        tmp.write(content)
        tmp_path = tmp.name

    try:
        # Step 2: STT - Convert audio to text
        question = transcribe_file(tmp_path)

        if question.startswith("["):
            raise HTTPException(status_code=400, detail="Could not understand audio")

        answer = get_response(question)
        audio_path = text_to_speech(answer)

        return FileResponse(
            audio_path,
            media_type="audio/mpeg",
            filename="response.mp3",
            # Include transcription in response headers (optional metadata)
            headers={
                "X-Transcription": question[:100],  
                "X-Answer": answer[:100]            
            }
        )

    finally:
        # Clean up temp file
        os.unlink(tmp_path)


# ===== RUN SERVER =====

# This runs when you execute: python app.py , uvicorn app:app --reload
if __name__ == "__main__":
    import uvicorn

    # Run the app on localhost:8000
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
