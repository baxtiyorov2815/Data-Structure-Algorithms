# Bubble Sort
def bubbleSort(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst

print(bubbleSort([10, 2, 3, 9, 7, 5]))