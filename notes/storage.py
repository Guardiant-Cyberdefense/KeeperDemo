import json
from pathlib import Path

DATA_FILE = Path("notes.json")

def load_notes():
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)

def save_notes(notes):
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2)