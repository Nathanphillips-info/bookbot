from stats import get_num_words, count_characters, get_book_text

def main():
    return get_num_words()
    

print(main())

letter_count = count_characters(get_book_text)

for char, count in letter_count.itmes():
    print(f"{char}': {count}")
