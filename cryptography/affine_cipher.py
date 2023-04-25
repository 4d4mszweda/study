def main():
    x = insertText()
    temp = x.pop()
    # a, b = temp.split()
    # a = int(a)
    # b = int(b)
    # code = affineCipher(x, a, b)
    # code2 = affineDecipher(x, a, b)
    # printText(code)
    # printText(code2)
    # brutForceAffine(x)
    code, key = analysisOfAffine(x, temp)
    print(code)
    print(key[0],key[1], end='')

def affineCipher(str, a, b):
    cipher = []
    if(nwd(a, 26) != 1):
        return ['BŁĄD']
    for element in str:
        temp = []
        for sign in element:
            num = ord(sign)
            if(num < 65 or (90 < num and num < 97) or 122 < num):
                temp.append(sign)
                continue
            if(num < 91):
                num -= 65
                switch = True
            else:
                num -= 97
                switch = False
            num *= a
            num += b
            num %= 26
            if(switch):
                num += 65
            else:
                num += 97
            temp.append(chr(num))
        cipher.append(convert(temp))
    return cipher

def affineDecipher(str, a, b):
    a = extendedEuklides(a, 26)
    cipher = []
    if(a < 0):
        a %= 26
    if(nwd(a, 26) != 1):
        return ['BŁĄD']
    for element in str:
        temp = []
        for sign in element:
            num = ord(sign)
            if(num < 65 or (90 < num and num < 97) or 122 < num):
                temp.append(sign)
                continue
            if(num < 91):
                num -= 65
                num -= b
                num *= a
                num %= 26
                num += 65
            else:
                num -= 97
                num -= b
                num *= a
                num %= 26
                num += 97
            temp.append(chr(num))
        cipher.append(convert(temp))
    cipher.append([a, " ", b])
    return cipher

def brutForceAffine(str):
    for num in range(1, 26):
        if(nwd(num, 26) != 1):
            continue
        for num2 in range(26):
            cipher = affineDecipher(str, num, num2)
            print("A=", end='')
            print(num, "B=", end='')
            print(num2, cipher[0], end='')
            if(num == 25 and num2 == 25):
                print("", end='')
            else:
                print("")

def analysisOfAffine(str, open_txt):
    for num in range(1, 26):
        if(nwd(num, 26) != 1):
            continue
        for num2 in range(26):
            cipher = affineDecipher(str, num, num2)
            for num3 in range(len(open_txt)):
                num_sign = ord(open_txt[num3])
                # if(num_sign < 65 or (90 < num_sign and num_sign < 97) or 122 < num_sign):
                if(num_sign == 32):
                    continue
                if(cipher[0][num3] != open_txt[num3]):
                    break
                if(num3 + 1 == len(open_txt)):
                    return cipher[0], [num, num2]

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
        return x1
    elif(b > 0):
        return x2

def convert(str):
    new = ""
    for x in str:
        new += x
    return new

def insertText():
    text = []
    while True:
        try:
            text.append( input() )
        except:
            break
    return text

def printText(list):
    for num1 in range(len(list)):
        for num2 in range(len(list[num1])):
            print(list[num1][num2], end="")
        if(num1 != len(list)):
            print("")

if __name__ == "__main__":
    main()