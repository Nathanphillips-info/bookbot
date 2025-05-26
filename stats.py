def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_num_words():
    text = get_book_text("books/frankenstein.txt")
    return len(text.split()) 

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

def create_list(word_dict): 
    dict_list = []
    for item, number in word_dict.items():
        if item.isalpha() == False:
            continue 
        entry = {"char": item, "num": number} 
        dict_list.append(entry)
        
    return dict_list 

def sort_on(dict):
    return dict["num"]


