'''
Initial thoughts:
First we map the input array using two dictionaries, one to hold index as key and other to hold values of array as key. After mapping we
need to sort the array as per the explanation. There are two categories,
1 - when the element is even steps away from its position
2 - when the element is odd steps away from its position

Case 1:
The easy case as we just need to shift all the elements in between to the next index. For example if the array is [5,4,2,3,1], now to put 1 back to its position from index 4 to index 0, we have to do 4 rotation. The resulting array would be [1,5,4,2,3], as you must have noticed the elements in the original array from index 0 to index 4 are just shifted to next index. Finally index 0 of the new array is given the value 1.

Case 2.1:
In this case we have to be careful while shifting the elements near the desired location. For example if the array is [5,4,2,3,6,1], now
to get 1 back to its position from index 5 to index 0 the resulting array after sorting would be [1,4,5,2,3,6]. Notice that the element 
from index 2 to index 4 are just shifted to next index as we did in case 1. The elements at index 2 of rotated array is replaced by 
index 0 of original array and index 0 of rotated array is given the value 1.
Case 2.2
This is the special case of 2, when the element is just 1 steps away from its position. For example [3,1,2], the result after getting 1 to its position would be [1,2,3]. Index 1 of rotated array gets element at index 2 of original array, index 2 of rotated array gets the 
element at index 0 of original array, and finally the index 0 of rotated array is set to value 1.

In both the cases the position of the elements in the array at each step is changed and the index is updated. The last three elements are then check if they can be rotated to get the sorted array.
'''


def larrysArray(A,n):
    values = {}            # dictionary to store array's value as key
    index = {}          # dictionary to store arrays index as key
    for ind,val in enumerate(A):         # mapping of the array A
        values[val] = ind
        index[ind] = val
    i=0
    while i < (n-3):
        if values[i+1] != i:        # starting from first element of array check if the current element is on the right position or not
            now = values[i+1]       # current position of the element(i+1) that suppose to be at i
            if (now - i)%2 == 0:   #check if case 1
                for j in range(now - i):     #shift all the element in between to next index
                    index[now-j] = index[now-j-1]   # updating index of the element
                    values[index[now-j]] = now - j  # updating values according to new index
            else:                #case 2
                if (now - i) == 1: #case 2.2
                    index[i+1] = index[i+2]   # this step is explained in the explanation of case 2.2 above
                    values[index[i+1]] = i+1
                else:              #case 2.1
                    for j in range(now - i - 2):
                        index[now-j] = index[now-j-1]   # updating index of the element
                        values[index[now-j]] = now - j  # updating values according to new index
                index[i+2] = index[i]         # this step is explained in explanation of case 2.1
                values[index[i+2]] = i + 2
            index[i] = i + 1                  # the final step of placing the misplaced element on its position
            values[index[i]] = i
        i += 1
    diff = n - 3   
    poss = {'123','231','312'}   # these are the possible combination of index that can be rotated to get the sorted array.
    first = index[i] - diff
    second = index[i+1] - diff
    third = index[i+2] - diff
    com = str(first) + str(second) + str(third)
    if com in poss:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A,n)

        fptr.write(result + '\n')

    fptr.close()
