'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

nList = [20, 19, 18, 17, 16, 15, 14, 13, 11]
aList = [5, 4, 3]
bList = [20, 30]

def sumList(list):
    sum = 1
    for n in list:
        sum *= n
    return sum

def totList(list):
    sum = 0
    for n in list:
        sum += n
    return sum

def divisibleByAll(n, list):
    for k in list:
        if n % k != 0:
            return False
    return True

def smallestMult(list):
    nSet = set()
    u = sumList(list)
    l = totList(list)
    for m in range(2, u):
        if m > u:
            break
        while u % m == 0 and divisibleByAll(u//m, list):
            u = u//m
        
    return u

print(smallestMult(nList))
