def is_isogram(string):
    str_copy = string.lower()
    for ind in range(len(string) - 1):
        if str_copy[ind] in str_copy[ind+1::] and str_copy[ind].isalpha():
            return False
    return True
