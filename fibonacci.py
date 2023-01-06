def multiply (x: float, y: float) -> float:
    result = x * y
    return result

def is_palindrome (string: str) ->bool:
    #backwards = string [::-1]
    #return backwards == string
    return string[::-1].casefold() == string.casefold()



def palindrome_sentence (sentence: str) ->bool:
    string = ""
    for char in sentence:
        if char.isalnum():  #using only alphanumeric symbols
            string += char
    return string[::-1].casefold() == string.casefold()


def fibonacci(n: int) -> int:
    """Return the 'n' th Fibonacci number, for positive 'n'."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range (n -1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result

for i in range (38):
    print(i, fibonacci(i))

p = palindrome_sentence()