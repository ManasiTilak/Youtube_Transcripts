import os
from youtube_transcript_api import YouTubeTranscriptApi

## getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e

def save_transcript_to_file(transcript, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(transcript)
        print(f"Transcript saved to {filename}")
    except Exception as e:
        raise e

# Example usage
if __name__ == "__main__":
    youtube_video_url = "youtube.com/watch?v=lEDH-vq5l6M"
    transcript = extract_transcript_details(youtube_video_url)
    save_transcript_to_file(transcript, "transcript.txt")
