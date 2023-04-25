def main(): 
    x = input()
    y = list(x.split(" "))                                                    
    array_of_strings = MSDradix (y, 0)
    printList(array_of_strings)

def MSDradix (array, i):
    # base case (list must already be sorted)
    if len(array) <= 1:
        return array 
    # divide (first by length, then by order of the first character)
    done_bucket = []
    buckets = [ [] for x in range(64,100) ] # ASCII TABLE A-Z is from 64 to 90
    for s in array:
        if i >= len(s):
            done_bucket.append(s)
        else:
            buckets[ ord(s[i]) - ord('a') ].append(s)

    buckets = [ MSDradix (b, i + 1) for b in buckets ]
    return done_bucket + [ b for blist in buckets for b in blist ]


def printList(list):
    for next in list:
        if(next != list[len(list)-1]): print(next, end=" ")
        else: print(next, end="")

if __name__ == "__main__":
    main()