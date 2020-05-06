'''
Time complexity: n
First sort the array. Start with index 0 and (0+k-1) i.e the fisrt and last elements of the subarray with k elements (our subarray).
We then check the difference of this two element as they are the max and min of this subarray. Continue till index (n-k-1).
'''

def maxMin(k, arr, n):
    arr.sort()
    i = 0
    ans = arr[k-1] - arr[0]
    for i in range(n - k + 1):
        temp = arr[i + k - 1] - arr[i]
        if temp < ans:
            ans = temp
    return ans
