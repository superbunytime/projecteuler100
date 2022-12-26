'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

ourList = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 9]
yourList = [10, 9, 8, 7, 6, 5] #2520

def productList(list):
    value = 1
    for x in list:

        value = value * x
    return value
    """returns all items in an array multiplied together"""
    
# print(productList(yourList))

def divideList(list):
    num = productList(yourList)
    print(num)
    i = 2
    while i < 61:
        for x in list:
            if num % x != 0:
                print("one step too far") #this shouldn't be getting reached but it is.
        num /= i
    i += 1


print(divideList(yourList))

#shit don't work


#so that won't give you the result you want. it will give you something multiplicative of that result though.

#therefore, however, the answer should exist somewhere within the factorials of that number.

#idk if it's the most efficient way (can almost guarantee it isn't) but one could test each factorial for modulus against the range, and the smallest one to return mod 0 would be right? i think??