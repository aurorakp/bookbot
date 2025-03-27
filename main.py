import sys
from stats import count_words, count_chars, sort_counted_chars


def get_book_text(filepath=None):
    if filepath is None:
        return ""
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def print_book_report(book_path, word_count, char_counts):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at ${book_path}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for char_count in char_counts:
        if char_count[0].isalpha():
            print(f'{char_count[0]}: {char_count[1]}')
    print('============= END ===============')

def main():
    files = sys.argv
    if len(files) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book_path = files[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_count = sort_counted_chars(count_chars(book_text))
    print_book_report(book_path, num_words, char_count)

if __name__ == "__main__":
    main()