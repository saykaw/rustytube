from youtube_transcript_api import YouTubeTranscriptApi

def format_transcript(transcript):
    formatted_transcript = ""
    
    for entry in transcript:
        duration = entry["duration"]
        start = entry["start"]
        text = entry["text"]

        formatted_transcript += f"Duration: {duration:.3f}s, Start: {start:.3f}s\n"
        formatted_transcript += f"Text: {text}\n"
        formatted_transcript += "=" * 30 + "\n"  # Separator for better readability

    return formatted_transcript

def get_video_transcription(video_id):
    try:
        transcript_list= YouTubeTranscriptApi.get_transcript(video_id)

        #for entry in transcript:
          #  print(f"{entry['start']} - {entry['start'] + entry['duration']}: {entry['text']}")
        transcriptformat = ' '.join([d['text'] for d in transcript_list])
    

    except Exception as e:
        print(f"Error: {e}")
    return transcriptformat
# Example usage


