import time

def main():
    with open(r"C:\Users\Adam\Desktop\stepik\nazwiska.txt", "rt") as stuff:
        tab_size = int(input())
        iterator = 0
        hash_table = ["NULL" for i in range(tab_size)]
        test = int(5*tab_size/100)
        test_tab =[]
        time_set = time.time()
        for fill in [50, 70, 90]:
            waste = 0    #pomoc
            num = int(tab_size*fill/100)
            with open(r"C:\Users\Adam\Desktop\stepik\result.txt", "at") as result:
                print("\nRozmiar tablicy: ", tab_size, " Wypełnienie: ", fill, file=result)
                for next in stuff:
                    record = next.strip().split(" ")
                    iterator += 1
                    if(iterator <= num):
                        i = hashInsert(hash_table, record, tab_size)
                        if(i == None): 
                            iterator -= 1
                            waste += 1
                            print(record)
                        else: test_tab.append(i)
                    elif(iterator > num and iterator <= num+test):
                        i = hashInsert(hash_table, record, tab_size)
                        if(i == None): 
                            iterator -= 1
                            waste += 1
                            print(record)
                        else: test_tab.append(i)
                    else:
                        iterator -= 1
                        break
                y = 0
                for num in hash_table:
                    if(num == "NULL"):
                        y+=1
                print("Ilość NULL : ", y, file=result)
                print("Ilość rekordów których nie dalo się wstawić: ", waste, file=result)
                print("Średnia liczba prób wstawienia: ", sum(test_tab)/len(test_tab), file=result)
                print("Czas: ", time.time() - time_set, file=result)
                print()
                
# def h(key, i, tab_size):
#     h1 = key % tab_size
#     hash_key = (h1 + i) % tab_size
#     return hash_key

# def h(key, i, tab_size):
#     h1 = key % tab_size
#     h2 = 1 + (key % (tab_size - 2))
#     hash_key = (h1 + (i * h2)) % tab_size
#     return hash_key

def h(key, i, tab_size):
    h1 = key % (tab_size - 1)
    hash_key = (h1 + i + 3 * (i * i)) % tab_size 
    return hash_key

def naturalIntKey(arg):
    key = 0
    for chr in arg:
        key += ord(chr)*1000
    return key

def hashInsert(hash_table, key, tab_size):
    i = 0
    int_key = naturalIntKey(key[1])
    try:
        while(i != tab_size):
            hash_key = h(int_key, i, tab_size)
            if(hash_table[hash_key] == "NULL"):
                hash_table[hash_key] = key
                return i + 1
            else:
                i = i + 1
    except:
        print("Overload of hash table")

if __name__ == "__main__":
    main()