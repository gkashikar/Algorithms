# LINEAR SEARCH USING WHILE loop
 
lst = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
 
def linear_search_whileloop(lst,x):
    i = 0
    flag = False
      
    while i < len(lst):
        if lst[i] == x:
            flag = True
            break
        i = i + 1
     
    if flag == 1:
        print('{} was found at index {}.'.format(x, i))
    else:
        print('{} was not found.'.format(x))
 
linear_search_whileloop(lst,170)
