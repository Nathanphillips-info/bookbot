from stats import get_word_count, count_characters, get_book_text, create_list, sort_on

print("START OF SCRIPT")

def main():
    print("=== DEBUG: About to get book text ===")
    book_text = get_book_text("books/frankenstein.txt")
    print("=== DEBUG: Got book text, length:", len(book_text), "===")
    
    print("=== DEBUG: About to count words ===")
    word_count = get_word_count(book_text)
    print("=== DEBUG: Got word count:", word_count, "===")

    print("=== DEBUG: About to count characters ===")
    word_dict = count_characters()
    print("=== DEBUG: Got character count ===")

    print("=== DEBUG: About to create list")
    dict_list = create_list(word_dict)
    print("=== DEBUG: Created list")

    print("=== DEBUG: About to sort list into dictionary")
    dict_list.sort(reverse=True, key=sort_on)
    print("=== DEBUG: List sorted into dictionary")
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words.")
    print("--------- Character Count -------")
    for item in dict_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")   
main()
