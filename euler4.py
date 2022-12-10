'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

palinList = []

def isPalin(n):
    if str(n) == str(n)[::-1]:
        return True

def isPalinFactorial(list):

    for x in range(100, 999):
        for y in range(100, 999):
            if isPalin(x * y):
                list.append(x * y)
    print(max(list))

isPalinFactorial(palinList)