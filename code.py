import copy
from queue import Queue
import heapq

#R_C (row,col) tuple
#stack (strings(124356870)) list
#G (goal string) string
#visited (string(124356870)) set

# L U R D
# 0  1  2
# 3  4  5
# 6  7  8


### DFS
def INITIAL_LOC(STRT):

    count=int(0)
    for i in STRT:
        if i=='0':
            break
        else:
            count+=1

    row=count//3
    col=count%3

    return (row,col)

def DFS_HELP(stack,G,visited):
    while stack:
        node=stack.pop()
        if node==G:
            print("Path found to the goal (DFS)")
            return
        visited.add(node)
        R_C=INITIAL_LOC(node)
        if(R_C[0]==0):
            if(R_C[1]==0):
                node1=node[1]+node[0]+node[2:]
                node2=node[3]+node[1:3]+node[0]+node[4:]    
                if node2 not in visited:
                    stack.append(node2)
                if node1 not in visited:
                    stack.append(node1)
                    
            if(R_C[1]==1):
                node1=node[1]+node[0]+node[2:]
                node2=node[0:1]+node[2]+node[1]+node[3:]
                node3=node[0:1]+node[4]+node[2:4]+node[1]+node[5:]
                if node3 not in visited:
                    stack.append(node3)
                if node2 not in visited:
                    stack.append(node2)
                if node1 not in visited:
                    stack.append(node1) 
                                
            if(R_C[1]==2):
                node1=node[0:1]+node[2]+node[1]+node[3:]
                node2=node[0:2]+node[5]+node[3:5]+node[2]+node[6:]    
                if(not node2 in visited):
                    stack.append(node2)
                if(not node1 in visited):
                    stack.append(node1)
                
        elif(R_C[0]==1):
            if(R_C[1]==0):
                node1=node[3]+node[1:3]+node[0]+node[4:]
                node2=node[0:3]+node[4]+node[3]+node[5:]
                node3=node[0:3]+node[6]+node[4:6]+node[3]+node[7:]
                if(not node3 in visited):
                    stack.append(node3)
                if(not node2 in visited):
                    stack.append(node2)
                if(not node1 in visited):
                    stack.append(node1)
                
            if(R_C[1]==1):
                node1=node[0:3]+node[4]+node[3]+node[5:]
                node2=node[0]+node[4]+node[2:4]+node[1]+node[5:]
                node3=node[0:4]+node[5]+node[4]+node[6:]
                node4=node[0:4]+node[7]+node[5:7]+node[4]+node[8]
                if(not node4 in visited):
                    stack.append(node4)
                if(not node3 in visited):
                    stack.append(node3)
                if(not node2 in visited):
                    stack.append(node2)
                if(not node1 in visited):
                    stack.append(node1)
                
            if(R_C[1]==2):
                node1=node[0:4]+node[5]+node[4]+node[6:]
                node2=node[0:2]+node[5]+node[3:5]+node[2]+node[6:]
                node3=node[0:5]+node[8]+node[6:8]+node[5]
                if(not node3 in visited):
                    stack.append(node3)
                if(not node2 in visited):
                    stack.append(node2)
                if(not node1 in visited):
                    stack.append(node1)
                
        elif R_C[0] == 2:
            if R_C[1] == 0:
                node1 = node[0:3]+ node[6] + node[4:6] + node[3] + node[7:]
                node2 = node[0:6] + node[7] + node[6] + node[8]
                if node2 not in visited:
                    stack.append(node2)
                if node1 not in visited:
                    stack.append(node1)
                
            if R_C[1] == 1:
                node1 = node[0:6] + node[7] + node[6] + node[8]
                node2 = node[0:4] + node[7] + node[5:7] + node[4] + node[8]
                node3 = node[0:7] + node[8] + node[7]
                if node3 not in visited:
                    stack.append(node3)
                if node2 not in visited:
                    stack.append(node2)
                if node1 not in visited:
                    stack.append(node1)
                
            if R_C[1] == 2:
                node1 = node[0:7] + node[8] + node[7]
                node2 = node[0:5] + node[8] + node[6:8] + node [5]
                if node2 not in visited:
                    stack.append(node2)
                if node1 not in visited:
                    stack.append(node1)
                
def DFS(S_G):
    visited=set()
    stack=list()
    stack.append(S_G[0])
    DFS_HELP(stack,S_G[1],visited)


