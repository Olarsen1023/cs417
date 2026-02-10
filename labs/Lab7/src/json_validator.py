"""
JSON Structure Validator — Lab 7

Validates the structural nesting of a JSON string using a Stack.
Reports the location (line, column) of any errors found.
"""

from stack import Stack


# Maps each closing character to its expected opening character.
MATCHING = {
    "}": "{",
    "]": "[",
}


def validate(json_string):
    """
    Validate the structural nesting of a JSON string.

    Checks that every { has a matching }, every [ has a matching ],
    and that quoted strings are properly closed.

    Args:
        json_string (str): The JSON text to validate.

    Returns:
        tuple: (is_valid, errors)
            - is_valid (bool): True if the structure is valid.
            - errors (list[str]): List of error message strings.
              Empty if valid.
    """
    stack = stack()
    line = 1, col = 0

    i = 0
    n = len(json_string)

    while i < n:
        ch = json_string[i]
        col += 1
    
    # handling the new lines
        if ch == '\n':
            line += 1
            col = 0
            i += 1
            continue
        if ch == '\r':
            i += 1
            if i >= n or json_string[i] != '\n':
                line += 1
                col = 0
            continue
        
        if ch == '{' or ch == '[':
            stack.push((ch, line, col))
        elif ch == '}' or ch == ']':
            if stack.is_empty():
                #unexpected close bracket thingy
                return (False, f"ERROR Line {line}, Col {col}: Unexpected closer '{ch}'")
            
            open_char, open_line, open_col = stack.pop()
            if open_char == '{' and ch != '}':
                # squig mismatch
                return (False, f"ERROR Line {line}, Col {col}: Expected '}}' but got {ch}'", f"(opening '{{' at Line {open_line}, Col {open_col})")
           
            if open_char == '[' and ch != ']':
                # bracket mismatch
                return (
                    False,
                    f"ERROR Line {line}, Col {col}: Expected ']' but found '{ch}' "
                    f"(opening '[' at Line {open_line}, Col {open_col})"
                )
        # had to add this to keep parsing
        i += 1

    # checks the end of the string
    if not stack.is_empty():
        # find the most recent open to handle that case too
        open_char, open_line, open_col = stack.pop()
        return (False, f"ERROR: Unclosed '{open_char}' at Line {open_line}, Col {open_col}")

    return (True, None)


def validate_file(filepath):
    """
    Validate a JSON file by reading it and calling validate().

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        tuple: (is_valid, errors) — same as validate().
    """
    with open(filepath, "r") as f:
        content = f.read()
    return validate(content)


# ── Main ─────────────────────────────────────────────────────────
# You can use this to test your validator from the command line:
#   python src/json_validator.py tests/test_data/easy_correct.json

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python json_validator.py <filepath>")
        sys.exit(1)

    filepath = sys.argv[1]
    is_valid, errors = validate_file(filepath)

    if is_valid:
        print(f"{filepath}: Valid JSON structure")
    else:
        for error in errors:
            print(error)