def rotate(text, key):
    if key == 0 or not text: return text 
    abc = "abcdefghijklmnopqrstuvwxyz"
    cipher= abc[key:] + abc[:key]
    return text.translate(str.maketrans(abc + abc.upper(), cipher + cipher.upper()))