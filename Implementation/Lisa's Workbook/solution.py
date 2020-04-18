def workbook(n, k, arr):
    page = count = 0     #to store the current page and count of special problem
    for i in range(0,n):
        no_prob = arr[i]   #stores the count of problems
        start_prob = 1     #stores starting problem of every page
        while no_prob > 0: #loop till there are no problem to assign to the chapter
            page += 1
            end_prob = start_prob + min(no_prob,k) - 1  #calculate page's end problem
            if (start_prob) <= page <= end_prob:     #check if there are special problem
                count += 1                           #increment the count
            start_prob = end_prob + 1             #this is the starting problem number for next page
            no_prob -= min(no_prob,k)       #decrement the count of problems assigned to this page
    return count
