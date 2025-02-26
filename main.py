#!/usr/bin/env python3
import os
import sys
import replicate

def main():
    # Ensure an argument is passed
    if len(sys.argv) < 2:
        raise ValueError("Please provide the path to the audio file as the first argument.")
    
    audio_file_path = sys.argv[1]
    
    # Ensure the API tokens are set
    replicate_token = os.getenv("REPLICATE_API_TOKEN")
    huggingface_token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")
    
    if not replicate_token:
        raise EnvironmentError("Please set the REPLICATE_API_TOKEN environment variable.")
    
    if not huggingface_token:
        raise EnvironmentError("Please set the HUGGINGFACE_ACCESS_TOKEN environment variable for diarization.")

    # Define the input parameters for the WhisperX model
    inputs = {
        "audio_file": audio_file_path,
        "language": "en",  # Default language to English
        "diarization": True,  # Enable diarization
        "align_output": True,  # Enable alignment
        "huggingface_access_token": huggingface_token  # Pass Hugging Face token for diarization
        # Optional parameters:
        # "debug": True,
        # "vad_onset": 0.5,
        # "batch_size": 64,
        # "vad_offset": 0.363,
        # "temperature": 0.0,
        # "max_speakers": None,
        # "min_speakers": None,
        # "initial_prompt": "",
        # "language_detection_min_prob": 0.0,
        # "language_detection_max_tries": 5,
    }

    # Call the WhisperX model via Replicate
    output = replicate.run(
        "victor-upmeet/whisperx:84d2ad2d6194fe98a17d2b60bef1c7f910c46b2f6fd38996ca457afd9c8abfcb",
        input=inputs
    )

    # Print the transcription output
    print(output)

if __name__ == "__main__":
    main()
