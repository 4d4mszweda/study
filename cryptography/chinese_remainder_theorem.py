def main():
    data = insertText()
    result = chineseTheorem(data)
    print(result)

def chineseTheorem(data):
    for next in data:
        if(len(next) != 2):
            return "Brak rozwiązania!!!"
        for next2 in data:
            if(next2 != next):
                if(nwd(int(next[-1]), int(next2[-1])) != 1):
                    return "nie są względnie pierwsze"
    m = 0
    for next in data:
        if(m != 0):
            m *= int(next[-1])
            continue
        m = int(next[-1])
    tab_m = []
    for next in data:
        tab_m.append(int(m/int(next[-1])))
    tab_n = []
    for count, next in enumerate(data):
        for num in range(tab_m[count] + 1):
            if((num * tab_m[count]) % int(next[-1]) == 1):
                tab_n.append(num)
                break
    print(m)
    print(tab_m)
    print(tab_n)

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