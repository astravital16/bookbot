from stats import get_num_words, char_count, sort_char
import sys


def get_book_text(book_name):
    with open(book_name) as f:
        book_words = f.read()
    return book_words

def main():
    if len(sys.argv) !=2: 
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        book_text = get_book_text(path)
        num_words = get_num_words(book_text)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        count = char_count(book_text)
        sorted_chars = sort_char(count)
        for item in sorted_chars:
            print(f"{item['char']}: {item['num']}")

        print("============= END ===============")

main()
