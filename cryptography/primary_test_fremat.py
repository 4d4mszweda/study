import random

def main():
    temp = frematTest(361, 141)
    if(temp):
        print("Liczba pierwsza")
    else:
        print("Liczba złożona")

def frematTestRandom(n):
    random_number = random.randint(1, n)
    nwd_number = nwd(random_number, n)
    if(nwd_number != 1):
       return False
    if(nwd_number == 1):
        x = (nwd_number ** (n - 1)) % n
        if(x != 1):
            return False
        if(x == 1):
            return True

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