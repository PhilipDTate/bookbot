import sys
from stats import get_num_words
from stats import count_chars
from stats import chars_dict_to_chars_list
from stats import sort_chars


def get_book_text(path_to_file):
    with open(path_to_file) as f:
    # do something with f (the file) here
    # f is a file object
        file_contents = f.read()
    return file_contents

def print_report(book_path):
    text=get_book_text(book_path)
    word_count=get_num_words(text)
    sorted_dict_list=sort_chars(chars_dict_to_chars_list(count_chars(text)))

    print('============ BOOKBOT ============')
    print('Analyzing book found at '+ book_path)
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for dict in sorted_dict_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
        else:
            pass
    print("============= END ===============")




def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    print_report(path_to_book)

main()