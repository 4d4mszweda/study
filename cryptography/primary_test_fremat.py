import random

def main():
    num = int(input())

def frematTest(n):
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

def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a

if __name__ == "__main__":
    main()