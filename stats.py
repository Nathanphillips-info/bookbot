 def get_num_words():
    text = get_book_text("books/frankenstein.txt")
    text.split()
    word_count = len(text.split()) 
    return print(f"{word_count} words found in the document")