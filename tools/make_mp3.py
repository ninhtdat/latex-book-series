import os
from pathlib import Path
import edge_tts
import asyncio
import re

# ==============================
# GLOBAL CONFIG
# ==============================
OUTPUT_DIR = Path("audio")
OUTPUT_DIR.mkdir(exist_ok=True)

# ===== Voices =====
VOICE_EN = "en-US-JennyNeural"
VOICE_JA = "ja-JP-NanamiNeural"

# ==============================
# Load words.txt
# ==============================
try:
    with open("words.txt", "r", encoding="utf-8") as f:
        words = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file words.txt.")
    exit(1)

# ==============================
# Concurrency control
# ==============================
CONCURRENCY_LIMIT = 20
semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)

# ==============================
# Language detection (EN / JA)
# ==============================
JP_PATTERN = re.compile(r"[\u3040-\u30FF\u4E00-\u9FFF]")

def detect_language(text: str) -> str:
    """Return 'ja' or 'en'"""
    return "ja" if JP_PATTERN.search(text) else "en"

def get_voice(text: str) -> str:
    return VOICE_JA if detect_language(text) == "ja" else VOICE_EN

# ==============================
# Audio generation
# ==============================
async def create_audio(text: str):
    async with semaphore:
        voice = get_voice(text)

        # Tên file KHÔNG có _en / _ja
        safe_name = text.replace(" ", "_")
        filename = OUTPUT_DIR / f"{safe_name}.mp3"

        if filename.exists():
            return

        communicate = edge_tts.Communicate(text, voice)

        try:
            await communicate.save(str(filename))
            print(f"Đã tạo: {filename}")
        except Exception as e:
            print(f"Lỗi khi tạo '{text}': {e}")
            if "[Errno 24]" in str(e):
                await asyncio.sleep(1)

# ==============================
# Main async
# ==============================
async def main_async():
    tasks = [asyncio.create_task(create_audio(word)) for word in words]
    if tasks:
        await asyncio.gather(*tasks)

    print("Hoàn tất tạo audio (tự nhận diện EN / JA).")

# ==============================
# Entry point
# ==============================
if __name__ == "__main__":
    asyncio.run(main_async())
