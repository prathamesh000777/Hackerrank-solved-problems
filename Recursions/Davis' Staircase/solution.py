'''
Initial thoughts:
We have two recursive function that act like a binary tree. In this approach we start with all the step with size 1.

First we replace the two steps with size 1 with one step with size 2 (poss_staircase_2(loc-1,count_1-2,count_2+1,count_3)) and reduce
the total number of steps by 1 (loc-1) because when you replace two step 1 with one step 2 the total number of steps decrease by 1. 
Simultaneously, we also replace three step 1 with one step 3 (poss_staircase_3(loc-2,count_1-3,count_2,count_3+1)) and reduce the total
number of steps by 2 (loc - 2).

Next we recursively do the previous step for all the step 1 replaced by step 2 as shown in the tree below
         start
           /\
          2  3
         /\   \ 
        2 3    3
       /\  \    \
      2 3   3    3

But the step 1 replaced by step 3 recursively call only the poss_startcase_3 which replace step 1 with step 3 only.
'''



# Complete the stepPerms function below.
def cal(loc,count_1,count_2,count_3):
    ''' calculates the permuatation of number of ways to arrange the steps with size 1,2 and 3
    loc = total number of steps
    count_1 = total number of steps with size = 1
    count_2 = total number of steps with size = 2 
    count_3 = total number of steps with size = 3
    '''
    x = int(math.factorial(loc)/(math.factorial(loc - (count_2+count_3))*math.factorial(count_2)*math.factorial(count_3)))
    return x

def poss_staircase_2(loc,count_1,count_2,count_3):
    ''' 
    Recursively call the fuction to replace the steps with size 1 with steps with size 2 and steps with size 3 seperately and return 
    the possible ways
    loc = total number of steps
    count_1 = total number of steps with size = 1
    count_2 = total number of steps with size = 2 
    count_3 = total number of steps with size = 3
    '''
    #base case: no more step 2 and 3 can be used. Hence we only calculate the number of ways possible
    if (count_1 < 2):
        return cal(loc,count_1,count_2,count_3)
    # no more step 3 can be used. Calculate the number of ways possible with current steps + with one more 2 sized step added
    elif (count_1 == 2):   
        return cal(loc,count_1,count_2,count_3) + poss_staircase_2(loc-1,count_1-2,count_2+1,count_3)
    # Calculate the number of ways possible with current steps + call the fuction to replace one step 1 with step 2 
                                                                     #  + call the fuction to replace one step 1 with step 3
    else:
        return cal(loc,count_1,count_2,count_3) + poss_staircase_2(loc-1,count_1-2,count_2+1,count_3) + 
                                                                       poss_staircase_3(loc-2,count_1-3,count_2,count_3+1)

def poss_staircase_3(loc,count_1,count_2,count_3):
    '''
    Recursively call the fuction to replace the steps with size 1 with size 3 and return the possible ways
    '''
    #base case: no more step 3 can be used. Hence we only calculate the number of ways possible
    if (count_1 < 3):   
        return cal(loc,count_1,count_2,count_3)
    # Calculate the number of ways possible with current steps + call the fuction to replace one step 1 with step 3
    else:
        return cal(loc,count_1,count_2,count_3) + poss_staircase_3(loc-2,count_1-3,count_2,count_3+1)   

def stepPerms(n):
    # we start with all the steps with size = 1 and hence steps of size 2 = 0 and size 3 = 0
    count_2 = 0       # total number of steps with size = 2
    count_3 = 0       # total number of steps with size = 3
    count_1 = int(n)  # total number of steps with size = 1
    loc = int(n)      # total number of steps 
    if count_1 == 1:
        return 1
    elif count_1 == 2:
        return 2
    else:
        return poss_staircase_2(loc,count_1,count_2,count_3)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
