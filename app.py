from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import langchain_helper as lch
from verdictfile import verdict
from tscript import get_video_transcription
from summ import generate_summary
from keyworder import getvidkeys


app = Flask(__name__)

@app.get('/summary')
def summary_api():
    url = request.args.get('url', '')
    video_id = url.split('=')[1]
    summary = generate_summary(get_transcript(video_id))
    return summary, 200

def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript

def generate_summary(transcript):
    summary = summarize(transcript,ratio=0.2)
    return summary
    summariser = pipeline('summarization')
    summary = ''
    for i in range(0, (len(transcript)//1000)+1):
        summary_text = summariser(transcript[i*1000:(i+1)*1000])[0]['summary_text']
        summary = summary + summary_text + ' '
    return summary

# def get_summary(transcript):
#     summariser = pipeline('summarization')
#     summary = ''
#     for i in range(0, (len(transcript)//1000)+1):
#         summary_text = summariser(transcript[i*1000:(i+1)*1000])[0]['summary_text']
#         summary = summary + summary_text + ' '
    
#     return summary
    
@app.get('/response')
def chatapp():
    url =request.args.get('videourl', '')
    query=request.args.get('query','')
    db = lch.create_db_from_youtube_video_url(url)
    response, docs = lch.get_response_from_query(db, query)

    return response
@app.get('/transcription')
def transcribe():
    
    url =request.args.get('videourl', '')
    video_id = url.split('=')[1]
    transcript=get_video_transcription(video_id)
    return transcript

@app.get('/verdict')
def getVerdict():
      url =request.args.get('videourl', '')
      result=verdict(url)
      return result

@app.get('/keywords')
def getvideokeyword():
    url =request.args.get('videourl', '')
    video_id = url.split('=')[1]
    keyword=getvidkeys(video_id)
    return keyword



if __name__ == '__main__':
    app.run()