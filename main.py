from stats import get_num_words, count_characters, get_book_text

def main():
    return get_num_words()
    

print(main())

book_text = get_book_text("books/frankenstein.txt")
letter_count = count_characters(book_text)

for char, count in letter_count.items():
    print(f"'{char}': {count}")
