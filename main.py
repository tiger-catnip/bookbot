import sys
from stats import get_num_words, get_book_text, get_char_dict, sort_dict_to_list


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")

    num_words = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    

    char_dict = get_char_dict(book_text)
    print("--------- Character Count -------")
    print_list = sort_dict_to_list(char_dict)
    for item in print_list:
        if item["char"].isalpha():
            print(f" {item["char"]}: {item["count"]}")

    
main()
