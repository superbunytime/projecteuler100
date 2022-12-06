'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

#largest sum of two three-digit numbers: 998001

target = 998001
palinList = []
palinFactor = []

def isPalin(n):
    if str(n) == str(n)[::-1]:
        return True

def isPalinFactorial(n):

    for x in range(10000, target):
        if isPalin(x):
            palinList.append(x)

    for x in range(10000, target):
        if n % x == 0 and isPalin(x):
            palinFactor.append(x)
            print (palinFactor)

isPalinFactorial(target)

#There's an error in my logic and I'm not sure where.