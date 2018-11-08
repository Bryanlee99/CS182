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
<<<<<<< HEAD
=======
from game import Directions
>>>>>>> 78cd9fef1a5c95ffb80f2a370ca3b7eff5f83771

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
<<<<<<< HEAD
    util.raiseNotDefined()
=======
    # Stores states on frontier
    to_search = util.Stack()
    # Stores states' parents to return moves
    parent_dict = {}
    # Visited states
    visited = []
    to_search.push((problem.getStartState(), 'None', 1))

    # DFS
    while(not to_search.isEmpty()):
        state = to_search.pop()
        if(problem.isGoalState(state[0])):
            # Retrace path to goal
            moves = []
            curr_state = state
            while(True):
                if (curr_state[0] == problem.getStartState()):
                    break
                moves.append(curr_state[1])
                curr_state = parent_dict[curr_state]
            moves = list(reversed(moves))
            return moves
        if(state[0] in visited):
             continue
        # Mark as visited
        visited.append(state[0])
        # Append neighbors
        neighbors = problem.getSuccessors(state[0])
        for a in neighbors:
            if(a[0] not in visited):
                to_search.push(a)
                parent_dict[a] = state
>>>>>>> 78cd9fef1a5c95ffb80f2a370ca3b7eff5f83771

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
<<<<<<< HEAD
    util.raiseNotDefined()
=======
    # Stores states on frontier
    to_search = util.Queue()
    # Stores states' parents to return moves
    parent_dict = {}
    # Visited states
    visited = []
    to_search.push((problem.getStartState(), []))

    # BFS
    while (not to_search.isEmpty()):
        state = to_search.pop()
        if (problem.isGoalState(state[0])):
            return state[1]
        if (state[0] in visited):
            continue
        # Mark as visited
        visited.append(state[0])
        # Append neighbors
        neighbors = problem.getSuccessors(state[0])
        for n in neighbors:
            loc_corner_state = n[0]
            updated_action = state[1] + [n[1]]
            if (loc_corner_state not in visited):
                to_search.push((loc_corner_state, updated_action))
>>>>>>> 78cd9fef1a5c95ffb80f2a370ca3b7eff5f83771

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
<<<<<<< HEAD
=======
    # Stores states on frontier
    to_search = util.PriorityQueue()
    # Parent
    parent_dict = {}
    # Visited states
    visited = []
    to_search.push((problem.getStartState(), []), 0)
    parent_dict[problem.getStartState()] = []
    # UCS
    while (not to_search.isEmpty()):
        state = to_search.pop()
        if (problem.isGoalState(state[0])):
            return state[1]
        if (state[0] in visited):
            continue
        # Mark as visited
        visited.append(state[0])
        # Append neighbors
        neighbors = problem.getSuccessors(state[0])
        for n in neighbors:
            if (n[0] not in visited):
                parent_dict[n[0]] = parent_dict[state[0]] + [n[1]]
                to_search.push((n[0], state[1] + [n[1]]), problem.getCostOfActions(state[1] + [n[1]]))

>>>>>>> 78cd9fef1a5c95ffb80f2a370ca3b7eff5f83771
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
<<<<<<< HEAD
    util.raiseNotDefined()


=======
    # Stores states on frontier
    to_search = util.PriorityQueue()
    # Parent
    parent_dict = {}
    # Visited states
    visited = []
    # States are ((location, corners_visited), action)
    to_search.push(((problem.getStartState(), []), [], 1), 0 + heuristic(problem.getStartState(), problem))
    # A*
    while (not to_search.isEmpty()):
        state = to_search.pop()
        if (problem.isGoalState(state[0][0])):
            return state[1]
        if (state[0] in visited):
            continue
        # Mark as visited
        visited.append(state[0])
        # Append neighbors
        neighbors = problem.getSuccessors(state[0][0])
        for n in neighbors:
            if (n[0] not in visited):
                to_search.push(((n[0], []), state[1] + [n[1]]), problem.getCostOfActions(state[1] + [n[1]]) \
                               + heuristic(n[0], problem))
    util.raiseNotDefined()

>>>>>>> 78cd9fef1a5c95ffb80f2a370ca3b7eff5f83771
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