### BFS
def BFS_HELP(queue,G,visited):
    while queue:
        node=queue.get()
        if node==G:
            print("Path found to the goal (BFS)")
            return
        visited.add(node)
        R_C=INITIAL_LOC(node)
        if(R_C[0]==0):
            if(R_C[1]==0):
                node1=node[1]+node[0]+node[2:]
                node2=node[3]+node[1:3]+node[0]+node[4:]    
                if node2 not in visited:
                    queue.put(node2)
                if node1 not in visited:
                    queue.put(node1)
                    
            if(R_C[1]==1):
                node1=node[1]+node[0]+node[2:]
                node2=node[0:1]+node[2]+node[1]+node[3:]
                node3=node[0:1]+node[4]+node[2:4]+node[1]+node[5:]
                if node3 not in visited:
                    queue.put(node3)
                if node2 not in visited:
                    queue.put(node2)
                if node1 not in visited:
                    queue.put(node1) 
                                
            if(R_C[1]==2):
                node1=node[0:1]+node[2]+node[1]+node[3:]
                node2=node[0:2]+node[5]+node[3:5]+node[2]+node[6:]    
                if(not node2 in visited):
                    queue.put(node2)
                if(not node1 in visited):
                    queue.put(node1)
                
        elif(R_C[0]==1):
            if(R_C[1]==0):
                node1=node[3]+node[1:3]+node[0]+node[4:]
                node2=node[0:3]+node[4]+node[3]+node[5:]
                node3=node[0:3]+node[6]+node[4:6]+node[3]+node[7:]
                if(not node3 in visited):
                    queue.put(node3)
                if(not node2 in visited):
                    queue.put(node2)
                if(not node1 in visited):
                    queue.put(node1)
                
            if(R_C[1]==1):
                node1=node[0:3]+node[4]+node[3]+node[5:]
                node2=node[0]+node[4]+node[2:4]+node[1]+node[5:]
                node3=node[0:4]+node[5]+node[4]+node[6:]
                node4=node[0:4]+node[7]+node[5:7]+node[4]+node[8]
                if(not node4 in visited):
                    queue.put(node4)
                if(not node3 in visited):
                    queue.put(node3)
                if(not node2 in visited):
                    queue.put(node2)
                if(not node1 in visited):
                    queue.put(node1)
                
            if(R_C[1]==2):
                node1=node[0:4]+node[5]+node[4]+node[6:]
                node2=node[0:2]+node[5]+node[3:5]+node[2]+node[6:]
                node3=node[0:5]+node[8]+node[6:8]+node[5]
                if(not node3 in visited):
                    queue.put(node3)
                if(not node2 in visited):
                    queue.put(node2)
                if(not node1 in visited):
                    queue.put(node1)
                
        elif R_C[0] == 2:
            if R_C[1] == 0:
                node1 = node[0:3]+ node[6] + node[4:6] + node[3] + node[7:]
                node2 = node[0:6] + node[7] + node[6] + node[8]
                if node2 not in visited:
                    queue.put(node2)
                if node1 not in visited:
                    queue.put(node1)
                
            if R_C[1] == 1:
                node1 = node[0:6] + node[7] + node[6] + node[8]
                node2 = node[0:4] + node[7] + node[5:7] + node[4] + node[8]
                node3 = node[0:7] + node[8] + node[7]
                if node3 not in visited:
                    queue.put(node3)
                if node2 not in visited:
                    queue.put(node2)
                if node1 not in visited:
                    queue.put(node1)
                
            if R_C[1] == 2:
                node1 = node[0:7] + node[8] + node[7]
                node2 = node[0:5] + node[8] + node[6:8] + node [5]
                if node2 not in visited:
                    queue.put(node2)
                if node1 not in visited:
                    queue.put(node1)

def BFS(S_G):
    visited=set()
    queue=Queue()
    queue.put(S_G[0])
    BFS_HELP(queue,S_G[1],visited)
    
def INPUT():
    STRT=input("Enter the initial grid config: ")
    GOAL=input("Enter the final grid config: ")
    return [STRT,GOAL]


