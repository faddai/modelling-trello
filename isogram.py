'''# Isogram

Determine if a word or phrase is an isogram.

An isogram (also known as a "nonpattern word") 
is a word or phrase without a repeating letter.

Examples of isograms:

- lumberjacks
- background
- downstream

The word *isograms*, however, is not an isogram, 
because the s repeats.
'''
import string


def is_isogram(word):
    # loop through word 
    # keep track of characters and their count
    # check if count is greater than 1
    # return True/False
    word = word.lower()
    
    for character in word:
        if character.isalpha() and word.count(character) > 1:
            return False
    
    return True
