import sys
import re

def merge_transcript_lines(transcript):
    lines = transcript.splitlines()
    merged_lines = []
    current_speaker = None
    current_timestamp = None
    current_text = ""

    pattern = re.compile(r"\[(.*?)\] (SPEAKER_\d+): (.*)")

    for line in lines:
        line = line.strip()
        if not line:  # Skip blank lines
            continue
        match = pattern.match(line)
        if match:
            timestamp, speaker, text = match.groups()
            if speaker == current_speaker:
                current_text += " " + text.strip()
            else:
                if current_speaker is not None:
                    merged_lines.append(f"[{current_timestamp}] {current_speaker}: {current_text}")
                current_timestamp = timestamp
                current_speaker = speaker
                current_text = text.strip()
    
    if current_speaker is not None:
        merged_lines.append(f"[{current_timestamp}] {current_speaker}: {current_text}")

    return "\n".join(merged_lines)

if __name__ == "__main__":
    transcript = sys.stdin.read()  # Read from standard input
    merged_transcript = merge_transcript_lines(transcript)
    print(merged_transcript)
