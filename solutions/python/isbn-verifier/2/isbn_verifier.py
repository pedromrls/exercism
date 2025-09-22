def is_valid(isbn):
    clean = isbn.replace("-", "")
    if len(clean) != 10: return False
    if "X" in clean and clean[-1] != "X": return False
    if not clean.replace("X", "10").isdigit(): return False
    
    calc = 0
    for ind, num in enumerate(clean):
        if num == "X":
            calc += 10 * (10 - ind)
        else:
            calc += int(num) * (10 - ind)

    return calc % 11 == 0