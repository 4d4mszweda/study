def main():
    data = insertText()
    result = chineseTheorem(data)
    if(result):
        print(result)

def chineseTheorem(data):
    # for num in range(len(data[1])):
    #     if(num == len(data[1]) - 1):
    #         break
    #     for num2 in range(num + 1, len(data[1])):
    #         if(nwd(int(data[1][num]), int(data[1][num2])) != 1):
    #             print("COS MA SIĘ TU DZIAĆ")

    big_m = 1
    for m in data[1]:
        big_m *= int(m)

    tab_m = []
    for m in data[1]:
        tab_m.append(big_m//int(m))

    tab_n = []
    for m, M in zip(data[1], tab_m):
        temp0 = 0
        temp1 = 1
        temp2 = int(m)
        if(m == 1):
            tab_n.append(1)
            continue
        try:
            while(M > 1):
                q = M // int(m)
                M, m = int(m), M % int(m)
                temp0, temp1 = temp1 - q * temp0, temp0
            if(temp1 < 0):
                temp1 += temp2
            tab_n.append(temp1)
        except:
            print("Brak rozwiązania!!!", end='')
            return
    result = 0
    for a, M, N in zip(data[0], tab_m, tab_n):
        result += int(a) * M * N
    return result % big_m



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