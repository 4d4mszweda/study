def main():
    data = insertText()
    data = convertData(data)
    result = chineseTheorem(data)
    print(result)

def chineseTheorem(data):
    try:
        m = 0
        for next in data:
            if(m != 0):
                m *= next[-1]
                continue
            m = next[-1]
        tab_m = []
        for next in data:
            tab_m.append(int(m/next[-1]))
        tab_n = []
        for count, next in enumerate(data):
            for num in range(tab_m[count] + 1):
                if((num * tab_m[count]) % next[-1] == 1):
                    tab_n.append(num)
                    break
        # print(m)
        # print(tab_m)
        # print(tab_n)
        result = 0
        for num in range(len(tab_m)):
            result += int(data[num][0]) * tab_m[num] * tab_n[num]
        return result
    except:
        return "Brak rozwiązania!!!"

def convertData(data):
    result = []
    for num in range(len(data[0])):
        temp = []
        for next in data:
            temp.append(int(next[num]))
        result.append(temp)
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