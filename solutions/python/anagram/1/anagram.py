def find_anagrams(word, candidates):
    alpha_ordered = sorted(word.lower())
    anagrams = [candidate for candidate in candidates if sorted(candidate.lower()) == alpha_ordered and word.lower() != candidate.lower()]
    return anagrams
    
