import openai
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request,json
from flask_cors import CORS
import youtube_transcript_api
from youtube_transcript_api.formatters import TextFormatter
import googleapiclient.discovery

load_dotenv()
app = Flask(__name__)
CORS(app)
openai.api_key = os.environ.get('CHATGPT_API_KEY')
message_history = []
query = [{"role": "system", "content": "You are a youtube video transcript analysis expert and can answer the questions about a video. Do not add anything to the transcript yourself"}]
api_service_name = "youtube"
api_version = "v3"
yt_api_key = os.environ.get('YOUTUBE_API_KEY')
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = yt_api_key)


def extract_video_id(video_url: str) -> str:
    # Parse the video ID from the URL
    # e.g. https://www.youtube.com/watch?v=dQw4w9WgXcQ -> dQw4w9WgXcQ

    video_id = video_url.split('?v=')[-1]
    return video_id

@app.route('/transcript', methods=['GET'])
def transcript():
    args = request.args
    
    video_url = args.get('videoUrl')
    print(video_url)
    video_id = extract_video_id(video_url)
    
    transcript = youtube_transcript_api.YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = ' '.join([item['text'] for item in transcript])
    
    return {'transcript':transcript_text }




# Endpoint to get metadata about youtube video
@app.route('/metadata', methods=['GET'])
def metadata():
    args = request.args
    video_url = args.get('videoUrl')
    video_id = extract_video_id(video_url)
    # Get Video Metadata from Youtubev3 API
    yt_request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response =  yt_request.execute()
    return{'metadata':response['items'][0]['snippet']}

# Endpoint to generate response using ChatGPT API
@app.route('/question', methods=['POST'])
def generate_response():
    print('question endpoint')
    transcript = request.json.get('transcript')
    print("transcript"+transcript['transcript'][0:100])
    question = request.json.get('question')
    print("question"+question)
    if not message_history :
        message_history.append({"role": "user", "content": "Here is the transcript of a video-"+transcript['transcript'][0:500]})
        message_history.append({"role": "user", "content":question})
    else:
        message_history.append({"role": "user", "content":question})
    # print('message_history after append')
    # print(message_history)
    
    try:
        query.extend(message_history)
        # Generate response using the ChatGPT API
        result = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=query
        )
        print("here is the query")
        print(query)
        gpt_message = result["choices"][0]["message"]
        message_history.append({"role": gpt_message["role"], "content": gpt_message["content"]})
        # print(query)
        return  jsonify({'message':gpt_message["content"]})

    except Exception as e:
        print(e)
        return jsonify({'message': 'Error generating response'}), 500
if __name__ == '__main__':
    app.run(debug=True)
