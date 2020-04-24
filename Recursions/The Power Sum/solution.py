'''
Solution with recursion and backtracking. The logic is straight forward. Example for X=100, N=2, all the exponents are
[1,4,9,16,25,36,49,64,81,100].

We start with first element i.e.,1
    Next we add second element i.e 1+4
        Next we add third element i.e 1+4+9
            Continue till the sum is less than X else we stop
    Next we add third element i.e. 1+9
        Next we add fourth element i.e. 1+9+16
            Continue till the sum is less than X else we stop
 
This way we backtrack whenever we encounter the sum greater than X or increment the count if sum is equal to X.
'''

def sumer(j,tot,count):
    if (j < n) and (tot < X):
        for k in range(j,n):
            new_tot = tot + elements[k]
            if new_tot == X:
                count[0] += 1
                return
            elif new_tot < X:
                sumer(k+1,new_tot,count)
            else:
                return 
    else:
        return


# Complete the powerSum function below.
def powerSum(X, N,count):
    for i in range(n-1):
        sumer(i+1,elements[i],count)
    return count[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())
    elements = []              #to hold the exponents
    exp = 1
    num = 2
    while exp <= X:
        elements.append(exp)
        exp = num**N
        num += 1
    n = num - 2
    if elements[-1] == X:
        count = [1]               # to hold the count of power sums
    else:
        count = [0]
    result = powerSum(X, N, count)

    fptr.write(str(result) + '\n')

    fptr.close()
