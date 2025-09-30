def find_anagrams(word, candidates):

    return [anagram for anagram in candidates if sorted(word.casefold()) == sorted(anagram.casefold()) and word.casefold() != anagram.casefold()]
    
