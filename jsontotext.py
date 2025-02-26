import json
import sys

def seconds_to_hhmmss(seconds):
    """Convert seconds to HH:MM:SS format."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{secs:02}"

def format_transcript(json_data):
    """Format a transcript from JSON data."""
    data = json.loads(json_data)
    transcript_lines = []

    for segment in data.get("segments", []):
        start_time = seconds_to_hhmmss(segment["start"])
        speaker = segment["speaker"]
        text = segment["text"].strip()

        formatted_line = f"[{start_time}] {speaker}: {text}"
        transcript_lines.append(formatted_line)
    
    return "\n\n".join(transcript_lines)

if __name__ == "__main__":
    # Read JSON input from stdin
    json_input = sys.stdin.read()
    
    # Format and print the transcript
    formatted_transcript = format_transcript(json_input)
    print(formatted_transcript)
