from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from autocorrect import Speller
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import re

API = 'AIzaSyCrmfpUElWOUZeHjvDmS_WQlbup-5BuCYA'
youtube = build('youtube', 'v3',developerKey= API)
pattern = (
    r'(https?://)?(www\.)?'
    '(youtube|youtu|youtube-nocookie)\.(com|be)/'
    '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

stop_words = set(stopwords.words('english'))
spell = Speller()
analyzer = SentimentIntensityAnalyzer()
def fetch_comments(url):
    match = re.search(pattern, url)
    s = match.group(6)
    request = youtube.commentThreads().list(
        part="snippet",
        videoId= s,
        maxResults=50,
        order='relevance'
    )
    try:
        response = request.execute()
    except HttpError as e:
        print('Error response status code : {0}, reason : {1}'.format(e.status_code, e.error_details))

    comments = []
    for text in response['items']:
        comments.append(text['snippet']['topLevelComment']['snippet']['textDisplay'])
    return(comments)
def cleaning(text):
    text = text.lower()
    text = word_tokenize(text)
    clean_text = [word for word in text if word not in stop_words]
    clean_text = [word for word in clean_text if word not in string.punctuation]
    clean_text = [spell(word) for word in clean_text]
    cleaned_text = ' '.join(clean_text)
    return(cleaned_text)

def verdict(url):
    url1=url
    for comment in fetch_comments(url1):
        eval = cleaning(comment)
        pos = neg = 0
        scores = analyzer.polarity_scores(eval)
        if scores['compound'] >= 0.05:
            pos += 1
        elif scores['compound'] <= -0.05:
            neg += 1

    if pos > neg:

        return "Good video"
    else:
        
        return "Bad video"



