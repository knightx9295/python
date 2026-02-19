import copy
from collections import deque
import heapq
import time

#R_C (row,col) tuple
#stack (strings(124356870)) list
#G (goal string, no of nodes visited) string
#visited (string(124356870)) set

# L U R D (priority)
# 0  1  2
# 3  4  5
# 6  7  8

# def display_path(tracker):
#     print("---------------------------------")
#     print("Path is: ")
#     path_cost=0
#     while tracker:
#         print(tracker.pop())
#         path_cost+=1
#     print("---------------------------------")
#     print("Path cost is: ",path_cost)
#     print("---------------------------------")

# def pathtracker(node_stack):
#     tracker=list()
#     parent,child=node_stack.pop()
#     tracker.append(child)    
#     while node_stack:
#         p,c=node_stack.pop()
#         if parent==c:
#             tracker.append(parent)
#             parent=p
#     display_path(tracker)

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
def INPUT():
    STRT=input("Enter the initial grid config: ")
    GOAL=input("Enter the final grid config: ")
    return [STRT,GOAL]

### DFS
def display_path(path):
    print("---------------------------------")
    print("Path is: ")
    for step in path:
        print(step)
    print("---------------------------------")
    print("Path cost is: ", len(path) - 1)
    print("---------------------------------")

def DFS_HELP(stack,G,visited):
    while stack:
        path=stack.pop()
        node=path[-1]
        if node==G[0]:
            print("Path found to the goal (DFS)")
            print("No of nodes visited (DFS):",G[1])
            display_path(path)
            return
        if node in visited:
            continue
        visited.add(node)
        steps=G[1]+1
        G[1]=steps
        R_C=INITIAL_LOC(node)
        if(R_C[0]==0):
            if(R_C[1]==0):
                node1=node[1]+node[0]+node[2:]
                node2=node[3]+node[1:3]+node[0]+node[4:]    
                if node2 not in visited:
                    stack.append(path+[node2])
                if node1 not in visited:
                    stack.append(path+[node1])
                    
            if(R_C[1]==1):
                node1=node[1]+node[0]+node[2:]
                node2=node[0:1]+node[2]+node[1]+node[3:]
                node3=node[0:1]+node[4]+node[2:4]+node[1]+node[5:]
                if node3 not in visited:
                    stack.append(path+[node3])
                if node2 not in visited:
                    stack.append(path+[node2])
                if node1 not in visited:
                    stack.append(path+[node1]) 
                                
            if(R_C[1]==2):
                node1=node[0:1]+node[2]+node[1]+node[3:]
                node2=node[0:2]+node[5]+node[3:5]+node[2]+node[6:]    
                if(not node2 in visited):
                    stack.append(path+[node2])
                if(not node1 in visited):
                    stack.append(path+[node1])
                
        elif(R_C[0]==1):
            if(R_C[1]==0):
                node1=node[3]+node[1:3]+node[0]+node[4:]
                node2=node[0:3]+node[4]+node[3]+node[5:]
                node3=node[0:3]+node[6]+node[4:6]+node[3]+node[7:]
                if(not node3 in visited):
                    stack.append(path+[node3])
                if(not node2 in visited):
                    stack.append(path+[node2])
                if(not node1 in visited):
                    stack.append(path+[node1])
                
            if(R_C[1]==1):
                node1=node[0:3]+node[4]+node[3]+node[5:]
                node2=node[0]+node[4]+node[2:4]+node[1]+node[5:]
                node3=node[0:4]+node[5]+node[4]+node[6:]
                node4=node[0:4]+node[7]+node[5:7]+node[4]+node[8]
                if(not node4 in visited):
                    stack.append(path+[node4])
                if(not node3 in visited):
                    stack.append(path+[node3])
                if(not node2 in visited):
                    stack.append(path+[node2])
                if(not node1 in visited):
                    stack.append(path+[node1])
                
            if(R_C[1]==2):
                node1=node[0:4]+node[5]+node[4]+node[6:]
                node2=node[0:2]+node[5]+node[3:5]+node[2]+node[6:]
                node3=node[0:5]+node[8]+node[6:8]+node[5]
                if(not node3 in visited):
                    stack.append(path+[node3])
                if(not node2 in visited):
                    stack.append(path+[node2])
                if(not node1 in visited):
                    stack.append(path+[node1])
                
        elif R_C[0] == 2:
            if R_C[1] == 0:
                node1 = node[0:3]+ node[6] + node[4:6] + node[3] + node[7:]
                node2 = node[0:6] + node[7] + node[6] + node[8]
                if node2 not in visited:
                    stack.append(path+[node2])
                if node1 not in visited:
                    stack.append(path+[node1])
                
            if R_C[1] == 1:
                node1 = node[0:6] + node[7] + node[6] + node[8]
                node2 = node[0:4] + node[7] + node[5:7] + node[4] + node[8]
                node3 = node[0:7] + node[8] + node[7]
                if node3 not in visited:
                    stack.append(path+[node3])
                if node2 not in visited:
                    stack.append(path+[node2])
                if node1 not in visited:
                    stack.append(path+[node1])
                
            if R_C[1] == 2:
                node1 = node[0:7] + node[8] + node[7]
                node2 = node[0:5] + node[8] + node[6:8] + node [5]
                if node2 not in visited:
                    stack.append(path+[node2])
                if node1 not in visited:
                    stack.append(path+[node1])
         
