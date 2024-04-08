# AI_Sliding_Puzzle

## PROBLEM DEFINITION
Sliding puzzle is a game played in different levels  (2x2, 3x3, 4x4, 5x5) grid with a determined number of tiles and one space. The objective of the game is to rearrange the tiles from a given initial state to a desired goal initially by sliding the empty space into the neighboring tiles (left, right, up, down).

## AGENT SPECIFICATION
### Performance Measure:
Complete and minimize the number of moves, time, and space complexity taken to reach the goal state.

### Environment:
A grid representing the puzzle

### Actuators: 
The agent can perform actions to move the tiles in four directions: up, down, left, and right.

### Sensors:
The agent perceives the current state of the puzzle, including the positions of the tiles and the empty space, to determine the next action to take based on the chosen algorithm.

## PROBLEM FORMULATION

### Start state: 
{2,3,1,0} for 2*2 puzzle,
             
{6,1,2,4,0,3,5,7,8} for 3*3 puzzle.
           
{2,5,1,4,6,9,3,8,10,13,7,12,14,11,15,0} for 4*4 puzzle.
           
{1,7,2,4,5,6,12,3,8,10,11,17,13,9,15,0,22,18,14,19,16,21,23,24,20} for 5*5 puzzle   .     
     
### Goal State:  
The image is arranged in the right order.

### Search space:

A state description specifies the location of each the determined number of tiles (3,8,15,24) and the blank in one of the tiles grid.

### Action:

the available actions for the blank space(left, right, up, down), and each action depends on where the blank tile is.

### Path cost: 

it takes a unique cost which is equal to 1 for each cost.

## TASK ENVIRONMENT

1- Fully observable

2- Deterministic

3- Sequential

4- Single-agent

5- Static

6- Discrete


## WHAT OUR PROJECT DOES

We created this project to solve a sliding puzzle game with 4 versions (2*2,3*3,4*4,5*5) with different AI algorithms  

## ALGORITHMS USED TO SOLVE THE PROBLEM

1- Breadth-first Search

2- Depth-first Search 

3- Uniform Cost Search (Dijkstra)

4- A_Star Algorithm

5- Greedy Algorithm




