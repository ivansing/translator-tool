# Translator Tool

## Introduction

The Audio Translator is a Python-based application that converts audio files into a specified format and transcribes the spoken content using OpenAI's API. This tool is particularly useful for users who need to process audio recordings for various applications such as transcription services, educational purposes, or personal projects.

### Features
- Convert audio files to different formats.
- Transcribe audio content using OpenAI's speech recognition capabilities.
- Supports WAV format.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.8 or later
- Required Python packages (listed isn `requirements.txt`)
- An OpenAI API key (touse the transcription feature)

## Installation

1. Clone the repository
2. cd to folder
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your OpenAI API key. You can do this by creating a .env file in the root directory with the following content:  
```bash
OPENAI_API_KEY=your_api_key_here
```

## Running the Application
To run the application, execute the following command in your terminal:
```bash
python3 app.py
```

When prompted, enter the path to the audio file you wish to convert and transcribe (e.g., `assets/audio/jackhammer.wav`).

## Example Usage
```plaintext
Please enter the path to the audio file (e.g., assets/audio/jackhammer.wav): assets/audio/jackhammer.wav
```

## Building the Application
If you wish to create an executable version of the application using PyInstaller, run the following command:
```bash
pyinstaller --onefile --add-binary "/usr/lib/x86_64-linux-gnu/libpython3.8.so:lib" --add-data ".env:.env" --add-data "assets:assets" app.py
```

## Contributing

Feel free to submit issues, feature requests, or pull requests. Contributions are welcome!


## License

This project is licensed under the MIT License.