def DFS(S_G):
    print("---------------------------------")
    print("DFS ALGO")
    print("---------------------------------")
    start=time.time()
    visited=set()
    stack=list()
    stack.append([S_G[0]])
    goal=[S_G[1],0]
    DFS_HELP(stack,goal,visited)
    end=time.time()
    t_time=end-start
    print(f"Time taken: {t_time:.4f} seconds")
    


### BFS
def BFS_HELP(queue,G,visited):
    node_stack=list()
    while queue:
        path=queue.popleft()
        node=path[-1]
        if node==G[0]:
            print("Path found to the goal (BFS)")
            print("No of nodes visited (BFS):",G[1])
            display_path(path)
            return node_stack
        if node in visited:
            continue
        visited.add(node)
        steps=G[1]+1
        G[1]=steps
        R_C=INITIAL_LOC(node)
        if(R_C[0]==0):
            if(R_C[1]==0):
                node1=node[1]+node[0]+node[2:]
                node2=node[3]+node[1:3]+node[0]+node[4:]    
                if node2 not in visited:
                    queue.append(path+[node2])
                if node1 not in visited:
                    queue.append(path+[node1])
                    
            if(R_C[1]==1):
                node1=node[1]+node[0]+node[2:]
                node2=node[0:1]+node[2]+node[1]+node[3:]
                node3=node[0:1]+node[4]+node[2:4]+node[1]+node[5:]
                if node3 not in visited:
                    queue.append(path+[node3])
                if node2 not in visited:
                    queue.append(path+[node2])
                if node1 not in visited:
                    queue.append(path+[node1]) 
                                
            if(R_C[1]==2):
                node1=node[0:1]+node[2]+node[1]+node[3:]
                node2=node[0:2]+node[5]+node[3:5]+node[2]+node[6:]    
                if(not node2 in visited):
                    queue.append(path+[node2])
                if(not node1 in visited):
                    queue.append(path+[node1])
                
        elif(R_C[0]==1):
            if(R_C[1]==0):
                node1=node[3]+node[1:3]+node[0]+node[4:]
                node2=node[0:3]+node[4]+node[3]+node[5:]
                node3=node[0:3]+node[6]+node[4:6]+node[3]+node[7:]
                if(not node3 in visited):
                    queue.append(path+[node3])
                if(not node2 in visited):
                    queue.append(path+[node2])
                if(not node1 in visited):
                    queue.append(path+[node1])
                
            if(R_C[1]==1):
                node1=node[0:3]+node[4]+node[3]+node[5:]
                node2=node[0]+node[4]+node[2:4]+node[1]+node[5:]
                node3=node[0:4]+node[5]+node[4]+node[6:]
                node4=node[0:4]+node[7]+node[5:7]+node[4]+node[8]
                if(not node4 in visited):
                    queue.append(path+[node4])
                if(not node3 in visited):
                    queue.append(path+[node3])
                if(not node2 in visited):
                    queue.append(path+[node2])
                if(not node1 in visited):
                    queue.append(path+[node1])
                
            if(R_C[1]==2):
                node1=node[0:4]+node[5]+node[4]+node[6:]
                node2=node[0:2]+node[5]+node[3:5]+node[2]+node[6:]
                node3=node[0:5]+node[8]+node[6:8]+node[5]
                if(not node3 in visited):
                    queue.append(path+[node3])
                if(not node2 in visited):
                    queue.append(path+[node2])
                if(not node1 in visited):
                    queue.append(path+[node1])
                
        elif R_C[0] == 2:
            if R_C[1] == 0:
                node1 = node[0:3]+ node[6] + node[4:6] + node[3] + node[7:]
                node2 = node[0:6] + node[7] + node[6] + node[8]
                if node2 not in visited:
                    queue.append(path+[node2])
                if node1 not in visited:
                    queue.append(path+[node1])
                
            if R_C[1] == 1:
                node1 = node[0:6] + node[7] + node[6] + node[8]
                node2 = node[0:4] + node[7] + node[5:7] + node[4] + node[8]
                node3 = node[0:7] + node[8] + node[7]
                if node3 not in visited:
                    queue.append(path+[node3])
                if node2 not in visited:
                    queue.append(path+[node2])
                if node1 not in visited:
                    queue.append(path+[node1])
                
            if R_C[1] == 2:
                node1 = node[0:7] + node[8] + node[7]
                node2 = node[0:5] + node[8] + node[6:8] + node [5]
                if node2 not in visited:
                    queue.append(path+[node2])
                if node1 not in visited:
                    queue.append(path+[node1])
        if queue:node_stack.append((node,queue[0][-1]))

