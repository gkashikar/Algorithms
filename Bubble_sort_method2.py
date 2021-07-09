#Method 2 - Bubble Sort

def bubble_sort(list2):
    # Traverse (travel across) through every element on the list
    for i in range(0, len(list2) - 1):
        # Compare each item in list 1 by 1. Comparison in each iteration 
        # will shorten as the last elements become sorted
        for j in range(0, len(list2) - 1 - i):
            # traverse the list from 0 to n-i-1 
            # if the element found is greater than the next element, swap
            if list2[j] > list2[j + 1]:
                list2[j], list2[j + 1] = list2[j + 1], list2[j]
 
    return list2

list2 = [2, 3, 7, 1, 9, 5]
bubble_sort(list2)
print(list2)

#When the above code is executed, it produces the following result −
#[1, 2, 3, 5, 7, 9]
