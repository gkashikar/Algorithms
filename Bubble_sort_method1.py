# Method 1 - Bubble Sort

def bubblesort(lst):
    # Swap the elements to arrange in order
    for iter_num in range(len(lst)-1,0,-1):
        for idx in range(iter_num):
            if lst[idx]>lst[idx+1]:
                temp = lst[idx]
                lst[idx] = lst[idx+1]
                lst[idx+1] = temp

lst = [19,2,31,45,6,11,121,27]
bubblesort(lst)
print(lst)

#When the above code is executed, it produces the following result −
#[2, 6, 11, 19, 27, 31, 45, 121]
