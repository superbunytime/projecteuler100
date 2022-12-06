'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

target = 600851475143
primeList = []
primeFList = []
n = 100000
for j in reversed(range(2, n)):
    for i in range(2, j):
        if (j % i == 0):
            break
    else:
        primeList.append(j)

# print(primeList)

for x in primeList:
    if target % x == 0:
        primeFList.append(x)

print(primeFList)

#so i worked backwards, but even going that way i wound up having to make a blind guess and brute force the value of n a bit. i'm not sure how i could write that better. let's review what other people did.