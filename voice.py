import io
import os
import wave

from google.cloud import speech_v1p1beta1 as speech
import pyaudio

# Set up Google Cloud Speech-to-Text client
client = speech.SpeechClient()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "friday.json"

# Set up recording parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

# Start recording audio
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

# Set up initial recognition config
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=RATE,
    language_code="en-US",
)

# Continuously transcribe audio input from microphone
while True:
    frames = []
    # Read audio data from the stream in chunks
    for i in range(0, int(RATE / CHUNK * 5)):  # 5s
        data = stream.read(CHUNK)
        frames.append(data)

    # Create a RecognizeRequest with the audio data
    audio_data = b"".join(frames)
    audio_content = io.BytesIO(audio_data)
    audio = speech.RecognitionAudio(content=audio_data)

    # Update the recognition config with the latest context
    response = client.recognize(config=config, audio=audio)
    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript

    # Print the transcript
    print(transcript)
