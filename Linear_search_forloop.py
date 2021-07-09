# LINEAR SEARCH USING FOR loop

lst = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]

def linear_search_forloop(lst,x):
    i = 0
    flag = False
     
    for i in range(len(lst)):
        if lst[i] == x:
            flag = True
            break
      
    if flag == 1:
        print('{} was found at index {}.'.format(x, i))
    else:
        print('{} was not found.'.format(x))

linear_search_forloop(lst,170)
