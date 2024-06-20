from youtube_transcript_api import YouTubeTranscriptApi
from keybert import KeyBERT

def getvidkeys(video_id):
    transcript = ""
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    for entry in transcript_list:
        transcript += entry['text'] + ' '

    model = KeyBERT('distilbert-base-nli-mean-tokens')
    keywords = model.extract_keywords(transcript)
            
    topkeywords = [keyword for keyword, _ in keywords[:3]]
  
    return ', '.join(topkeywords)  # Join keywords into a string separated by commas


