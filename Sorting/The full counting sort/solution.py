'''
Time complexity: n

A straight forward approach but i havent used counting sort but a dictionary to save the string as ecountered in the loop with key as 
the integer associated with it. This was the sorting part is done on the go.
'''


# Complete the countSort function below.
def countSort(arr,n):
    coll = dict()      # key is x[i] and value is list of all s[i] which have x[i]
    count = 0          # will be used to replace first half string with '-'
    for [i,j] in arr:
        if count < n/2:
            coll.setdefault(int(i),[]).append('-') # first half s[i] saved as '-'
            count += 1
        else:
            coll.setdefault(int(i),[]).append(j)   # next half s[i] as original string
    ans = []
    ele = list(sorted(list(coll.keys())))    # get all x[i] and sort
    for i in ele:
        temp = coll[i]
        ans.extend(temp)
    print(' '.join(ans))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr,n)
