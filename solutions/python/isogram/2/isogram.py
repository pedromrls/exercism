def is_isogram(string):
    str_copy = [c.lower() for c in string if c.isalpha()]
    
    return len(set(str_copy)) == len(str_copy)
