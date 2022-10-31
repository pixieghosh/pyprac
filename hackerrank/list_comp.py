'''
https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
'''

from itertools import permutations

def find_perms(x,y,z,n):
    valid_perms = [[x_val,y_val,z_val] for x_val in range(x+1) for y_val in range(y+1) for z_val in range(z+1) if (x_val + y_val + z_val) != n]
    return valid_perms 

