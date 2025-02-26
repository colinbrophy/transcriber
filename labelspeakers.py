import re
import sys

# Regular expression to match timestamps and speaker labels
pattern = re.compile(r"(\[\d{2}:\d{2}:\d{2}\]) (SPEAKER_\d{2}): (.*)")

speaker_map = {}
structured_transcript = []

# Ensure a filename argument is provided
if len(sys.argv) < 2:
    print("Error: No input file provided. Usage: python script.py <transcript_file>")
    sys.exit(1)

filename = sys.argv[1]

# Read from the specified file
with open(filename, "r") as file:
    transcript = file.readlines()

for line in transcript:
    match = pattern.match(line)
    if match:
        timestamp, speaker, text = match.groups()
        if speaker not in speaker_map:
            hint = text[:50] + "..." if len(text) > 50 else text
            speaker_name = input(f"Enter name for {speaker} (sample text: '{hint}'): ")
            speaker_map[speaker] = speaker_name.strip() or speaker
        structured_transcript.append(f"{timestamp} {speaker_map[speaker]}: {text}")
    elif line.strip():
        structured_transcript.append(f"{text}")  # Continue dialogue without a new speaker label

# Print the structured transcript to stdout
print("\n".join(structured_transcript))
