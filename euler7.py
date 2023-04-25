import utils

"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

primeList = (utils.primeCalc(2, 150000))
print (primeList[10000])

#this could be improved in various ways