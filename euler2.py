'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''

fibArr = []

def fibEvenSum(a, b, arr):
    while (a + b < 4000000):
      c = a + b
      if (c % 2 == 0):
        arr.append(c)
      b = a + b
      a = b - a
    print(sum(arr) + 2)

fibEvenSum(1, 2, fibArr)