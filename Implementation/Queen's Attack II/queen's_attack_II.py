'''
Approach to the problem.

There are 4 ways queen can move i.e. horizontal, vertical, forward line(line with slope 1) and backward line(line with slope -1). 

The first step is to check if the obstacle lies on which of the 4 possible way. The obstacle can lie only on one of the 4 way as the
intersection of these ways is the position of the queen itself and as per the problem statement the obstacle can never be on the 
queens position.

Next step is to check if the obstacle is to the right or left of the queen, followed by closest element of right and left. And finally 
calculate the possible ways to move by calculating the positions between queen and closest elements to right and left.

If you have understood the approach till now you can skip the next part of the explanation where I explain the steps in detail.

Obstacle lies on the horizontal line if obstalce's row (first element of obstacle) and queens row (r_q) are the same.
Obstacle lies on the vertical line if obstalce's column (second element of obstacle) and queens column (c_q) are the same.

For inclined lines we check if the line satisfies the condition y=mx+c where, y is the row, x is the column, and c is the y-intercept

Obstacle lies on the forward line (line with slope 1) if it satisfy the equation (row - column - intercept == 0)
Obstacle lies on the backward line (line with slope 1) if it satisfy the equation (row + column - intercept == 0)

For checking if the obstacle lies on the right or left of queen for horizontal,forward and backward line we only check the columns of
the obstacle. For the vertical line we have to use row of obstacle for comparing.

For example, suppose on a horizontal line queen is at 4th of the 8 column. Then for all the obstacle on the left (i.e. obstacles 
with column 1,2,3) the closest one to the queen is with column=3. Hence we have used variable max_left to store this location. Similarly
for right the closest one to the queen will be min_right (you can guess why :) ).

For horizontal and vertical line we initiate the max_left and min_right just outside the chessboard i.e. 0 and n+1 respectively.

For forward and backward line initiating the max_left and min_right is bit tricky.
For forward line the max_left (c_q - min((r_q - 1),(c_q - 1)) - 1), where the term (min((r_q - 1),(c_q - 1))) gives the available blocks
to the left of the queen on forward line. The terms checks which is minimum rows or columns to the left; as we can only move the
minimum step only or we will be out of the chess board.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#Helper function
def nearest_pos(i,queens_loc,max_left,min_right):
    #checks if the element is to the left(i < queens_loc) and if it is the closest to the left of queen by checking then update max_left
    if (i < queens_loc) and (i > max_left): 
        max_left = i
    #checks if the element is to the right(i > queens_loc) and if it is the closest to the right of queen then update min_right
    elif (i > queens_loc) and (i < min_right):  
        min_right = i
    return max_left,min_right

#helper function
def pos_count(max_left,min_right,queens_loc):
    #calculate the blocks available to move for the queen.
    return (queens_loc - max_left - 1) + (min_right - queens_loc - 1)

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacle):
    # Calculate the y-intercept(c = y - mx)
    fl_c = r_q - c_q      #forwardline y-intercept
    bl_c = r_q + c_q      #backwardline y-intercept

    #obstacle position initiation
    hl_max_left, hl_min_right = 0, n + 1    #explained on line 30
    vl_max_bot, vl_min_top = 0, n + 1       #vertical line

    #calculate the leftmost and rightmost possible column of the inclined lines
    fl_max_left =  c_q - min((r_q - 1),(c_q - 1)) - 1   #this step is explained on line 32.
    fl_min_right = c_q + min((n - r_q),(n - c_q)) + 1   #forwardline
    bl_max_left = c_q - min((n - r_q),(c_q - 1)) - 1    #backwardline
    bl_min_right = c_q +  min((r_q - 1),(n - c_q)) + 1


    for [r_o,c_o] in obstacle:
        #for horizontalline we check if obstacle lies on the same row as queen
        if r_o == r_q: 
            hl_max_left, hl_min_right = nearest_pos(c_o, c_q, hl_max_left, hl_min_right)
        #for verticalline we check if obstacle lies on the same column as queen
        elif c_o == c_q: 
            vl_max_bot, vl_min_top = nearest_pos(r_o, r_q, vl_max_bot, vl_min_top)
        #for forwardline we check if obstacle lies on the line by equation(y-x-c==0) since m = 1
        elif (r_o - c_o - fl_c) == 0: 
            fl_max_left, fl_min_right = nearest_pos(c_o, c_q, fl_max_left, fl_min_right)
        #for backward we check if obstacle lies on the line by equation(y+x-c==0) since m = -1
        elif (r_o + c_o - bl_c) == 0:
            bl_max_left, bl_min_right = nearest_pos(c_o, c_q, bl_max_left, bl_min_right)
    
    hl_count = pos_count(hl_max_left,hl_min_right, c_q)
    vl_count = pos_count(vl_max_bot,vl_min_top, r_q)
    fl_count = pos_count(fl_max_left,fl_min_right, c_q)
    bl_count = pos_count(bl_max_left,bl_min_right, c_q)
    
    count = hl_count + vl_count + fl_count + bl_count
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
