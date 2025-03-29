from stats import get_char_numb
from stats import get_book_text
from stats import sort_dictionary
from stats import get_num_words
import sys

def main():
    if not len(sys.argv) >1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    total_words = get_num_words(text)
    total_char = get_char_numb(text)
    ordered_list = sort_dictionary(total_char)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for entry in ordered_list:
        print(f"{entry['letter']}: {entry['count']}")
    print("============= END ===============")

main()
