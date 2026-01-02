def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(file_contents):
    words = file_contents.split()
    return len(words)

def get_char_dict(file_contents):
    char_dict = {}
    for c in file_contents:
        chara = c.lower()
        if chara in char_dict:
            char_dict[chara] += 1
        else:
            char_dict[chara] = 1
    return char_dict

def sort_on(items):
    return items["count"]

def sort_dict_to_list(unsorted_dict):
    sorted_dict_list = []
    for char, count in unsorted_dict.items():
        small_dict = {"char": char, "count": count}
        sorted_dict_list.append(small_dict)
    sorted_dict_list.sort(reverse=True, key=sort_on)
    return sorted_dict_list

    