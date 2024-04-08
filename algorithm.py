from settings import *
import copy
import sys
import time
import heapq

#------------dictonary intializtion ------------
# store parents
Parent_state={}
# get id from state
State_from_id={}
# get state with id
ID_form_state={}


#---------------- functions --------------------
def init_for_DBFS(start,goal,gameLevel):
    s=tuple(tuple(sub)for sub in start)
    g=tuple(tuple(sub)for sub in goal)
    return s,g

def valid(x,y,gameSize):
    return x>=0 and x<gameSize and y>=0 and y<gameSize

def find_zero(state):
    pos=[0,0]
    for i in range(len(state)):
        for j in range(len(state)):
            if(state[i][j]==0):
                pos=[i,j]
                return pos
    

def get_next_states(state,gameSize):
    pos=find_zero(state)
    Dx=[-1,1,0,0]
    Dy=[0,0,-1,1]
    Dirctions=["down","up","right","left"]
    states=[]
    dir=[]
    for k in range (0,4):
        x=pos[0]+Dx[k]
        y=pos[1]+Dy[k]
        if(valid(x,y,gameSize)):
            new=[list(sub)for sub in state]
            new[pos[0]][pos[1]],new[x][y]= new[x][y],new[pos[0]][pos[1]]
            states.append(tuple(tuple(sub)for sub in new))
            dir.append(Dirctions[k])
   
    return states,dir

def get_dimen(current, key):
    for x in range(len(current)):
        for y in range(len(current[0])):
            if current[x][y]==key:
                return x,y
            

def heuristics(current, goal,gameSize):
    sum = 0
    for i in range(1,gameSize**2):
        x1,y1 = get_dimen(current,i)
        x2,y2 = get_dimen(goal,i)
        sum+= abs(x1-x2) + abs(y1-y2)
    return sum

# ------------------ Deapth-Breadth first Search -----------------------
def D_B_FS(start,goal,pop,gameSize):
    # id,direction
    q=[(1,[])]
    ID=2
    level=0
    while len(q)>0:
        state_id,path=q.pop(pop)
        level+=1
        if State_from_id[state_id] == goal:
            return path
        
        if sys.getsizeof(State_from_id)>=10**7 or (pop==-1 and level>=500):
            return ""
        
        next_states,direction=get_next_states(State_from_id[state_id],gameSize)
        
        for i in range(len(next_states)):
            
            if next_states[i] not in ID_form_state:
                ID_form_state[next_states[i]]=ID
                State_from_id[ID]=next_states[i]
                q.append((ID,path+[direction[i]]))
                ID+=1
        
    return ""


# ------------------ Uniform cost Search ------------------------
def UCS(start,goal,pop,gameSize):
    q=[(0,1,[])]
    ID=2
    while q:
        q.sort()
        curr_cost,state_id,path=q.pop(pop)
        if State_from_id[state_id] == goal:
            return path
        
        if sys.getsizeof(State_from_id)>=10**7:
            return ""
        
        next_states,dir=get_next_states(State_from_id[state_id],gameSize)
        
        for i in range(len(next_states)):
            if next_states[i] not in ID_form_state:
                Parent_state[ID]=state_id
                ID_form_state[next_states[i]]=ID
                State_from_id[ID]=next_states[i]
                q.append((curr_cost+1,ID,path+[dir[i]]))
                ID+=1
        
    return "" 

# ------------------ Gready fisrt search --------------------
def Gready(start,goal,pop,gameSize):
    vistited = []
    fronter = [(heuristics(start,goal,gameSize) , start , [])]
    while len(fronter)>0:
        curr_cost , curr_state , curr_path = heapq.heappop(fronter)
        if curr_state == goal:
            return curr_path 
        if curr_state not in vistited:
            vistited.append(curr_state)
            neighbours,dir = get_next_states(curr_state,gameSize)  # neighbours(curr_state)
            for i in range(len(neighbours)):
                heapq.heappush(fronter,( heuristics(neighbours[i],goal,gameSize), neighbours[i] , curr_path+[dir[i]]))
    return ""

# ----------------------------A Star-----------------------------
def A_Star(start,goal,pop,gameSize):
    vistited = []
    fronter = [(heuristics(start,goal,gameSize) , start , [])]
    while len(fronter)>0:
        curr_cost , curr_state , curr_path = heapq.heappop(fronter)
        curr_actual_path_cost = curr_cost-heuristics(curr_state,goal,gameSize)
        if curr_state == goal:
            return curr_path 
        
        if curr_state not in vistited:
            vistited.append(curr_state)
            neighbours,dir = get_next_states(curr_state,gameSize)  # neighbours(curr_state)
            for i in range(len(neighbours)):
                heapq.heappush(fronter,( curr_actual_path_cost + 1 + heuristics(neighbours[i],goal,gameSize), neighbours[i] , curr_path+[dir[i]]))
    return ""

def Choose_algo(st,gl,type,gameSize):

    start,goal=init_for_DBFS(st,gl,gameSize)
   
    global Parent_state,State_from_id,ID_form_state
    if Parent_state:
        Parent_state.clear()
        State_from_id.clear()
        ID_form_state.clear()
    Parent_state[1]=()
    State_from_id={1:start}
    ID_from_state={start:1}
    Algorithms={
        "DFS":D_B_FS,
        "BFS":D_B_FS,
        "UCS":UCS,
        "Gready":Gready,
        "A_star":A_Star,
    }
   
    if type=='DFS':
        return D_B_FS(start,goal,-1,gameSize)
    path=Algorithms[type](start,goal,0,gameSize)
    return path

def Solve(type,gameLevel):
    tilesize,gameSize,start,goal=set_game(gameLevel)
    path=Choose_algo(start,goal,type,gameSize)
    return path



