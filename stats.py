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