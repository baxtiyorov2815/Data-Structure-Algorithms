# Selection Sort
def findSmallest(lst):
    smallest = lst[0]
    smallestIndex = 0
    for i in range(1, len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
            smallestIndex = i
    
    return smallestIndex

def SelectionSort(lst):
    sortedList = []
    while lst:
        smallestIndex = findSmallest(lst)
        smallest = lst.pop(smallestIndex)
        sortedList.append(smallest)

    return sortedList

print(SelectionSort([10, 2, 3, 9, 7, 5]))