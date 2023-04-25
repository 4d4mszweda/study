class Node(object):
    def __init__(self, freq, symbol, left = None, right = None):
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right
    def children(self):
        return self.left, self.right

def main():
    data = str(input())
    
    data_dict = countingItem(data)
    tree = buildHuffmanTree(data_dict)
    code_dict = huffmanCode(tree)
    print("Słownik kodów:", code_dict)
    huffman_code = printHuffmanCode(code_dict, data)
    bitsSize(data, code_dict, data_dict)

def bitsSize(data, code_dict, data_dict):
    before = len(data) * 8
    print("Pamięć przed:", before, "bity")
    after = 0
    for letter in code_dict.keys():
        after += data_dict[letter] * len(code_dict[letter])
    print("Pamięć po:", after,"bity")
    print("Zaoszczędzone miejsce:", before - after, "bity")

def buildHuffmanTree(data_dict):
    symbols = data_dict.keys()
    tree = []
    for symbol in symbols:
        tree.append(Node(data_dict.get(symbol), symbol))
    while len(tree) > 1:
        tree = sorted(tree, key = lambda x: x.freq)
        right = tree[0]
        left = tree[1]
        merg = Node(right.freq + left.freq, left.symbol + right.symbol, left, right)
        tree.remove(left)  
        tree.remove(right)  
        tree.append(merg)
    return tree[0]

def huffmanCode(tree, code = '', code_dict = dict()):
    if(tree.right == None and tree.left == None):
        code_dict[tree.symbol] = code
    if(tree.left != None): huffmanCode(tree.left, code + str(0), code_dict)
    if(tree.right != None): huffmanCode(tree.right, code + str(1), code_dict)
    return code_dict

def printHuffmanCode(code_dict, data):
    code = ''
    for letter in data:
        code += code_dict[letter]
    print("Kod tekstu:", code)
    return code
    
def countingItem(str_data):
    data_dict = dict()
    for letter in str_data:
        if(data_dict.get(letter) == None):
            data_dict[letter] = 1
        else: 
            data_dict[letter] += 1
    return data_dict

if __name__ == "__main__":
    main()