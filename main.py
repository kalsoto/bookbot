import sys
from stats import (
    get_word_count,
    get_char_occurence,
    get_sorted_char_list,
)


def main():
    book_path = get_book_from_args()
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_dict = get_char_occurence(text)
    sorted_chars = get_sorted_char_list(char_dict)
    print_report(book_path, num_words, sorted_chars)


def get_book_from_args():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]


def print_report(book_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


main()
