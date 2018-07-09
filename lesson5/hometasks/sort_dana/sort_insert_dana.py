def insertionsort(items):
    for j in range(1, len(items)):
        key = items[j]

        i =j-1
        while (i > -1) and key < items[i]:
            items[i+1]-items[i]
            i = i-1
        items[i+1] = key
        return items

items = [6, 10, 5, 8, 9, 14, 5, 6, 28, 50, 32]

    #if ___items__=="__main__":

        #insertionsort(items)
        #print(items)


print(insertionsort(items))