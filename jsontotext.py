import json

def seconds_to_hhmmss(seconds):
    # Convert seconds to hours, minutes, and seconds.
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{secs:02}"

def format_transcript(json_data):
    # Parse the JSON data
    data = json.loads(json_data)
    transcript_lines = []

    # Loop over each segment and format it
    for segment in data.get("segments", []):
        start_time = seconds_to_hhmmss(segment["start"])
        speaker = segment["speaker"]
        text = segment["text"].strip()  # Remove any leading/trailing whitespace
        
        # Format: [HH:MM:SS] SPEAKER: Spoken text.
        formatted_line = f"[{start_time}] {speaker}: {text}"
        transcript_lines.append(formatted_line)
    
    # Join all segments with a blank line for readability
    return "\n\n".join(transcript_lines)

# Example JSON input
json_input = '''{
  "detected_language": "en",
  "segments": [
    {
      "end": 30.811,
      "speaker": "SPEAKER_00",
      "start": 2.585,
      "text": " The little tales they tell are false. The door was barred, locked and bolted as well. Ripe pears are fit for a queen's table. A big wet stain was on the round carpet. The kite dipped and swayed but stayed aloft. The pleasant hours fly by much too soon. The room was crowded with a mild wob."
    },
    {
      "end": 48.592,
      "speaker": "SPEAKER_00",
      "start": 33.029,
      "text": " The room was crowded with a wild mob. This strong arm shall shield your honour. She blushed when he gave her a white orchid. The beetle droned in the hot June sun."
    }
  ]
}'''

# Format the transcript and print the result
formatted_transcript = format_transcript(json_input)
print(formatted_transcript)
