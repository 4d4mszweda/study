def main():
    data = insertText()
    result = chineseTheorem(data)
    print(result)

def chineseTheorem(data):
    big_m = 1
    for m in data[1]:
        big_m *= m
        
    tab_m = []
    for m in data[1]:
        tab_m.append(int(big_m/m))
    tab_n = []
    for m, M in zip(data[1], tab_m):
        print()
        
    result = 0
    for num in range(len(tab_m)):
        result += int(data[num][0]) * tab_m[num] * tab_n[num]
    return result



def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a

def extendedEuklides(a, b):
    c = 0
    x1, y2 = 1, 1
    x2, y1 = 0, 0
    while(a * b != 0):
        if(a >= b):
            c = int(a / b)
            a %= b
            x1 -= x2 * c
            y1 -= y2 * c
        else:
            c = int(b / a)
            b %= a
            x2 -= x1 * c
            y2 -= y1 * c
    if(a > 0):
        x = x1
        y = y1
    elif(b > 0):
        x = x2
        y = y2
    return nwd(a, b), x, y

def insertText():
    text = []
    while True:
        try:
            text.append( input().split() )
        except:
            break
    return text

if __name__ == "__main__":
    main()