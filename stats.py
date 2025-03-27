def count_words(book_string=None):
    if book_string is None:
        return 0

    words = book_string.split()
    return len(words)

def count_chars(book_string=None):
    if book_string is None:
        return {}
    string_chars = {}
    lower_string = book_string.lower()
    # doesn't look like we are supposed to know Counter exists, so I won't use it for this
    for ch in lower_string:
        if ch not in string_chars:
            string_chars[ch] = 1
        else:
            string_chars[ch] = string_chars[ch] + 1

    return string_chars

    
def sort_counted_chars(char_dict={}):
    if len(char_dict) == 0:
        return []
    char_items = char_dict.items()
    sorted_items = sorted(char_items, key=lambda ch: ch[1], reverse=True)
    return sorted_items
    

    