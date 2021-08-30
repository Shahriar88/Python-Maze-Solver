# -*- coding: utf-8 -*-
"""
Python Maze Solver

Algorithm:
    The coordinates which have only one way out, make them zero
"""
import numpy as np

def possib_ways(a,y,x):
    row,col=a.shape

    i=0
    if y-1<0:
        pass
    elif a[y-1][x]==1: # Up possible
        i+=1
        
    if y+2>row:  # y+1>row-1
        pass
    elif a[y+1][x]==1: # Down possible
        i+=1
        
    if x+2>col: # x+1>col-1
        pass
    elif a[y][x+1]==1: # Right possible
        i+=1
        
    if x-1<0:
        pass
    elif a[y][x-1]==1: # Left possible
        i+=1
    
    return i

def make_zero(a,row,col):
    zeros=0
    for y in range(row):
        for x in range(col):
            ways=possib_ways(a,y,x)
            if ways<=1:
                zeros+=1
                if np.array_equal(start,[y,x]): # Ensure not the start point
                    pass
                elif np.array_equal(end,[y,x]): # Ensure not the end point
                    pass
                else:
                    a[y,x]=0
            else:
                pass
    return zeros


array=[
   [1,0,1,0,0,0,0,1],
   [1,1,0,1,1,0,1,1],
   [1,0,0,1,0,0,1,0],
   [1,0,0,1,1,0,1,0],
   [1,0,0,0,1,0,1,0],
   [1,1,0,0,1,0,1,1],
   [0,1,1,1,1,1,0,1],
   [1,1,0,0,0,1,1,1]]

a=np.array(array)
start = np.array([7,0])
end = np.array([0,7])

# Run the function and u will have your result 
# It ensures that there is no coordinates having only one way or no way out  
loop=1
zerosR=0
row,col=a.shape
while(loop):
    zeros=make_zero(a,row,col)
    if zeros==zerosR:
        loop=0
    else:
        zerosR=zeros
print(a) # Result
