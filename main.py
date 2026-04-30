import sys
from notes.manager import add_note, list_notes, delete_note

def print_usage():
    print("Usage:")
    print("  python main.py add \"Note text\"")
    print("  python main.py list")
    print("  python main.py delete <note_id>")

def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) == 3:
        add_note(sys.argv[2])
    elif command == "list":
        list_notes()
    elif command == "delete" and len(sys.argv) == 3:
        delete_note(int(sys.argv[2]))
    else:
        print_usage()

if __name__ == "__main__":
    main()