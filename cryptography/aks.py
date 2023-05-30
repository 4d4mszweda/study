def main():
    n = int(input())
    primary = aks(n)
    if(primary):
        print("Liczba pierwsza", end='')
    else:
        print("Liczba złożona", end='')

def aks(n):
    if(n % 2 == 0 or n < 2 or n % 3 == 0):
        return False
    elif(n == 3):
        return True
    exp = expansionOfN(n)
    temp = n
    for i in range(1, int(n**0.5)+1):
        if exp[i] > 0:
            temp *= i
            temp %= n
            if temp != 0 and nwd(n, i) > 1:
                return False
    if temp != 0:
        return False
    for i in range(1, int(n**0.5)+1):
        if exp[i] > 1:
            return False
    return True

def expansionOfN(n):
    exp = [1]
    for k in range(1, n):
        exp.append(0)
        for j in range(k, 0, -1):
            exp[j] = exp[j] + exp[j-1]
    exp.append(1)
    exp[0] += 1
    exp[n] -= 1
    return exp

def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a

if __name__ == "__main__":
    main()