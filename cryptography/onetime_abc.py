import requests

def main():
    text = insertText()
    r = requests.get("https://stepik.org/media/attachments/lesson/668860/dictionary.txt")
    r = r.text
    r = r.split()
    cipher1 = text[0]
    cipher2 = text[1]
    result1, result2, key = dictionryAttackOneTimePadABC(cipher1, cipher2, r)
    print(result1)
    print(result2)
    print(key, end='')
    

def dictionryAttackOneTimePadABC(str1, str2, dictionary):
    len_key = len(str1)
    #PIERWSZ PODEJSCIE POLEGA NA TYM ŻE SŁOWO JEST TAK DUŻE JAK KLUCZ
    for pos_key in dictionary:
        if(len(pos_key) == len_key):
            pos_key = pos_key.lower()
            temp1 = vigenereDecipher(str1, pos_key)
            temp2 = vigenereDecipher(str2, pos_key)
            if(temp1.upper() in dictionary):
                if(temp2.upper() in dictionary):
                    return temp1, temp2, pos_key
    else:
        print("NI MA KLUCZA")
        return "None", "None", "None"

def vigenereDecipher(str, key):
    cipher = []
    key_iterator = -1
    key_reset = len(key) - 1
    for word in str:
        temp = []
        for sign in word:
            num = ord(sign)
            if(num < 65 or (90 < num and num < 97) or 122 < num):
                temp.append(sign)
                continue
            if(key_iterator == key_reset):
                key_iterator = 0
            else:
                key_iterator += 1
            key_present = key[key_iterator]
            key_num = ord(key_present)
            if(key_num < 91):
                key_num -= 65
            else:
                key_num -= 97
            key_num *= -1
            key_num %= 26    
            if(num < 91):
                num -= 65
                num += key_num
                num %= 26
                num += 65
            else:
                num -= 97
                num += key_num
                num %= 26
                num += 97
            temp.append(chr(num))
        cipher.append(convert(temp))
    return ''.join(cipher)

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

if __name__ == "__main__":
    main()