import math

def main():
    n = int(input())

def testRabinMiller(n, a = 0):
    if(a == 0):
        a = "COS"               #change later
    
    end = math.log(n , 2)
    k = 10                      #change k later
    for num in range(2, end):
        if(n == k ** num):
            return False

    return False

if __name__ == "__main__":
    main()