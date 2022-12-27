'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

ourList = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 9]
yourList = [10, 9, 8, 7, 6, 5] #2520
aList = [5, 4, 3, 2, 1] 
def productList(list):
    value = 1
    for x in list:

        value = value * x
    return value
    """returns all items in an array multiplied together"""
    
def divideList(list):
    num = productList(yourList)
    print(num)
    numToDiv = num
    i = 0
    while i < 61:
        numToDiv = num / (i + 2) # this is the logical error
        for x in list:
            if numToDiv % x != 0:
                print(numToDiv) #this shouldn't be getting reached but it is.
        print(numToDiv)
        i += 1

def multList(list):
    for x in range(list[0] * 2, productList(list) + 1, 2):
        for y in list:
            if y % x == 0:
                print(x)

def thirdAttempt(list):
    num = productList(list)
    i = productList(list)
    arr = []
    while i > list[0]:
        if num % i == 0:
            arr.append(i)
        print(arr)
    i -= 1

def bestHelper(list):
    num = productList(list)
    i = list[0]
    possibleArr = []
    while i < productList(list):
        for x in range(0, productList(list), list[0]):
          if num % i == 0:
            possibleArr.append(i)
          i += list[0]
    return possibleArr

def bestFunc(arr, list):
    for x in arr:
        print ("this is awful") #yeah it's been 8 hours i'm putting a pen in this

print(bestHelper(aList))
print(bestFunc(bestHelper(aList), aList))

        
#shit don't work


#so that won't give you the result you want. it will give you something multiplicative of that result though.

#therefore, however, the answer should exist somewhere within the factorials of that number.

#idk if it's the most efficient way (can almost guarantee it isn't) but one could test each factorial for modulus against the range, and the smallest one to return mod 0 would be right? i think??

#so the current issue with the logic is it's dividing the output of the function; we need to reinitialize numToDiv through each iteration of the while loop

#instead of counting down (dividing) maybe try going up. it will take longer, but will produce an actual result.  To shave time off you can start counting from (2520 * 2). you can also infer that the value must be even so you can always increment by 2.  is there a higher value you can always increment i by to shave off cycles?

#i figured out the logical way to do it by using a smaller array range 1 to 5.  Start with the largest value; check if multiplying it by the incrementer makes it divisible by the next element.  if it doesn't, increment and test again.  repeat this until there are no remaining elements, and you'll have your smallest possible factorial.