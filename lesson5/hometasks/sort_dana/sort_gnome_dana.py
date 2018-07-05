from random import randrange


def gnomesort(items):
    i = 0
    while i < len(items):
        if i == 0 or items[i-1] <= items[i]:
            i += 1
        else:
            items[i], items[i-1] = items[i-1], items[i]
            i -= 1

items = [6, 10, 5, 8, 9, 14, 5, 6, 28, 50, 32]

print(gnomesort(items))

#if __name__ == "__main__":
    #nums = [randrange(20) for x in range(10)]
    #print "Numbers", nums
   # gnomesort(nums)
    #print "Sorted numbers", nums