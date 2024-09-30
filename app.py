import os
import sys 
from src.audio_processing import transcribe_audio

def main():
    
    # Determine the base directory based on whether we're in a 
    # bundled executable or a script
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
    
    audio_file = input("Please enter the path to the audio file (e.g., assets/audio/jackhammer.wav):")
    
    audio_file_path = os.path.join(base_dir, audio_file)
    
    if getattr(sys, 'frozen', False):
        audio_file_path = os.path.join(base_dir, 'assets', 'audio', os.path.basename(audio_file))
    
    print(f"Resolved audio file path: {audio_file_path}")
    
    if audio_file_path:
        try:
            
            if not os.path.exists(audio_file_path):
                raise FileNotFoundError(f"The file at {audio_file_path} does not exists.")
            
            transcription = transcribe_audio(audio_file_path)
            print("Transcription: ", transcription)
        except FileNotFoundError:
            print("The specified file was not found. Please check the file path and try again.")
        except Exception as e:
            print(f"An error occureed: {e}")
    else:
        print("No file path provided. Exiting the program.")                
        
    
if __name__ == "__main__":
    main()    
               