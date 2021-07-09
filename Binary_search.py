#Script to utilize Binary Search Algorithm to search a number in a random number list and providing count of tries it took.

import random
random.seed("test")

numbers = []
for _ in range(100):
    numbers.append(random.randint(0,1000))

numbers.sort()

counter = 0
def binary_search(numbers_list, number,left, right):
    global counter
    counter += 1
    #basic case 
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if number == numbers_list[mid]:
        return mid
    elif number < numbers_list[mid]:
        return binary_search(numbers_list, number, left, mid-1)
    else:
        return binary_search(numbers_list, number, mid+1, right)
    
print(numbers)
print(binary_search(numbers, 240,0, len(numbers)-1))
print(counter)
