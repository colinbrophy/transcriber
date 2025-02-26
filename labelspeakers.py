#!/usr/bin/env python3

import re
import sys

# Regular expression to match timestamps and speaker labels
pattern = re.compile(r"(\[\d{2}:\d{2}:\d{2}\]) (SPEAKER_\d{2}): (.*)")

speaker_map = {}
structured_transcript = []

transcript = sys.stdin.read()

for line in transcript.split("\n"):
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

print("\n".join(structured_transcript))
