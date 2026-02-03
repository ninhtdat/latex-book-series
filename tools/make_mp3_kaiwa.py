import asyncio
from pathlib import Path

import edge_tts
import openpyxl

# ==============================
# CONFIG
# ==============================
INPUT_FILE = "data.xlsx"
OUTPUT_DIR = Path("audio")
OUTPUT_DIR.mkdir(exist_ok=True)

VOICE_EN = "en-US-JennyNeural"
VOICE_JP = "ja-JP-NanamiNeural"

CONCURRENCY_LIMIT = 3
semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)

# ==============================
# TTS
# ==============================
async def create_audio(text: str, voice: str, out_path: Path):
    if not text:
        return

    async with semaphore:
        communicate = edge_tts.Communicate(
            text=text,
            voice=voice,
        )
        await communicate.save(str(out_path))
        print(f"Đã tạo: {out_path}")

# ==============================
# Main
# ==============================
async def main_async():
    wb = openpyxl.load_workbook(INPUT_FILE)
    ws = wb.active

    tasks = []

    for row in ws.iter_rows(min_row=1, values_only=True):
        if not row or len(row) < 3:
            continue

        row_id, dialogue_en, dialogue_jp = row
        if not row_id:
            continue

        rid = int(row_id)

        if dialogue_en:
            tasks.append(
                create_audio(
                    dialogue_en,
                    VOICE_EN,
                    OUTPUT_DIR / f"en_{rid}.mp3"
                )
            )

        if dialogue_jp:
            tasks.append(
                create_audio(
                    dialogue_jp,
                    VOICE_JP,
                    OUTPUT_DIR / f"jp_{rid}.mp3"
                )
            )

    if tasks:
        await asyncio.gather(*tasks)

    print("Hoàn tất tạo audio.")

# ==============================
# Entry
# ==============================
if __name__ == "__main__":
    asyncio.run(main_async())