def BFS(S_G):
    print("---------------------------------")
    print("BFS ALGO")
    print("---------------------------------")
    start=time.time()
    visited=set()
    queue=deque()
    queue.append([S_G[0]])
    goal=[S_G[1],0]
    node_stack=copy.deepcopy(list(BFS_HELP(queue,goal,visited)))
    end=time.time()
    t_time=end-start
    print(f"Time taken: {t_time:.4f} seconds")



### UCS
def UCS_HELP(pq,G,visited):
    while pq:
        dist,path=heapq.heappop(pq)
        node=path[-1]
        if node==G:
            print("Path found to the goal (UCS)")
            print("No of nodes visited (UCS):",dist)
            display_path(path)
            return
        if node in visited:
            continue
        visited.add(node)
        R_C=INITIAL_LOC(node)
        if(R_C[0]==0):
            if(R_C[1]==0):
                node1=node[1]+node[0]+node[2:]
                node2=node[3]+node[1:3]+node[0]+node[4:]    
                if node2 not in visited:
                    heapq.heappush(pq,(dist+1,path+[node2]))
                if node1 not in visited:
                    heapq.heappush(pq,(dist+1,path+[node1]))
                    
            if(R_C[1]==1):
                node1=node[1]+node[0]+node[2:]
                node2=node[0:1]+node[2]+node[1]+node[3:]
                node3=node[0:1]+node[4]+node[2:4]+node[1]+node[5:]
                if node3 not in visited:
                    heapq.heappush(pq,(dist+1,path+[node3]))
                if node2 not in visited:
                    heapq.heappush(pq,(dist+1,path+[node2]))
                if node1 not in visited:
                    heapq.heappush(pq,(dist+1,path+[node1])) 
                                
            if(R_C[1]==2):
                node1=node[0:1]+node[2]+node[1]+node[3:]
                node2=node[0:2]+node[5]+node[3:5]+node[2]+node[6:]    
                if(not node2 in visited):
                    heapq.heappush(pq,(dist+1,path+[node2]))
                if(not node1 in visited):
                    heapq.heappush(pq,(dist+1,path+[node1]))
                
        elif(R_C[0]==1):
            if(R_C[1]==0):
                node1=node[3]+node[1:3]+node[0]+node[4:]
                node2=node[0:3]+node[4]+node[3]+node[5:]
                node3=node[0:3]+node[6]+node[4:6]+node[3]+node[7:]
                if(not node3 in visited):
                    heapq.heappush(pq,(dist+1,path+[node3]))
                if(not node2 in visited):
                    heapq.heappush(pq,(dist+1,path+[node2]))
                if(not node1 in visited):
                    heapq.heappush(pq,(dist+1,path+[node1]))
                
            if(R_C[1]==1):
                node1=node[0:3]+node[4]+node[3]+node[5:]
                node2=node[0]+node[4]+node[2:4]+node[1]+node[5:]
                node3=node[0:4]+node[5]+node[4]+node[6:]
                node4=node[0:4]+node[7]+node[5:7]+node[4]+node[8]
                if(not node4 in visited):
                    heapq.heappush(pq,(dist+1,path+[node4]))
                if(not node3 in visited):
                    heapq.heappush(pq,(dist+1,path+[node3]))
                if(not node2 in visited):
                    heapq.heappush(pq,(dist+1,path+[node2]))
                if(not node1 in visited):
                    heapq.heappush(pq,(dist+1,path+[node1]))
                
            if(R_C[1]==2):
                node1=node[0:4]+node[5]+node[4]+node[6:]
                node2=node[0:2]+node[5]+node[3:5]+node[2]+node[6:]
                node3=node[0:5]+node[8]+node[6:8]+node[5]
                if(not node3 in visited):
                    heapq.heappush(pq,(dist+1,path+[node3]))
                if(not node2 in visited):
                    heapq.heappush(pq,(dist+1,path+[node2]))
                if(not node1 in visited):
                    heapq.heappush(pq,(dist+1,path+[node1]))
                
        elif R_C[0] == 2:
            if R_C[1] == 0:
                node1 = node[0:3]+ node[6] + node[4:6] + node[3] + node[7:]
                node2 = node[0:6] + node[7] + node[6] + node[8]
                if node2 not in visited:
                    heapq.heappush(pq,(dist+1,path+[node2]))
                if node1 not in visited:
                    heapq.heappush(pq,(dist+1,path+[node1]))
                
            if R_C[1] == 1:
                node1 = node[0:6] + node[7] + node[6] + node[8]
                node2 = node[0:4] + node[7] + node[5:7] + node[4] + node[8]
                node3 = node[0:7] + node[8] + node[7]
                if node3 not in visited:
                    heapq.heappush(pq,(dist+1,path+[node3]))
                if node2 not in visited:
                    heapq.heappush(pq,(dist+1,path+[node2]))
                if node1 not in visited:
                    heapq.heappush(pq,(dist+1,path+[node1]))
                
            if R_C[1] == 2:
                node1 = node[0:7] + node[8] + node[7]
                node2 = node[0:5] + node[8] + node[6:8] + node [5]
                if node2 not in visited:
                    heapq.heappush(pq,(dist+1,path+[node2]))
                if node1 not in visited:
                    heapq.heappush(pq,(dist+1,path+[node1]))

