def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    text.split()
    word_count = len(text.split()) 
    return print(f"{word_count} words found in document")


main()


