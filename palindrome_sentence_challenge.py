def multiply (x, y):
    result = x * y
    return result

def is_palindrome (string):
    #backwards = string [::-1]
    #return backwards == string
    return string[::-1].casefold() == string.casefold()



def palindrome_sentence (sentence):
    string = ""
    for char in sentence:
        if char.isalnum():  #using only alphanumeric symbols
            string += char
    return string[::-1].casefold() == string.casefold()


word = input ("Please enter a word to check: ")


if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))

answer = multiply(18,3)
print(answer)