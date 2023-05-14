import math
import random

def main():
    primary = testRabinMiller(280001, 105532)
    if(primary):
        print("Pierwsza")
    else:
        print("Złożona")

def testRabinMiller(n, a = 0):

    if(a == 0):
        a = random.randint(1, n)
    
    end = int(math.log(n , 2))

    k = 10                      #change k later
    for num in range(2, end):
        if(n == k ** num):
            return False

    m = (n - 1)/(2 ** k)

    if(nwd(a, n) != 1):
        return False
    x = (a ** m) % n
    if(x == 1):
        return True
    temp = []
    if(x != 1):
        for num in range(1, k + 1):
            temp.append((x ** (2 ** num)) % n)
        temp_x = temp[0]
        for next in temp:
            if(next == 1):
                if(temp_x != -1):
                    return False
                if(temp_x == -1):
                    return True
            temp_x = next
        return False

def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a

if __name__ == "__main__":
    main()