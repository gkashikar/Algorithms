#Merge Sort
'''Merge sort has a divide and conquer approach to sorting, 
and is a recursive sorting algorithm, different from 
the ones above which are iterative. To understand merge sort, 
we must first understand recursion.
Recursive functions are functions that call themselves, 
but have a base case to work towards to prevent infinite loops.'''

#Merge sort first divides the array into equal halves and #then combines them in a sorted manner.

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

# Find the middle point and divide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]
   
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves
def merge(left_half,right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

unsorted_list = [64, 34, 25, 12, 22, 11, 90]

print(merge_sort(unsorted_list))

#When the above code is executed, it produces the following result
#[11, 12, 22, 25, 34, 64, 90]
