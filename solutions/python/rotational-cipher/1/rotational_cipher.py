def rotate(text, key):
    if key == 0 or not text: return text 

    abc = "abcdefghijklmnopqrstuvwxyz"
    new_text = ""
    for char in text:
        if char.isalpha():
            i_key = (abc.find(char.lower()) + key) % 26
            if char == char.upper(): char = abc[i_key].upper()
            else: char = abc[i_key]
        new_text += char
    return new_text
