# Quick Sort
# Big O ----> O(nlogn) average case, O(n**2) worst case

def quick_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0] # You can choose pivot randomly(It helps the code to run faster)
        
        low = [i for i in lst[1:] if i <= pivot]
        high = [j for j in lst[1:] if j > pivot]

        return quick_sort(low) + [pivot] + quick_sort(high)
    
print(quick_sort([1, 1, 1, 1]))