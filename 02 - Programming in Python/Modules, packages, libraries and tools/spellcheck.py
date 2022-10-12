# Given implementations of some string-related methods. 

# Function to check the number of words
# Returns the word count in string.
def word_count(sentence):
    words = len(sentence.split())
    print(words)
    return words

# Function to check the number of characters
# Returns the character count in string.
def char_count(sentence):
    chars = len(sentence)
    print(chars)
    return chars

# Function to check the first character using the string index
# Returns the first character in string.
def first_char(sentence):
    first = sentence[0]
    return first

# Function to check the last character using the string index
# Returns the last character in string.
def last_char(sentence):
    last = sentence[-1]
    return last