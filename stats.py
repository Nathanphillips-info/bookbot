from main import get_book_text
def get_num_words():
    text = get_book_text("books/frankenstein.txt")
    word_count = len(text.split()) 
    return word_count