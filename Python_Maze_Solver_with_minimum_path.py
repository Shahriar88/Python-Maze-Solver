# -*- coding: utf-8 -*-
"""
Python Maze Solver with minimum path

Algorithm:
    1. The coordinates which have only one way out, make them zero
    2. Then use Dijkstra's Algorithm to find out the minimum path 
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

def DjsAf(nodes,index): # Modified Dijkstra's Algorithm for the Maze
    row=nodes[index,0]
    col=nodes[index,1]
        
    for i in range(1,len(nodes)):
        if nodes[i][0]==row:
            temp=nodes[i][1]+nodes[index][2]-col# Same Row, col diff
            temp1=nodes[i][1]-col
            if temp<nodes[i][2] and temp1==1:
                nodes[i][2]=temp
                nodes[i][3]=index # Source Index
                
    row=nodes[index,0]
    col=nodes[index,1]
        
    for i in range(1,len(nodes)):
        if nodes[i][1]==col:
            temp=nodes[i][0]+nodes[index][2]-row  # Same col, row diff 
            temp1=nodes[i][0]-row
            if temp<nodes[i][2] and temp1==1:
                nodes[i][2]=temp
                nodes[i][3]=index
    return nodes
            

def FindMin(nodes):
    nod=nodes.copy()
    paths=nod[:,2]
    for i in range(len(nod)):
        if nod[i][4]==0:
            paths[i]=10000
    val=np.amin(paths)
    index=np.where(paths==val)
    return index

def mark_node(a,row,col,start,end,way):
    nodes= np.array([[]])
    nodes=np.array([[start[0],start[1]]])

    for y in range(row):
        for x in range(col):
            if a[y,x]==1:
                ways=possib_ways(a,y,x)
            else:
                ways=-1
            if ways>=way:
                nodes=np.concatenate((nodes,[[y,x]]), axis=0)
    nodes=np.concatenate((nodes,[[end[0],end[1]]]), axis=0)
    #nodes=np.delete(nodes,0,axis=0)
    return nodes
#%%
#%%
#%%
matrix = [
	[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
	[0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
	[0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
	[1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
	[0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
	[1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
	[0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
	[0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
	[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
	[0, 0, 1, 0, 0, 1, 1, 0, 0, 1]]

src  = (0, 0)
dest = (5, 7)
a=np.array(matrix)
start = np.array(src)
end = np.array(dest)

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

#%%                
nodes=mark_node(a,row,col,start,end,2)            #>>>>>>>>>>>>>>>>>>>>>>>>>>


# Now use Dijkstra's Algorithm

DjsA=nodes.copy() # DjsA[0]=Row, DjsA[1]=Col
zz=len(nodes)
fill=np.array([[10000]*len(nodes)])
fill=np.transpose(fill)

nodes=np.concatenate((nodes,fill), axis=1) # Col 2 is the distance
nodes=np.concatenate((nodes,fill), axis=1) # Col 3 is the from row number
nodes=np.concatenate((nodes,fill), axis=1) # Col 4 is denoting that it was used before as reference
nodes[0][2]=0


loop=1
nonz=10000
while(loop):

    index=FindMin(nodes)
    index=index[0][0]
    nodes[index][4]=0
    nodes=DjsAf(nodes,index)
    if nonz!=np.count_nonzero(nodes[:,4]): # No change happening
        nonz=np.count_nonzero(nodes[:,4])
    else:
        loop=0
 #%% We have the answer in nodes, need to extract from there

index=len(nodes)-1
result=[[nodes[index][0],nodes[index][1]]]
result_no=[nodes[index][2]]

loop=1
while(loop):
    index=nodes[index][3]
    result.append([[nodes[index][0],nodes[index][1]]])
    result_no.append([nodes[index][2]])
    
    ll=np.array(result_no[-1])
    if int(ll==0):
        loop=0
result=result[::-1]
result_no=result_no[::-1]
print(result)
print(result_no)
