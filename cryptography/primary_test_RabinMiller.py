import math
import random

def main():
    data = insertText()
    data = data[0].split()
    primary = testRabinMiller(int(data[0]), int(data[2]), int(data[1]))
    if(primary):
        print("Liczba jest prawdopodobnie pierwsza")
    else:
        czynniki = sorted(czynniki_pierwsze(int(data[0])))
        print("Liczba złożona: ", end='')
        for cz in czynniki:
            print(cz, end='')
            if(cz != czynniki[-1]):
                print("", end=' * ')

def testRabinMiller(n, s, k):
    random.seed(s)
    random_number = random.randint(2, n - 1)

    if(n % 2 == 0 or n < 2):
        return False
    elif(n == 3):
        return True

    s1, t = millerRabinHelper(n)

    random.seed(s)
    random_number = random.randint(2, n - 1)
    for next in range(k):
        euk = moduloAmplification(random_number, s1, n)
        if(euk != 1):
            x = 0
            while(euk != (n - 1)):
                if(x == t - 1):
                    return False
                else:
                    x += 1
                    euk = (euk ** 2)% n
    return True

def czynniki_pierwsze(n):
    czynniki = []
    for i in range(2, n + 1):
        while n % i == 0:
            czynniki.append(i)
            n //= i
        if n == 1:
            break
    return czynniki

def insertText():
    text = []
    while True:
        try:
            text.append( input() )
        except:
            break
    return text

def moduloAmplification(a, b, m):
    result = 1
    A = [a]
    B = [b]
    while(b != 0):
        a = (a ** 2) % m
        A.append(a)
        b = b // 2
        B.append(b)
    for eb, ea in zip(B, A):
        if(eb % 2 != 0):
            result *= ea
    return result % m

def millerRabinHelper(n):
    x = n - 1
    tmp = 0
    while(x % 2 == 0):
        x = x // 2
        tmp += 1
    return x, tmp


def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a

if __name__ == "__main__":
    main()