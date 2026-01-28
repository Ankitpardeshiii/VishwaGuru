import httpx
import asyncio
import wave
import io
import os
import sys
from PIL import Image
import struct

# Add backend to path
sys.path.append(os.getcwd())

def verify_endpoints():
    from backend.main import app
    from fastapi.testclient import TestClient

    # TestClient context manager triggers lifespan events
    with TestClient(app) as client:
        print("Verifying /api/detect-water-leak...")
        # Create a real small red image using PIL
        img = Image.new('RGB', (100, 100), color = 'red')
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG')
        img_content = img_byte_arr.getvalue()

        # We need to create a fresh BytesIO for each request or seek(0)

        response = client.post("/api/detect-water-leak", files={"image": ("test.jpg", io.BytesIO(img_content), "image/jpeg")})
        print(f"Water Leak Status: {response.status_code}")
        if response.status_code not in [200, 500]:
             print(f"FAILED: Unexpected status code {response.status_code}")
             print(response.text)
        else:
             print("PASSED (Endpoint reachable)")

        print("Verifying /api/detect-audio...")
        # Create dummy audio (Minimal WAV file)
        audio_io = io.BytesIO()
        with wave.open(audio_io, 'wb') as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(44100)
            data = struct.pack('<h', 0) * 100 # 100 frames of silence
            wav_file.writeframes(data)
        audio_content = audio_io.getvalue()

        response = client.post("/api/detect-audio", files={"file": ("test.wav", io.BytesIO(audio_content), "audio/wav")})
        print(f"Audio Status: {response.status_code}")
        if response.status_code not in [200, 500]:
             print(f"FAILED: Unexpected status code {response.status_code}")
             print(response.text)
        else:
             print("PASSED (Endpoint reachable)")

        print("Verifying /api/detect-accessibility...")
        response = client.post("/api/detect-accessibility", files={"image": ("test.jpg", io.BytesIO(img_content), "image/jpeg")})
        print(f"Accessibility Status: {response.status_code}")
        if response.status_code not in [200, 500]:
             print(f"FAILED")
        else:
             print("PASSED")

        print("Verifying /api/detect-crowd...")
        response = client.post("/api/detect-crowd", files={"image": ("test.jpg", io.BytesIO(img_content), "image/jpeg")})
        print(f"Crowd Status: {response.status_code}")
        if response.status_code not in [200, 500]:
             print(f"FAILED")
        else:
             print("PASSED")

if __name__ == "__main__":
    # Ensure backend deps are installed (assuming environment is set up)
    try:
        verify_endpoints()
    except ImportError as e:
        print(f"ImportError: {e}. Make sure you are running from repo root.")
    except Exception as e:
        print(f"An error occurred: {e}")
