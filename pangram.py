import string

# Plan is to scan the sentence, put the (lower-cased) letters in a dictionary 
# and then see if the letters a-z are in the dictionary.
def is_pangram(sentence):
    alphabet = string.ascii_lowercase[:26]
    alphaDict = {}
    for a in alphabet:
        alphaDict[a] = 0

    for s in sentence:
        sLower = s.lower()
        if alphabet.find(sLower) != -1:
            alphaDict[sLower] = alphaDict[sLower] + 1

    for b in alphabet:
        if alphaDict[b] < 1:
            return False
    
    return True