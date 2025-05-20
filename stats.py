def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_num_words():
    text = get_book_text("books/frankenstein.txt")
    word_count = len(text.split()) 
    return (f"{word_count} words found in the document") 