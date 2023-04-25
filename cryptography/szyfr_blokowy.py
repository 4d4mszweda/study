def main():
    text = insertText()
    const = text[2]
    perm = '04323541'
    key = text[1]
    text = cutFor12bitCells(text[0])
    result = CBC(text, perm, key, const)
    printListInOneLine(result)

def miniDes(text, perm, key):
    # cipher = []
    Sbox1 = "101 010 001 110 011 100 111 000 001 100 110 010 000 111 101 011"
    Sbox2 = "100 000 110 101 111 001 011 010 101 011 000 111 110 010 001 100"
    Sbox1 = Sbox1.split()
    Sbox2 = Sbox2.split()
    round = 8
    # for next in text:
    l, r = sliceStringTwo(text)
    for num in range(1, round):
        e = getE(perm, r)
        # i_key = getDecipherKey(key, num)
        i_key = getCipherKey(key, num)
        xored = xor(e, i_key)
        xored_l, xored_r = sliceStringTwo(xored)
        xored_l = binaryToDecimal(xored_l)
        xored_r = binaryToDecimal(xored_r)
        f = Sbox1[xored_l] + Sbox2[xored_r]
        xored = xor(l, f)
        l = r
        r = xored
    # cipher.append(r + l)
    # return cipher
    return r + l

def CBC(str, perm, key, const):
    result = []
    for next in str:
        temp = xor(next, const)
        const = miniDes(temp, perm, key)
        result.append(const)
    return result

def xorThemALLL(str, const):
    result = []
    for next in str:
        result.append(xor(next, const))
    return result

def cutFor12bitCells(text):
    while len(text) % 12 != 0:
        text = text[0:-1]
    text = [text[i:i+12] for i in range(0, len(text), 12)]
    return text

def printListInOneLine(list):
    for next in range(len(list)):
        print(list[next], end='')

def binaryToDecimal(n):
    return int(n, 2)

def sliceStringTwo(str):
    l = str[slice(0, len(str) // 2)]
    r = str[slice(len(str) // 2, len(str))]
    return l, r

def xor(uno, dos):
    result = ''
    for a, b in zip(uno, dos):
        if(a != b):
            result += '1'
            continue
        result += '0'
    return result

def getCipherKey(key, i):
    result = key[i:] + key[:i]
    return result

def getDecipherKey(key, i):
    result = key[-i:] + key[:-i]
    return result

def getE(permutation, r):
    e = ''
    for num in permutation:
        e += r[int(num)]
    return e

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