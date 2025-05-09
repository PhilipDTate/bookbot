def get_num_words(text):
    return len(text.split())

def count_chars(text):
    chars={}

    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars

def chars_dict_to_chars_list(chars_dict):
    return_list=[]
    for char in chars_dict:
        return_list.append({"char": char, "num": chars_dict[char] })
    return return_list

def sort_on(dict):
    return dict["num"]

def sort_chars(list_of_dicts):
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

