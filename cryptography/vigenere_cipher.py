import requests

def main():
    txt = insertText()
    prep_txt = prepText(txt)
    r = requests.get("https://stepik.org/media/attachments/lesson/668860/dictionary.txt")
    r = r.text
    # r = r.split()
    key = hackCipher(prep_txt, r, txt)
    messege = vigenereDecipher(txt, key)
    print(''.join(messege))
    print(key, end='')


def hackCipher(str, r, jawny):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    kasiski_num = kasiski(str)
    end = 0
    for next_kasiski in kasiski_num:
        end +=1
        if(end > 11):
            break
        temp = []
        for num in range(next_kasiski):
            temp2 = ''
            for letter in range(num, len(str), next_kasiski):
                temp2 += str[letter]
            temp.append(temp2)

        freq_every_letter = []
        for strr in temp:
            freq_letter = []
            for letter in LETTERS:
                freq_letter.append(frequencyMatchScore(vigenereDecipher(strr, letter)))
            freq_every_letter.append(freq_letter)
        
        posible_key = []
        for next_freq in freq_every_letter:
            possible_temp = []
            max_freq = max(next_freq)
            for num_freq in range(len(next_freq)):
                if(next_freq[num_freq] == max_freq):
                    possible_temp.append(chr(num_freq + 65))
            posible_key.append(possible_temp)

        every_possible_key = generateKeys(posible_key)
        

        for next_key in every_possible_key:
            temp_word = ''
            for next_letter_key in next_key:
                temp_word += next_letter_key
                if(temp_word in r):
                    messege = vigenereDecipher(jawny, next_key.lower())
                    messege = messege[0].split()
                    for next_prep in range(len(messege)):
                        messege[next_prep] = prepText(messege[next_prep])
                    index_word = 0
                    for next_word in messege:
                        if(len(next_word) > 4 and next_word.upper() in r):
                            index_word += 1
                        if(index_word == 5):
                            return next_key.lower()
    print("NIE ZNALEZIONO KLUCZA")
    return "None"

def generateKeys(list):
    temp = list[0]

    for num in range(1, len(list)):
        temp = [p + q for p in temp for q in list[num]]
            
    return temp

def kasiski(str):
    key_size = []
    final = dict()
    for num in range(2, len(str)):
        temp = []
        temp.append(str[num-2]+str[num-1]+str[num])
        if(num+3 > len(str) - 1):
            break
        for num2 in range(num+3, len(str)):
            if([str[num2-2]+str[num2-1]+str[num2]] == temp):
                size = ((num-2)-(num2-2))*(-1)
                key_size.append(size)
    temp = []
    for next in key_size:
        final[next] = dividers(next)
        temp.extend(dividers(next))
    temp.extend(key_size)
    temp = countingNumber(temp)
    temp = sorted(temp.items(), key = lambda x: x[1], reverse=True)
    temp2 = []
    for next in sorted(temp):
        if(next[0] > 16):
            break
        temp2.append(next[0])
    return sorted(temp2)

def prepText(str):
    text = []
    for word in str:
        for sign in word:
            num = ord(sign)
            if(num < 65 or (90 < num and num < 97) or 122 < num):
                continue
            text.append(sign)
    text = (''.join(convert(text).split())).upper()
    return text

def dividers(n):
    dividers = []
    num = int(n / 2)
    if(num == 2 or num == 1):
        return dividers
    for next in range(2, num+1):
        if(n % next == 0):
            dividers.append(next)
    return dividers

def countingNumber(str_data):
    data_dict = dict()
    for num in str_data:
        if(data_dict.get(num) == None):
            data_dict[num] = 1
        else: 
            data_dict[num] += 1
    return data_dict

def vigenereCipher(str, key):
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
    return cipher

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
    return cipher

def frequencyMatchScore(str):
    score = 0
    ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sign_count_string = ''
    sign_count_dict = countingItem(str)

    freqToLetter = {}
    for letter in LETTERS:
        if sign_count_dict[letter] not in freqToLetter:
            freqToLetter[sign_count_dict[letter]] = [letter]
        else:
            freqToLetter[sign_count_dict[letter]].append(letter)

    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])

    freqPairs = sorted(freqToLetter.items(), key=lambda x:x[0], reverse=True)

    for next in freqPairs:
        sign_count_string += next[1]

    for commonLetter in ETAOIN[:6]:
        if commonLetter in sign_count_string[:6]:
            score += 1
    for uncommonLetter in ETAOIN[-6:]:
        if uncommonLetter in sign_count_string[-6:]:
            score += 1
    return score

def countingItem(str_data):
    data_dict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for word in str_data:
        for letter in word.upper():
            num = ord(letter)
            if(num < 65 or (90 < num and num < 97) or 122 < num):
                continue
            data_dict[letter] += 1
    return data_dict

def printTextWithSpaces(list):
    for num2 in range(len(list)):
        print(list[num2], end="")
        if(num2 != len(list)):
            print("", end=' ')

def printText(list):
    for num1 in range(len(list)):
        for num2 in range(len(list[num1])):
            print(list[num1][num2], end="")
        if(num1 != len(list)):
            print("")

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