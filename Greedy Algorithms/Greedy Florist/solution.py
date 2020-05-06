'''
Initial thoughts:
We first sort the given list of prices of flowers.

Consider a case where n = 10, and c = [1,2,3,4] and k = 4. Then first we consider flower [1,2,3,4] for orignal price. Next we have to
buy 4 more that is [1,2,3,4] at twice the price. Next we have to buy 2 more, for these we have to consider the lowest priced flower 
that is [1,2] for thrice the price. 

Now same logic we apply by repeating the array c by tot_loop (how many time all the flowers can be considered). For example in the
previous example we make c as [1,2,3,4,1,2,3,4]. Now the remaining two lowest priced flowers are added at the front of this array as,
[1,2,1,2,3,4,1,2,3,4]. Once we have this array, we start with last k elements, sum them and then multiply them with the current purchase
'p'.
'''

# Complete the getMinimumCost function below.
def getMinimumCost(k, c, n):
    c.sort()
    l = len(c)
    tot_loop = n//l                          # total number of complete loops
    last_elements = n%l                      # number of last remaining flowers
    c = c[:last_elements] + c*tot_loop       # explained in the explanation above
    p = 1                                    #count of purchases
    i = 1
    ans = 0
    while (l - (i-1)*k >= 0):
        ans += sum(c[max(l-i*k,0):l-(i-1)*k])*p  
        i += 1
        p += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c,n)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
