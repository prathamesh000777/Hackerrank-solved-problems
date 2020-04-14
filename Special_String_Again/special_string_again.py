'''
Some initial thoughts.
There are three cases to check. One, if it is case were all the characters are equal. Two, if it a special palindrome with second last character being equal to current character. Third and the last being the subsequent characters are not equal.

Next, I have explained each step in detail.

In first case if the current character is equal to the previous character we go on counting all the same characters in the recursive call count_same() and keep the track of the count in 'length' variable. At last when a different character is formed we calculate all the substring formed by this i.e. (length*(length + 1)/2) and also return the position of the last character. For example, string 'aaaa' which is of length 4 will give 4*(4+1)/2 i.e. 10 substrings also explained in the problem statement.

Second case is when it is a special palindrome that is second last character being equal to the current character. We then use a recursive call to count the length of it and return length. For example, string 'oopoo' can form only two special palindrome i.e. 'opo' and 'oopoo'.

In third case we just increment the count as it is neither same nor special palindrome.
'''

# Complete the substrCount function below.
def count_centered(s,i,j,length,n):
''' The parameter are s - string, i-current index, j - index of the character before the center element, length - to keep track of count, n - size of the string.'''
    if (i < n-1) and (j > 0) and (s[i+1] == s[j-1]) and (s[i+1] == s[i]):  #index i and j shouldnot be the last character to avoid error
        return count_centered(s,i+1,j-1,length+1,n)
    else:
        return length

def count_same(s,i,length,n):
    '''Here we count the length of substring formed by same characters'''
    if (i < n-1) and (s[i+1] == s[i]):
        return count_same(s,i+1,length+1,n)
    else:
        return (length*(length + 1)/2),i

def substrCount(n, s):
    count = 1    # as we start from index 1 and count set the count to 1 (i.e the first element)
    i = 1
    while i < n:
        if s[i] == s[i-1]:                       # Case 1: all the characters are same
            temp,i = count_same(s,i,2,n)   
            count += temp - 1                    # -1 because we have already counted the first element before
        elif (i > 1) and s[i] == s[i-2]:         # Case 2: if it is a special palindrome
            count += count_centered(s,i,i-2,1,n) + 1   # +1 because we have moved to the next character
        else:
            count += 1
        i+= 1
            
    return int(count)
