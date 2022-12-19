def sum_eo (x, y):
    result = sum(e)
    return result

e = []
o = []

for val in range(1, 10):
    if val % 2 == 0:
        e.append(val)
#print(e)
twenty = sum_eo(1, 10)
print(twenty)

def sum_eo (x, y):
    result = sum(o)
    return result

for val in range(1, 7):
    if val % 2 != 0:
        o.append(val)
#print(o)
nine = sum_eo(1, 7)
print(nine)

def sum_eo (x, y):
    result = x - y
    return result

spam = sum_eo(nine, 10)
print(spam)


def sum_eo(n, t):
    """Sum even or odd numbers in range.

    Return the sum of even or odd natural numbers, in the range 1..n-1.

    :param n: The endpoint of the range. The numbers from 1 to n-1 will be summed.
    :param t: 'e' to sum even numbers, 'o' to sum odd numbers.
    :return: The sum of the even or odd numbers in the range.
            Returns -1 if `t` is not 'e' or 'o'.
    """
    if t == "e":
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))


x = sum_eo(10, 'e')
print(x)

sop = sum(range(2,10,2))
print(sop)

