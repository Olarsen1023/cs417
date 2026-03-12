"""Word counter using argparse."""
import argparse
from collections import Counter


def build_parser():
    """Create and return the argument parser.

    Arguments to define:
        filename    - positional, the text file to analyze
        --ignore-case / -i  - store_true, lowercase all words
        --top / -t          - int, show top N most frequent words (default: None)
        --min-length / -m   - int, only count words with at least this many chars (default: 1)
        --sort-by / -s      - choices ["freq", "alpha"], how to sort top words (default: "freq")
        --reverse / -r      - store_true, reverse the sort order

    Returns:
        argparse.ArgumentParser
    """
    # TODO: Create an ArgumentParser with a description
    parser = argparse.ArgumentParser(description="Count words in a text file.")
    # TODO: Add the positional 'filename' argument
    parser.add_argument("filename", help="The text file to analyze")
    # TODO: Add --ignore-case / -i (action="store_true")
    parser.add_argument("--ignore-case", "-i", action="store_true", help="Lowercase all words")
    # TODO: Add --top / -t (type=int, default=None)
    parser.add_argument("--top", "-t", type=int, default=None, help="Show top N most frequent words")
    # TODO: Add --min-length / -m (type=int, default=1)
    parser.add_argument("--min-length", "-m", type=int, default=1, help="Only count words with at least this many characters")
    # TODO: Add --sort-by / -s (choices=["freq", "alpha"], default="freq")
    parser.add_argument("--sort-by", "-s", choices=["freq", "alpha"], default="freq", help="How to sort top words")
    # TODO: Add --reverse / -r (action="store_true")
    parser.add_argument("--reverse", "-r", action="store_true", help="Reverse the sort order")
    return parser


def analyze(filepath, ignore_case=False, top=None, min_length=1,
            sort_by="freq", reverse=False):
    """Analyze a text file and return a formatted result string.

    Args:
        filepath: path to the text file
        ignore_case: if True, lowercase all words before counting
        top: if set, show the N most frequent words with counts
        min_length: only count words with at least this many characters
        sort_by: "freq" (by count) or "alpha" (alphabetical) when showing top words
        reverse: if True, reverse the sort order

    Returns:
        str: formatted result

    Raises:
        FileNotFoundError: if the file doesn't exist
    """
    # TODO: Read the file and split into words on whitespace
    with open(filepath, "r") as f:
        text = f.read()
    words = text.split()
    # TODO: If ignore_case, lowercase all words
    if ignore_case:
        words = [w.lower() for w in words]
    # TODO: Filter out words shorter than min_length
    words = [w for w in words if len(w) >= min_length]
    # TODO: Count total words
    total_words = len(words)
    # TODO: If top is None, return "<filename>: <count> words"
    if top is None:
        return f"{filepath}: {total_words} words"
    word_counts = Counter(words)
    if sort_by == "alpha":
        sorted_words = sorted(word_counts.items(), key=lambda x: x[0], reverse=reverse)
    else:
        sorted_words = word_counts.most_common()
    if reverse:
        sorted_words = list(reversed(sorted_words))
    top_words = sorted_words[:top]
    result_lines = [f"{filepath}: {total_words} words", "", "Top 5 words:"]
    for word, count in top_words:
        result_lines.append(f"  {word}: {count}")
    return "\n".join(result_lines)



def main():
    """Build parser, parse args, analyze, print result."""
    # TODO: Build the parser
    # TODO: Parse args
    # TODO: Call analyze with the parsed arguments
    # TODO: Print the result
    parser = build_parser()
    args = parser.parse_args()
    result = analyze(args.filename, ignore_case=args.ignore_case, top=args.top,
                        min_length=args.min_length, sort_by=args.sort_by, reverse=args.reverse)
    print(result)



if __name__ == "__main__":
    main()
