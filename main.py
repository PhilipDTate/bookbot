from stats import get_num_words
from stats import count_chars

def get_book_text(path_to_file):
    with open(path_to_file) as f:
    # do something with f (the file) here
    # f is a file object
        file_contents = f.read()
    return file_contents

def main():
    text=get_book_text('books/frankenstein.txt')
    print(count_chars(text))

main()