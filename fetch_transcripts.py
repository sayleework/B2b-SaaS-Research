import os
import re
import requests

API_KEY = "sd_20f599a2e6115093f3f0ce712814c741"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "research", "youtube-transcripts")

VIDEOS = [
    "https://www.youtube.com/watch?v=PmKPtCUZlCE",
    "https://www.youtube.com/watch?v=9JfTwbCwKco",
    "http://youtube.com/watch?v=UWHcOQCw4NU",
    "https://www.youtube.com/watch?v=9wuHUDm4-WE",
    "https://www.youtube.com/watch?v=LOLzw_ZkoIc",
    "https://www.youtube.com/watch?v=mbCfRlY7elM",
]


def slugify(text, max_words=5):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    words = text.split()[:max_words]
    return "-".join(words)


def name_to_slug(channel):
    parts = channel.strip().split()
    if len(parts) >= 2:
        return f"{parts[0].lower()}-{parts[1].lower()}"
    return slugify(channel, max_words=2)


def fetch_transcript(video_url):
    resp = requests.get(
        "https://api.supadata.ai/v1/youtube/transcript",
        params={"url": video_url, "text": "true"},
        headers={"x-api-key": API_KEY},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def extract_video_id(video_url):
    match = re.search(r"v=([^&]+)", video_url)
    return match.group(1) if match else None


def fetch_metadata(video_url):
    vid_id = extract_video_id(video_url)
    if not vid_id:
        return {}
    resp = requests.get(
        "https://api.supadata.ai/v1/youtube/video",
        params={"id": vid_id},
        headers={"x-api-key": API_KEY},
        timeout=30,
    )
    if resp.status_code == 200:
        return resp.json()
    return {}


def save_transcript(video_url, data, meta):
    title = meta.get("title") or data.get("title") or "Untitled"
    raw_channel = meta.get("channel") or data.get("channel") or {}
    if isinstance(raw_channel, dict):
        channel = raw_channel.get("name") or "Unknown Channel"
    else:
        channel = str(raw_channel) or "Unknown Channel"

    name_slug = name_to_slug(channel)
    title_slug = slugify(title, max_words=5)
    filename = f"{name_slug}-{title_slug}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    content_lines = data.get("content", [])
    if isinstance(content_lines, list):
        transcript_text = " ".join(
            seg.get("text", "") if isinstance(seg, dict) else str(seg)
            for seg in content_lines
        )
    else:
        transcript_text = str(content_lines)

    md = f"""# {title}

**Channel:** {channel}
**Video URL:** {video_url}
**Date Retrieved:** April 2026

---

## Transcript

{transcript_text}
"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"  Saved: {filename}")
    return filename


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for url in VIDEOS:
        print(f"\nProcessing: {url}")
        try:
            meta = fetch_metadata(url)
            data = fetch_transcript(url)
            save_transcript(url, data, meta)
        except requests.HTTPError as e:
            print(f"  HTTP error {e.response.status_code}: {e.response.text[:200]}")
        except Exception as e:
            print(f"  Error: {e}")
    print("\nDone.")


if __name__ == "__main__":
    main()
