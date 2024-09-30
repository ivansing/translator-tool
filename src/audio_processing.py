import openai
from pydub import AudioSegment
from .config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def convert_to_mono_16k(audio_file_path, output_file_path):
    sound = AudioSegment.from_file(audio_file_path)
    sound = sound.set_channels(1)  # Mono
    sound = sound.set_frame_rate(16000)  # 16kHz
    sound.export(output_file_path, format="wav")
    print(f"Converted audio saved to {output_file_path}")

def transcribe_audio(audio_file_path):

    mono_audio_path = "assets/audio/jackhammer_monoj_16k.wav"
    convert_to_mono_16k(audio_file_path, mono_audio_path)

    with open(mono_audio_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

    return transcript['text']