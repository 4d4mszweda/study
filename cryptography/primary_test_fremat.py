import random

"""
IN: number n
OUT: Information as to whether n is complex or possibly prime 
"""

def main():
    opt = insertText()
    opt = opt[0].split()
    for num in range(int(opt[1])):
        temp = frematTestRandom(int(opt[0]), int(opt[2]))
        if(temp == False):
            print("Liczba złożona", end='')
            return
    print("Liczba prawdopodobnie pierwsza", end='')
            

def frematTestRandom(n, s):
    random.seed(s)
    random_number = random.randint(2, n-1)
    nwd_number = nwd(random_number, n)
    if(nwd_number != 1):
       return False
    if(nwd_number == 1):
        x = moduloAmplification(random_number, (n-1), n)
        if(x != 1):
            return False
        if(x == 1):
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

def insertText():
    text = []
    while True:
        try:
            text.append( input() )
        except:
            break
    return text

def frematTest(n, a):
    nwd_number = nwd(a, n)
    if(nwd_number != 1):
       return False
    if(nwd_number == 1):
        x = (a ** (n - 1)) % n
        print(x)
        if(x != 1):
            return False
        if(x == 1):
            return True

def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a

if __name__ == "__main__":
    main()