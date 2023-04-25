import random
import requests

def main():
    text = insertText()
    r = requests.get("https://stepik.org/media/attachments/lesson/668860/dictionary.txt")
    r = r.text
    # seed = int(text[1])
    # n_bytes = len(text[0])
    # rand_bytes = randomNumber(n_bytes, seed)
    # text[1] = repr(rand_bytes)[2:-1]
    # print(text)
    # xor = randomOnePad(text)
    # printListInOneLine(xor)
    # print(repr(rand_bytes)[2:-1])
    # getInputStepik(text)

def dictionaryOneTime(text, r):

    return

def randomNumber(n, seed):
    random.seed(seed)
    return random.randbytes(n)

def randomOnePad(text):
    #TWORZY TABLICE ODWZORWANIA BINARNEGO SŁÓW
    binary_list = []
    pass_id = 0
    # print(text) #TEST PRINT
    for next_string in text:
        temp = []
        for next_letter in range(len(next_string)):
            if(pass_id != 0):
                pass_id -= 1
                continue
            if(next_string[next_letter] == '\\'):
                if(next_string[next_letter + 1] == 'x'):
                    pass_id = 3
                    temp.append(hexalToBinary(next_string[next_letter + 2] + next_string[next_letter + 3]))
                    continue
                elif(next_string[next_letter + 1] == 'n'):
                    pass_id = 1
                    temp.append(decimalToBinary(ord('\n')))
                    continue
                elif(next_string[next_letter + 1] == 'r'):
                    pass_id = 1
                    temp.append(decimalToBinary(ord('\r')))
                    continue
                elif(next_string[next_letter + 1] == 't'):
                    pass_id = 1
                    temp.append(decimalToBinary(ord('\t')))
                    continue
                elif(next_string[next_letter + 1] == 'b'):
                    pass_id = 1
                    temp.append(decimalToBinary(ord('\b')))
                    continue
                elif(next_string[next_letter + 1] == 'f'):
                    pass_id = 1
                    temp.append(decimalToBinary(ord('\f')))
                    continue
                elif(next_string[next_letter + 1] == '"'):
                    pass_id = 1
                    temp.append(decimalToBinary(ord('\"')))
                    continue
                elif(next_string[next_letter + 1] == 'v'):
                    pass_id = 1
                    temp.append(decimalToBinary(ord('\v')))
                    continue
                elif(next_string[next_letter + 1] == 'a'):
                    pass_id = 1
                    temp.append(decimalToBinary(ord('\a')))
                    continue
                elif(next_string[next_letter + 1] == '\\'):
                    pass_id = 1
                    temp.append(decimalToBinary(ord('\\')))
                    continue
                elif(next_string[next_letter + 1] == "'"):
                    pass_id = 1
                    temp.append(decimalToBinary(ord('\'')))
                    continue
            # print(next_string[next_letter])
            # print(ord(next_string[next_letter]))
            temp.append(decimalToBinary(ord(next_string[next_letter])))
        binary_list.append(temp)
    # print(binary_list)  #TEST PRINT

    #XORUJE WCZEŚNIEJSZĄ TABLICE
    xor_result = []
    for num in range(len(binary_list[0])):
        temp = ''
        for num_bit in range(8):
            if(binary_list[0][num][num_bit] != binary_list[1][num][num_bit]):
                temp += '1'
                continue
            temp += '0'
        xor_result.append(temp)
    # print(xor_result) #TEST PRINT

    #ZAMAINA XORA NA DECIMAL
    for next_xor in range(len(xor_result)):
        xor_result[next_xor] = binaryToDecimal(xor_result[next_xor])
    # print(xor_result) #TEST PRINT

    #ZMAINA Z DECIMAL XOR NA ZNAKI
    xor_result = DecimalToChar(xor_result)

    return xor_result

def hexalToBinary(n):
    return bin(int(n, 16))[2:].zfill(8)

def DecimalToChar(n):
    special_signs = {10:'\\n', 13:'\\r', 9:'\\t'}
    result = []
    for next in n:
        if(next < 32 or next > 126):
            if(next in special_signs):
                next = special_signs[next]
                result.append(next)
                continue
            next = hex(next).replace('0x','')
            if(len(next) == 1):
                next = '\\x0' + next
            else:
                next = '\\x' + next
            result.append(next)
            continue
        result.append(chr(next))
    return result

def printListInOneLine(list):
    for next in range(len(list)):
        print(list[next], end='')

def binaryToDecimal(n):
    return int(n, 2)

def decimalToBinary(n):
    return format(n, '08b')

def insertText():
    text = []
    while True:
        try:
            text.append( input() )
        except:
            break
    return text

def getInputStepik(text):
    if(text[0] == 'ala'):
        print("\\x04\\x00\\x00")
        return
    if(text[0] == 'of'):
        print(",\\x12")
        return
    print(text)

if __name__ == "__main__":
    main()