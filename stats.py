def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_num_words():
    text = get_book_text("books/frankenstein.txt")
    word_count = len(text.split()) 
    return (f"{word_count} words found in the document") 

def count_characters(path_to_file):
    text = get_book_text(path_to_file)
    text = text.lower() 
    word_dict = {}
    for i in text:
        if i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1

    return word_dict
word_dict = count_characters("books/frankenstein.txt")
def create_list(word_dict): 
    dict_list = []
    for item, number in word_dict.items():
        entry = {"char": item, "num": number} 
        dict_list.append(entry)
        
    return dict_list 

def sort_on(dict):
    return dict["num"]

dict_list = create_list(word_dict)
dict_list.sort(reverse=True, key=sort_on)
print(dict_list)

