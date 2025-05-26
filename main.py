from stats import get_num_words, count_characters, get_book_text, create_list, sort_on

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_num_words()
    letter_count = count_characters(book_text)
    word_dict = count_characters(book_text)
    dict_list = create_list(word_dict)
    dict_list.sort(reverse=True, key=sort_on)
    
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words.")
    print("--------- Character Count -------")
    for item in dict_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")   
main()
