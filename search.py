# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import *
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

class Path(object):
    def __init__(self, position, directions, cost):
        self.position = position
        self.directions = directions
        self.cost = cost
def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from util import Stack
    road = Stack()
    pathRoad = Stack()
    startState = problem.getStartState()
    
    visited = []
    path = []

    if problem.isGoalState(startState):
        return path

    road.push(startState)
    pathRoad.push([])
    while (True):
         if road.isEmpty(): return []

         currentState = road.pop()
         path = pathRoad.pop()

         visited.append(currentState)

         if problem.isGoalState(currentState):
             return path

         successors = problem.getSuccessors(currentState)

         if successors:
             for child, direction, cost in successors:
                 if child not in visited:

                     newPath = path + [direction]
                     road.push(child)
                     pathRoad.push(newPath)

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    road = Queue()
    pathRoad = Queue()
    visited = []

    startState = problem.getStartState()
    path = []

    road.push(startState)
    pathRoad.push(path)
    visited.append(startState)

    while ( True ):
        if road.isEmpty(): return []
        currentState = road.pop()
        path = pathRoad.pop()
        if problem.isGoalState(currentState): return path

        successors = problem.getSuccessors(currentState)

        if successors:
            for child, direction, cost in successors:
                if child not in visited:
                    newPath = path + [direction]
                    road.push(child)
                    pathRoad.push(newPath)
                    visited.append(child)

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()
    
    #Initializing the queue and closed set    
    queue = PriorityQueue()
    startPath = Path(startState, [], 0)
    queue.push(startPath,0)    
    visited= []
    
    
    
    while not queue.isEmpty():
        
        node = queue.pop()
        currentPosition = node.position
        currentDirections = node.directions
        currentCost = node.cost
        if problem.isGoalState(currentPosition):
            return currentDirections
          
            
        if not currentPosition in visited:
            successors = problem.getSuccessors(currentPosition)
            for position, direction, cost in successors:
                if not position in visited:
                    newSuccessor = Path(position,currentDirections+[direction],currentCost+cost)
                    queue.push(newSuccessor, currentCost+cost)
            visited.append(currentPosition)

    
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()

    queue = PriorityQueue()
    startPath = Path(startState, [], 0)
    queue.push(startPath, 0)
    visited = []

    while not queue.isEmpty():
        node = queue.pop()
        currentPosition = node.position
        currentDirections = node.directions
        currentCost = node.cost

        if problem.isGoalState(currentPosition): return currentDirections

        if not currentPosition in visited:
            successors = problem.getSuccessors(currentPosition)
            for position, direction, cost in successors:
                if not position in visited: 
                    newDirections = currentDirections + [direction]
                    newCost = currentCost + cost;
                    newHeuristic = heuristic(position, problem)
                    totalCost = newCost + newHeuristic
                    newPath = Path(position, newDirections, newCost)
                    queue.push(newPath, totalCost)
            visited.append(currentPosition)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
