from openai import OpenAI
import uuid
import os

client = OpenAI()

def generate_voice(text: str) -> str:
    """
    Generates an MP3 voice file from text using OpenAI TTS.

    Returns:
        filepath (str): Path to the generated audio file.
    """
    # Ensure audio directory exists
    os.makedirs("audio", exist_ok=True)

    filename = f"audio_{uuid.uuid4()}.mp3"
    filepath = f"audio/{filename}"

    try:
        with client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=text
        ) as response:
            response.stream_to_file(filepath)
    except Exception as e:
        print(f"Voice generation failed: {e}")
        return None

    return filepath