### UCS
def UCS_HELP(pq,G,visited):
    while pq:
        dist,node=heapq.heappop(pq)
        if node==G:
            print("Path found to the goal (UCS) ",dist)
            return
        visited.add(node)
        R_C=INITIAL_LOC(node)
        if(R_C[0]==0):
            if(R_C[1]==0):
                node1=node[1]+node[0]+node[2:]
                node2=node[3]+node[1:3]+node[0]+node[4:]    
                if node2 not in visited:
                    heapq.heappush(pq,(dist+1,node2))
                if node1 not in visited:
                    heapq.heappush(pq,(dist+1,node1))
                    
            if(R_C[1]==1):
                node1=node[1]+node[0]+node[2:]
                node2=node[0:1]+node[2]+node[1]+node[3:]
                node3=node[0:1]+node[4]+node[2:4]+node[1]+node[5:]
                if node3 not in visited:
                    heapq.heappush(pq,(dist+1,node3))
                if node2 not in visited:
                    heapq.heappush(pq,(dist+1,node2))
                if node1 not in visited:
                    heapq.heappush(pq,(dist+1,node1)) 
                                
            if(R_C[1]==2):
                node1=node[0:1]+node[2]+node[1]+node[3:]
                node2=node[0:2]+node[5]+node[3:5]+node[2]+node[6:]    
                if(not node2 in visited):
                    heapq.heappush(pq,(dist+1,node2))
                if(not node1 in visited):
                    heapq.heappush(pq,(dist+1,node1))
                
        elif(R_C[0]==1):
            if(R_C[1]==0):
                node1=node[3]+node[1:3]+node[0]+node[4:]
                node2=node[0:3]+node[4]+node[3]+node[5:]
                node3=node[0:3]+node[6]+node[4:6]+node[3]+node[7:]
                if(not node3 in visited):
                    heapq.heappush(pq,(dist+1,node3))
                if(not node2 in visited):
                    heapq.heappush(pq,(dist+1,node2))
                if(not node1 in visited):
                    heapq.heappush(pq,(dist+1,node1))
                
            if(R_C[1]==1):
                node1=node[0:3]+node[4]+node[3]+node[5:]
                node2=node[0]+node[4]+node[2:4]+node[1]+node[5:]
                node3=node[0:4]+node[5]+node[4]+node[6:]
                node4=node[0:4]+node[7]+node[5:7]+node[4]+node[8]
                if(not node4 in visited):
                    heapq.heappush(pq,(dist+1,node4))
                if(not node3 in visited):
                    heapq.heappush(pq,(dist+1,node3))
                if(not node2 in visited):
                    heapq.heappush(pq,(dist+1,node2))
                if(not node1 in visited):
                    heapq.heappush(pq,(dist+1,node1))
                
            if(R_C[1]==2):
                node1=node[0:4]+node[5]+node[4]+node[6:]
                node2=node[0:2]+node[5]+node[3:5]+node[2]+node[6:]
                node3=node[0:5]+node[8]+node[6:8]+node[5]
                if(not node3 in visited):
                    heapq.heappush(pq,(dist+1,node3))
                if(not node2 in visited):
                    heapq.heappush(pq,(dist+1,node2))
                if(not node1 in visited):
                    heapq.heappush(pq,(dist+1,node1))
                
        elif R_C[0] == 2:
            if R_C[1] == 0:
                node1 = node[0:3]+ node[6] + node[4:6] + node[3] + node[7:]
                node2 = node[0:6] + node[7] + node[6] + node[8]
                if node2 not in visited:
                    heapq.heappush(pq,(dist+1,node2))
                if node1 not in visited:
                    heapq.heappush(pq,(dist+1,node1))
                
            if R_C[1] == 1:
                node1 = node[0:6] + node[7] + node[6] + node[8]
                node2 = node[0:4] + node[7] + node[5:7] + node[4] + node[8]
                node3 = node[0:7] + node[8] + node[7]
                if node3 not in visited:
                    heapq.heappush(pq,(dist+1,node3))
                if node2 not in visited:
                    heapq.heappush(pq,(dist+1,node2))
                if node1 not in visited:
                    heapq.heappush(pq,(dist+1,node1))
                
            if R_C[1] == 2:
                node1 = node[0:7] + node[8] + node[7]
                node2 = node[0:5] + node[8] + node[6:8] + node [5]
                if node2 not in visited:
                    heapq.heappush(pq,(dist+1,node2))
                if node1 not in visited:
                    heapq.heappush(pq,(dist+1,node1))

def UCS(S_G):
    visited=set()
    pq=[]
    heapq.heappush(pq,(0,S_G[0]))
    UCS_HELP(pq,S_G[1],visited)


S_G=list(INPUT())
DFS(S_G)
BFS(S_G)
UCS(S_G)