def UCS(S_G):
    print("---------------------------------")
    print("UCS ALGO")
    print("---------------------------------")
    start=time.time()
    visited=set()
    pq=[]
    heapq.heappush(pq,(0,[S_G[0]]))
    UCS_HELP(pq,S_G[1],visited)
    end=time.time()
    t_time=end-start
    print(f"Time taken: {t_time:.4f} seconds")



### IDS
def IDS_HELP(stack,G,visited,limit):
    while stack:
        path=stack.pop()
        node=path[-1]
        depth=len(path)-1
        if node==G[0]:
            print("Path found to the goal (IDS)")
            print("No of nodes visited (IDS):",G[1])
            display_path(path)
            return True
        if node in visited:
            continue
        if depth>=limit:
            continue
        visited.add(node)
        steps=G[1]+1
        G[1]=steps
        R_C=INITIAL_LOC(node)
        if(R_C[0]==0):
            if(R_C[1]==0):
                node1=node[1]+node[0]+node[2:]
                node2=node[3]+node[1:3]+node[0]+node[4:]    
                if node2 not in visited:
                    stack.append(path+[node2])
                if node1 not in visited:
                    stack.append(path+[node1])
                    
            if(R_C[1]==1):
                node1=node[1]+node[0]+node[2:]
                node2=node[0:1]+node[2]+node[1]+node[3:]
                node3=node[0:1]+node[4]+node[2:4]+node[1]+node[5:]
                if node3 not in visited:
                    stack.append(path+[node3])
                if node2 not in visited:
                    stack.append(path+[node2])
                if node1 not in visited:
                    stack.append(path+[node1]) 
                                
            if(R_C[1]==2):
                node1=node[0:1]+node[2]+node[1]+node[3:]
                node2=node[0:2]+node[5]+node[3:5]+node[2]+node[6:]    
                if(not node2 in visited):
                    stack.append(path+[node2])
                if(not node1 in visited):
                    stack.append(path+[node1])
                
        elif(R_C[0]==1):
            if(R_C[1]==0):
                node1=node[3]+node[1:3]+node[0]+node[4:]
                node2=node[0:3]+node[4]+node[3]+node[5:]
                node3=node[0:3]+node[6]+node[4:6]+node[3]+node[7:]
                if(not node3 in visited):
                    stack.append(path+[node3])
                if(not node2 in visited):
                    stack.append(path+[node2])
                if(not node1 in visited):
                    stack.append(path+[node1])
                
            if(R_C[1]==1):
                node1=node[0:3]+node[4]+node[3]+node[5:]
                node2=node[0]+node[4]+node[2:4]+node[1]+node[5:]
                node3=node[0:4]+node[5]+node[4]+node[6:]
                node4=node[0:4]+node[7]+node[5:7]+node[4]+node[8]
                if(not node4 in visited):
                    stack.append(path+[node4])
                if(not node3 in visited):
                    stack.append(path+[node3])
                if(not node2 in visited):
                    stack.append(path+[node2])
                if(not node1 in visited):
                    stack.append(path+[node1])
                
            if(R_C[1]==2):
                node1=node[0:4]+node[5]+node[4]+node[6:]
                node2=node[0:2]+node[5]+node[3:5]+node[2]+node[6:]
                node3=node[0:5]+node[8]+node[6:8]+node[5]
                if(not node3 in visited):
                    stack.append(path+[node3])
                if(not node2 in visited):
                    stack.append(path+[node2])
                if(not node1 in visited):
                    stack.append(path+[node1])
                
        elif R_C[0] == 2:
            if R_C[1] == 0:
                node1 = node[0:3]+ node[6] + node[4:6] + node[3] + node[7:]
                node2 = node[0:6] + node[7] + node[6] + node[8]
                if node2 not in visited:
                    stack.append(path+[node2])
                if node1 not in visited:
                    stack.append(path+[node1])
                
            if R_C[1] == 1:
                node1 = node[0:6] + node[7] + node[6] + node[8]
                node2 = node[0:4] + node[7] + node[5:7] + node[4] + node[8]
                node3 = node[0:7] + node[8] + node[7]
                if node3 not in visited:
                    stack.append(path+[node3])
                if node2 not in visited:
                    stack.append(path+[node2])
                if node1 not in visited:
                    stack.append(path+[node1])
                
            if R_C[1] == 2:
                node1 = node[0:7] + node[8] + node[7]
                node2 = node[0:5] + node[8] + node[6:8] + node [5]
                if node2 not in visited:
                    stack.append(path+[node2])
                if node1 not in visited:
                    stack.append(path+[node1])
    return False

def IDS(S_G):
    print("---------------------------------")
    print("IDS ALGO")
    print("---------------------------------")
    start=time.time()
    limit=1
    total_nodes=0
    while True:
        print(f"Searching at depth limit: {limit}")
        visited=set()
        stack=list()
        stack.append([S_G[0]])
        goal=[S_G[1],0]
        found=IDS_HELP(stack,goal,visited,limit)
        total_nodes+=goal[1]
        if found:
            print("No of nodes visited total across all iterations (IDS):",total_nodes)
            break
        limit+=1
    end=time.time()
    t_time=end-start
    print(f"Time taken: {t_time:.4f} seconds")
    


S_G=list(INPUT())
DFS(S_G)
BFS(S_G)
UCS(S_G)
IDS(S_G)