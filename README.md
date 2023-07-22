# Python Server for [TubeGPT Frontend](https://github.com/kashyap-datta/tubegpt)

This project showcases a web application for analyzing YouTube video transcripts using GPT-3, OpenAI's language model, and an unofficial YouTube Transcript API.

## Overview

The TubeGPT project leverages OpenAI's GPT API, to provide an interactive chat interface for users to question and gain insights about a YouTube video's content. The application also uses an unofficial YouTube Transcript API to fetch the transcript of the video.

## Note

This repository is a personal project aimed at exploring the integration of language models for real-world applications. It is designed to demonstrate the potential of ChatGPT and the YouTube Transcript API in generating video summaries and responding to user questions.

Please note that this project is a work-in-progress and may require further development and refinement. It is not intended to be a fully production-ready application but rather a learning experiment and showcase of technical skills in the field of natural language processing and AI.

Your feedback is highly appreciated, and I welcome any suggestions or improvements you may have regarding the project.

## Requirements

- Python 3.x
- Flask
- googleapiclient
- youtube_transcript_api
- openai

## Usage

1. Clone the repository and navigate to the project directory.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up environment variables for the ChatGPT API key (`CHATGPT_API_KEY`) and YouTube API key (`YOUTUBE_API_KEY`) using a `.env` file.
4. Run the Flask application with `python app.py`.
5. Access the application through your web browser or API client.

## Endpoints

The application exposes the following endpoints:

- `GET /transcript`: Fetches the transcript of a YouTube video based on the provided video URL.
- `GET /metadata`: Retrieves metadata (e.g., title, description) of a YouTube video based on the provided video URL.
- `POST /question`: Generates responses to user questions about the video using ChatGPT.

## Acknowledgments

Special thanks to OpenAI and the creators of the YouTube Transcript API for providing the tools and APIs that power this project.


