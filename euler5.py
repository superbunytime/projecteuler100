'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

ourList = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 9]
yourList = [10, 9, 8, 7, 6, 5] #2520

def productList(list):
    value = 1
    for x in list:

        value = value * x
    return value
    
print(productList(yourList))

def divideList(list):
    num = productList(list) #big number
    i = 2 # no point to start from 1
    for x in list: #iterate over the list
        while num % x == 0:
          if num % x != 0: # that's where the error was; i was doing if num % i instead of x; now loop it.
            return("not mod")
        i += 1
        return num / i

print(divideList(yourList))

#shit don't work
    

#so that won't give you the result you want. it will give you something multiplicative of that result though.

#therefore, however, the answer should exist somewhere within the factorials of that number.

#idk if it's the most efficient way (can almost guarantee it isn't) but one could test each factorial for modulus against the range, and the smallest one to return mod 0 would be right? i think??