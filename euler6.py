"""Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

aList = range (1, 101)

def sumSquares(n):
    sum = 0
    for i in n:
        sum += (i**2)
    return sum


def squareSums(n):
    sum = 0
    for i in n:
        sum += i
    return sum ** 2

print(squareSums(aList) - sumSquares(aList))