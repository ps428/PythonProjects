from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from io import BytesIO
from gtts import gTTS
from fastapi.responses import StreamingResponse

app = FastAPI()

class VoiceRequest(BaseModel):
    voices: List[str]
    text: str

@app.post("/generate-voice/")
async def generate_voice(request: VoiceRequest):
    # Ensure that the voices list is not empty
    if not request.voices:
        raise HTTPException(status_code=400, detail="Voices list cannot be empty.")
    
    # Handle the text-to-speech conversion (just using the first voice for simplicity)
    try:
        language="en"
        tts = gTTS(text=request.text, lang=language, slow=False)
        
        # Saving to an in-memory byte stream
        mp3_stream = BytesIO()
        tts.save(mp3_stream)
        mp3_stream.seek(0)
        
        # Return the mp3 file as a response
        return StreamingResponse(mp3_stream, media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating voice: {str(e)}")

# To run the FastAPI app:
# uvicorn app_name:app --reload
