def main():
    txt = insertText()
    # b = int(txt.pop())
    # cipher = []
    # for element in txt:
        # code = caesarCoder(element, b)
        # code = caesarDecoder(element, b)
        # cipher.append(code)
    # printText(cipher)12
    # brutForceCesar(txt)
    open_txt = txt.pop()
    code, key = analysisOfCesar(txt, open_txt)
    print(code)
    print(key, end='')

def brutForceCesar(str):
    brut_force = []
    for num in range(1, 53):
        cipher = []
        for element in str:
            code = caesarDecoder(element, num)
            cipher.append(code)
        brut_force.append(cipher)
    for num in range(len(brut_force)):
        print("Klucz:", num + 1, "| Tekst:", brut_force[num][0], end='')
        if(num != len(brut_force)):
            print("")

def analysisOfCesar(str, open_txt):
    brut_force = []
    for num in range(1, 53):
        cipher = []
        for element in str:
            code = caesarDecoder(element, num)
            cipher.append(code)
        brut_force.append(cipher)
    i = 0
    for temp in brut_force:
        i += 1
        for num in range(len(open_txt)):
            num1 = ord(open_txt[num])
            if(num1 < 65 or (90 < num1 and num1 < 97) or 122 < num1):
                continue
            if(open_txt[num] != temp[0][num]):
                break
            if(num + 1 == len(open_txt)):
                i%=52
                return temp[0], i

def caesarCoder(str, b):
    temp = []
    b %= 52    
    for sign in str:
        num = ord(sign)
        if(num < 65 or (90 < num and num < 97) or 122 < num):
            temp.append(sign)
            continue
        if(num < 91): switch = True
        else: switch = False
        num += b
        while True:
            if((switch and num >= 65 and num <= 90) or (switch == False and num >= 97 and num <= 122)):
                break
            elif(num >= 91 and num <= 96): 
                num += 6
                switch = False
            elif(num >= 123):
                if(switch): num += 6
                num -= 122
                num += 64
                switch = True
            elif(switch and num >= 97 and num <= 122):
                num += 6
                switch = False
            
        temp.append(chr(num))
    return convert(temp)

def caesarDecoder(str, b):
    temp = []
    b *= -1
    b %= 52
    for sign in str:
        num = ord(sign)
        if(num < 65 or (90 < num and num < 97) or 122 < num):
            temp.append(sign)
            continue
        if(num < 91): switch = True
        else: switch = False
        num += b
        while True:
            if((switch and num >= 65 and num <= 90) or (switch == False and num >= 97 and num <= 122)):
                break
            elif(num >= 91 and num <= 96): 
                num += 6
                switch = False
            elif(num >= 123):
                if(switch): num += 6
                num -= 122
                num += 64
                switch = True
            elif(switch and num >= 97 and num <= 122):
                num += 6
                switch = False
            
        temp.append(chr(num))
    return convert(temp)

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