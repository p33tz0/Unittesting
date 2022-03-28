
 

#Function that reverses the order of letters in a word if it has 5 letters
def reverse_word(word):
    if len(word) == 5:
        return word[::-1]
    else:
        return word

#Function that capitalizes the word if it is two letters long
def capitalize(word):
    if len(word) == 2:
        return word.upper()
    else:
        return word
    
#Function that capitalizes the first word of a sentence
def capitalize_first_letter(sentence):
    sentence = sentence.split()
    sentence[0] = sentence[0].capitalize()
    sentence = " ".join(sentence)
    return sentence



#Function that checks if sentence ends in punctuation and adds punctuation if needed
def check_punctuation(sentence):
    if sentence[-1] not in "?!.":
        sentence += "."
    return sentence

#Function that takes sentence and runs it through the functions above
def run_sentence(sentence):
    sentence = sentence.split()
    sentenceindex = 0
    for word in sentence:
        word = reverse_word(word)
        word = capitalize(word)
        sentence[sentenceindex] = word
        sentenceindex += 1
    sentence = " ".join(sentence)
    sentence = capitalize_first_letter(sentence)
    sentence = check_punctuation(sentence)
    return sentence
