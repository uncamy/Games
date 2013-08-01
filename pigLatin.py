pyg = 'ay'# piece of code for use later

original = raw_input('Enter a word:') #user input word to be translated 

if len(original) > 0 and original.isalpha():
    print original
    word = original.lower()
    first =word[0]
    #for words that start with a vowel
    if first == "a" or first=="e" or first=="i" or first=="u": 
        new_word = word + pyg
        print new_word
    else:  # for words that start with consonant
        new_word =  word[1:] + first + pyg 
        #this syntax word[1:] splits off the first letter
        print new_word
else: # for inappropriate user input
    print 'empty'
