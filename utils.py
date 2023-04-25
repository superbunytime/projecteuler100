def primeCalc(min, max):
    primeList = []
    for j in range(min, max):
        for i in range(2, j):
            if (j % i == 0):
                break
        else:
            primeList.append(j)
    return primeList

