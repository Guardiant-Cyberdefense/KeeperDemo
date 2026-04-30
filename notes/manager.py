from .storage import load_notes, save_notes

def add_note(text: str):
    notes = load_notes()
    notes.append(text)
    save_notes(notes)
    print(f"✅ Note added: {text}")

def list_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return

    for idx, note in enumerate(notes, start=1):
        print(f"{idx}. {note}")

def delete_note(note_id: int):
    notes = load_notes()
    if note_id < 1 or note_id > len(notes):
        print("❌ Invalid note ID")
        return

    removed = notes.pop(note_id - 1)
    save_notes(notes)
    print(f"🗑️ Removed note: {removed}")