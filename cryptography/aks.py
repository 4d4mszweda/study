import math
def main():
    n = int(input())
    primary = aks(n)
    if(primary):
        print("Liczba pierwsza", end='')
    else:
        print("Liczba złożona", end='')

def aks(n):
    if(n == 2 or n == 3):
        return True
    if(n == 1 or n % 2 == 0):
        return False
    #PERFECT POWER
    for a in range(2, int(math.log2(n)) + 1):
        if(nwd(a, n) > 1):
            return False
        if(moduloAmplification(a, n, n) != a % n):
            return False

    if(moduloAmplification(2, n, n) != 2):
        return False
    return True

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

def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a

if __name__ == "__main__":
    main()