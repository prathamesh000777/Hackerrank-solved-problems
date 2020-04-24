


def larrysArray(A,n):
    pos = {}
    index = {}
    for ind,val in enumerate(A):
        pos[val] = ind
        index[ind] = val
    i=0
    while i < (n-3):
        if pos[i+1] != i:
            now = pos[i+1]
            if (now - i)%2 == 0:
                for j in range(now - i):
                    index[now-j] = index[now-j-1]
                    pos[index[now-j]] = now - j
                index[i] = i+1
                pos[index[i]] = i
            else:
                if (now - i) == 1:
                    index[i+1] = index[i+2]
                    pos[index[i+1]] = i+1
                else:
                    for j in range(now - i - 2):
                        index[now-j] = index[now-j-1]
                        pos[index[now-j]] = now - j
                index[i+2] = index[i]
                pos[index[i+2]] = i + 2
                index[i] = i + 1
                pos[index[i]] = i
        i += 1
    diff = n - 3
    poss = {'123','231','312'}
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
