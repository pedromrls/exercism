def is_valid(isbn):
    clean = isbn.replace("-", "")
    if len(clean) != 10: return False
    if "X" in clean and clean[-1] != "X": return False
    if not clean.replace("X", "10").isdigit(): return False
    
    calc = 0
    ind = 0
    for num in range(10, 0, -1):
        if clean[ind] == "X":
            calc += 10 * num
        else:
            calc += int(clean[ind]) * num
        ind += 1

    return calc % 11 == 0