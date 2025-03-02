from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

# .env dosyasını yükleyelim
load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# YouTube API istemcisi
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

def get_video_details(video_id):
    """
    Video ID'sine göre izlenme, beğeni ve yorum sayısını alır.
    """
    request = youtube.videos().list(
        part="statistics",
        id=video_id
    )
    response = request.execute()

    if response.get("items"):
        stats = response["items"][0]["statistics"]
        return {
            "views": int(stats.get("viewCount", 0)),
            "likes": int(stats.get("likeCount", 0)),
            "comments": int(stats.get("commentCount", 0))
        }
    return None

def rank_videos(videos):
    """
    Videoları izlenme, beğeni ve yorum sayılarına göre sıralar.
    """
    ranked_videos = []
    for video in videos:
        details = get_video_details(video["id"])
        if details:
            video.update(details)
            ranked_videos.append(video)

    # Sıralama: Öncelik İzlenme > Beğeni > Yorum
    ranked_videos.sort(key=lambda x: (x["views"], x["likes"], x["comments"]), reverse=True)
    
    return ranked_videos
