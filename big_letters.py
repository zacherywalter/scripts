import json
import pathlib
import sys

def bprintc(character: str, letters_json: dict):
    """Prints a single character in big format vertically."""
    letter = letters_json.get(character)
    if isinstance(letter, list):
        for row in letter[:4]:
            print(row)
    else:
        print("not a string")

def bprints_vertical(string: str, letters_json: dict):
    """Prints a string in big format vertically, character by character."""
    for character in string:
        if character in letters_json:
            rows = letters_json[character]
            for row in rows[:4]:
                print(row)
            print()

def bprints(string: str, letters_json: dict):
    """Prints a string in big format horizontally (row by row)."""
    # Remove trailing newline if present from input
    string_copy = string.rstrip("\r\n")
    
    for j in range(4):
        for character in string_copy:
            letter_found = False
            if character in letters_json:
                letter_found = True
                rows = letters_json[character]
                if j < len(rows):
                    print(rows[j], end="")
            
            if not letter_found and character != '\n':
                print(f"letter {character} not found", end="")
        print()

def main():
    # Determine the directory where this script is located
    script_dir = pathlib.Path(__file__).parent.resolve()
    json_path = script_dir / "big_letters.json"

    # Load the JSON file containing the big letters using the absolute path
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            letters_json = json.load(file)
    except FileNotFoundError:
        print(f"Error: Could not find 'big_letters.json' at {json_path}")
        return

    # Check if a command-line argument was provided
    if len(sys.argv) > 1:
        words = sys.argv[1]
    else:
        words = "bigletters"

    # print(f"you typed: {words}")
    bprints(words, letters_json)

if __name__ == "__main__":
    main()

