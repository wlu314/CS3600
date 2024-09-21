# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    ## Start State
    start = problem.getStartState() 
    ## Initialization
    frontier = util.Stack()
    explored = set()
    node = {"state" : start, "path": []}
    ## Push startState
    frontier.push(node)
    
    ## Loop
    while not frontier.isEmpty():
        node = frontier.pop() 
        state = node["state"]
        
        ## If the state is already explored
        if state in explored: 
            continue
        explored.add(state)
        ## Check Goal State
        if problem.isGoalState(state):
            return node["path"]
        
        ## Note: Successor is given as a tuple (successor, action, stepCost), successor[0] = state, successor[1] = path
        for successor in problem.getSuccessors(state):
            if successor[0] not in explored:
                updated_path = node["path"] + [successor[1]]
                updated_node = {"state" : successor[0], "path" : updated_path}
                frontier.push(updated_node)
    
    util.raiseNotDefined()
        


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    ## Start State
    start = problem.getStartState() 
    ## Initialization
    frontier = util.Queue()
    explored = set()
    node = {"state" : start, "path" : []}
    ## Push Start
    frontier.push(node)
    
    ## Loop
    while not frontier.isEmpty():
        node = frontier.pop()
        state = node["state"]
        path = node["path"]
        
        if state in explored: 
            continue
        explored.add(state)
        
        ## Goal Check
        if problem.isGoalState(state): 
            return node["path"]
        
        ## Add the nieghbors
        for successor in problem.getSuccessors(state):
            if successor[0] not in explored:
                new_state = successor[0]
                new_path = successor[1]
                updated_path = path + [new_path]
                updated_node = {"state" : new_state, "path" : updated_path}       
                frontier.push(updated_node)
    util.raiseNotDefined()
    
def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """
    "*** YOUR CODE HERE ***"
    ## Start State
    start = problem.getStartState()
    ## Initialization 
    frontier = util.PriorityQueue()
    explored = set()
    node = {"state": start, "path": [], "cost": 0}
    ## Push start
    frontier.push(node, 0)
    
    ## Loop 
    while not frontier.isEmpty():
        node = frontier.pop()
        state = node["state"]
        path = node["path"]
        cost = node["cost"]
        
        if state not in explored:
            if problem.isGoalState(state):
                return path
            explored.add(state)
            for successor in problem.getSuccessors(state):
                s_state = successor[0] ## successors statae
                s_path = successor[1] ## action
                s_cost = successor[2] ## step cost
                updated_cost = cost + s_cost
                updated_path = path + [s_path]
                new_node = {"state": s_state, "path": updated_path, "cost": updated_cost}
                frontier.push(new_node, updated_cost)
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    "*** YOUR CODE HERE ***"
    ## Start State
    start = problem.getStartState()
    ## Initialization 
    frontier = util.PriorityQueue()
    explored = set()
    node = {"state": start, "path": [], "cost": 0}
    ## Push start
    frontier.push(node, 0)
    
    while not frontier.isEmpty():
        node = frontier.pop()
        state = node["state"]
        path = node["path"]
        cost = node["cost"]
        
        if problem.isGoalState(state):
            return path
        
        if state not in explored:
            explored.add(state)
            
            ## Expanding on Succesors
            for successor in problem.getSuccessors(state):
                s_state = successor[0] ## successors statae
                s_path = successor[1] ## action
                s_cost = successor[2] ## step cost
                updated_cost = cost + s_cost
                updated_path = path + [s_path]
                new_node = {"state": s_state, "path" : updated_path, "cost": updated_cost}

                ## Heurisitc 
                f_n = problem.getCostOfActions(updated_path) + heuristic(s_state, problem)
                frontier.push(new_node, f_n)
    
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
