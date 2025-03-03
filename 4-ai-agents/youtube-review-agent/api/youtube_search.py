import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
from api.video_ranking import rank_videos  # 📌 Video sıralama modülünü ekledik!

# API anahtarını yükle
load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

if not YOUTUBE_API_KEY:
    raise ValueError("❌ YouTube API Key bulunamadı! Lütfen .env dosyanı kontrol et.")

# YouTube API istemcisini başlat
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

def search_youtube_videos(product_name, max_results=10, language="tr", region="TR"):
    """
    Belirtilen ürün adıyla YouTube'da arama yapar ve en iyi sonuçları döndürür.
    """
    query = f"{product_name} review OR comparison OR unboxing"

    try:
        request = youtube.search().list(
            part="snippet",
            q=query,
            maxResults=max_results,
            order="relevance",  # En alakalı videoları getir
            type="video",
            relevanceLanguage=language,  # 📌 İçeriğin dilini belirle
            regionCode=region  # 📌 İçeriğin ülkesini belirle

        )
        response = request.execute()

        if "items" not in response:
            raise ValueError("❌ YouTube API'den beklenen veri alınamadı!")

        videos = []
        for item in response.get("items", []):
            video_id = item.get("id", {}).get("videoId")  # Eğer 'videoId' yoksa hata oluşmasını engelle
            title = item["snippet"]["title"]
            channel = item["snippet"]["channelTitle"]

            if not video_id:
                continue  # Video ID olmayanları geç

            videos.append({
                "id": video_id,
                "title": title,
                "channel": channel
            })

        if not videos:
            print("❌ Hiç video bulunamadı. Sorguyu kontrol edin.")
        
        return videos

    except Exception as e:
        print(f"❌ YouTube API Hatası: {e}")
        return []

# Test edelim
if __name__ == "__main__":
    product = "Is the iPhone 13 Pro good for work"
    videos = search_youtube_videos(product)

    if videos:
        print("\n📌 **YouTube Arama Sonuçları (Ham Veri):**")
        for vid in videos:
            print(f"{vid['title']} - {vid['channel']} - ID: {vid['id']}")

        # 📌 Videoları sıralayalım!
        ranked_videos = rank_videos(videos)

        print("\n📌 **Etkileşime Göre Sıralı Videolar:**")
        for vid in ranked_videos:
            print(f"{vid['title']} - {vid['views']} Views - {vid['likes']} Likes - {vid['comments']} Comments")
    else:
        print("❌ Hiçbir video bulunamadı!")
