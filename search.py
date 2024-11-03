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

from cmath import inf
from itertools import accumulate
from queue import PriorityQueue
import util
from math import inf as INF


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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    startState = problem.getStartState()
    startNode = (startState, '', 0, [])

    openList = util.Stack()
    openList.push(startNode)
    closedList = set()

    while not openList.isEmpty():
        node = openList.pop()
        state, action, cost, path = node

        if state not in closedList:
            closedList.add(state)

            if problem.isGoalState(state):
                path = path + [(state, action)]
                actions = [action[1] for action in path]
                del actions[0]
                return actions

            for succ in problem.getSuccessors(state):
                succState, succAction, succCost = succ
                newNode = (succState, succAction, cost + succCost, path + [(state, action)])
                openList.push(newNode)

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()
    startNode = (startState, '', 0, [])

    openList = util.Queue()
    openList.push(startNode)
    closedList = set()

    while not openList.isEmpty():
        node = openList.pop()
        state, action, cost, path = node

        if state not in closedList:
            closedList.add(state)

            if problem.isGoalState(state):
                path = path + [(state, action)]
                actions = [action[1] for action in path]
                del actions[0]
                return actions

            for succ in problem.getSuccessors(state):
                succState, succAction, succCost = succ
                newNode = (succState, succAction, cost + succCost, path + [(state, action)])
                openList.push(newNode)

    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    startState = problem.getStartState()
    startNode = (startState, '', 0, [])

    openList = util.PriorityQueue()
    openList.push(startNode, 0)
    closedList = set()

    while not openList.isEmpty():
        node = openList.pop()
        state, action, cost, path = node

        if state not in closedList:
            closedList.add(state)

            if problem.isGoalState(state):
                path = path + [(state, action)]
                actions = [action[1] for action in path]
                del actions[0]
                return actions

            for succ in problem.getSuccessors(state):
                succState, succAction, succCost = succ
                newNode = (succState, succAction, cost + succCost, path + [(state, action)])
                openList.push(newNode, cost + succCost)

    util.raiseNotDefined()


def greedyBestFirstSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    startState = problem.getStartState()
    startNode = (startState, '', 0, [])

    openList = util.PriorityQueue()
    openList.push(startNode, heuristic(startState, problem))
    closedList = set()

    while not openList.isEmpty():
        node = openList.pop()
        state, action, cost, path = node

        if state not in closedList:
            closedList.add(state)

            if problem.isGoalState(state):
                path = path + [(state, action)]
                actions = [action[1] for action in path]
                del actions[0]
                return actions

            for succ in problem.getSuccessors(state):
                succState, succAction, succCost = succ
                newNode = (succState, succAction, cost + succCost, path + [(state, action)])
                openList.push(newNode, heuristic(succState, problem))

    util.raiseNotDefined()


# Please DO NOT change the following code, we will use it later
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    myPQ = util.PriorityQueue()
    startState = problem.getStartState()
    startNode = (startState, '',0, [])
    myPQ.push(startNode,heuristic(startState,problem))
    visited = set()
    best_g = dict()
    while not myPQ.isEmpty():
        node = myPQ.pop()
        state, action, cost, path = node
        if (not state in visited) or cost < best_g.get(state):
            visited.add(state)
            best_g[state]=cost
            if problem.isGoalState(state):
                path = path + [(state, action)]
                actions = [action[1] for action in path]
                del actions[0]
                return actions
            for succ in problem.getSuccessors(state):
                succState, succAction, succCost = succ
                newNode = (succState, succAction, cost + succCost, path + [(state, action)])
                myPQ.push(newNode,heuristic(succState,problem)+cost+succCost)
    util.raiseNotDefined()


def enforcedHillClimbing(problem, heuristic=nullHeuristic):
    """
    Local search with heuristic function.
    You DO NOT need to implement any heuristic, but you DO have to call it.
    The heuristic function is "manhattanHeuristic" from searchAgent.py.
    It will be pass to this function as second argument (heuristic).
    """
    "*** YOUR CODE HERE ***"

    # Function of procedure improve: BFS for state with smaller h
    def improve(node):
        # Initialize start node to be the current node
        node_cur = state_cur, action_cur, cost_cur, path_cur = node
        # Initialize open list (queue) and closed list
        open_list = util.Queue()
        open_list.push(node_cur)
        closed_list = set()

        # Procedure of BFS
        while not open_list.isEmpty():
            # The node to be expanded
            node_exp = state_exp, action_exp, cost_exp, path_exp = open_list.pop()
            # Check if the expanded node is the closed list, if not:
            if state_exp not in closed_list:
                # Add the expanded node into closed list
                closed_list.add(state_exp)
                # If the expanded node has smaller h than current node, return the expanded node
                if heuristic(state_exp, problem) < heuristic(state_cur, problem):
                    return node_exp
                # Else proceed to successors of the expanded node
                for successor in problem.getSuccessors(state_exp):
                    suc_state, suc_action, suc_cost = successor
                    new_node = (suc_state, suc_action, cost_exp + suc_cost, path_exp + [(state_exp, action_exp)])
                    open_list.push(new_node)

        # Fail if no solution found
        return

    # Initialize the global start node with global start state
    node = (state, action, cost, path) = (problem.getStartState(), "", 0, [])

    # Procedure of enforced hill climbing search
    while not problem.isGoalState(state):
        node = state, action, cost, path = improve(node)

    # Extract the solution
    path = path + [(state, action)]
    actions = [a[1] for a in path]
    del actions[0]
    return actions

    # put the below line at the end of your code or remove it
    util.raiseNotDefined()


def bidirectionalAStarEnhanced(problem, heuristic=nullHeuristic, backwardsHeuristic=nullHeuristic):
    
    """
    Bidirectional global search with heuristic function.
    You DO NOT need to implement any heuristic, but you DO have to call them.
    The heuristic functions are "manhattanHeuristic" and "backwardsManhattanHeuristic" from searchAgent.py.
    It will be pass to this function as second and third arguments.
    You can call it by using: heuristic(state,problem) or backwardsHeuristic(state,problem)
    """
    "*** YOUR CODE HERE ***"
    # The problem passed in going to be BidirectionalPositionSearchProblem

    # Pseudocode line 1-2
    # Initialize open lists from two directions and
    open_lists = (open_list_f, open_list_b) = (util.PriorityQueue(), util.PriorityQueue())
    # Pop start nodes from forward direction into associated open list
    start_states = (start_state_f, start_state_b) = (problem.getStartState(), problem.getGoalStates())
    start_node_f = (start_state_f, "", 0, [])
    open_list_f.push(start_node_f, heuristic(start_state_f, problem) - backwardsHeuristic(start_state_f, problem))
    # Pop start nodes from backward direction into associated open list, and there may be multiple goal states
    for states in start_state_b:
        start_node_b = (states, "", 0, [])
        open_list_b.push(start_node_b, backwardsHeuristic(states, problem) - heuristic(states, problem))

    # Pseudocode line 3
    # Initialize closed lists and optimal historical cost lists from two directions
    closed_lists = (closed_list_f, closed_list_b) = (set(), set())
    # Initialize optimal historical cost lists from two directions & optimal path lists from two directions
    best_gs = (best_g_f, best_g_b) = (dict(), dict())
    best_ps = (best_p_f, best_p_b) = (dict(), dict())

    # Pseudocode line 4
    # Initialize lower bound, upper bound, solution list, and direction indicator
    lower_bound = 0  # Lower bound: L
    upper_bound = INF  # Upper bound: U
    solution = []  # List of solution
    x = 0  # Direction indicator: 0 = forward & -1 = backward
    # Put two get successors function into a tuple & put two heuristic functions into a tuple
    get_successors_list = (problem.getSuccessors, problem.getBackwardsSuccessors)
    heuristics = (heuristic, backwardsHeuristic)

    # Pseudocode line 5-23
    # Repeat searching if both two open lists are not empty
    while not open_list_f.isEmpty() and not open_list_b.isEmpty():
        # Pseudocode line 6-8
        # Update lower bound to be average of minimum f value in both open lists
        b_min_f = open_list_f.getMinimumPriority()
        b_min_b = open_list_b.getMinimumPriority()
        lower_bound = (b_min_f + b_min_b) / 2

        # Pseudocode line 9-10
        # Pop a node from open list from current direction and record its state, action, cost, path
        node = open_lists[x].pop()
        state, action, cost, path = node
        # Create a string version of state, because string is hashable
        state_str = str(state)
        # Put current node into closed list from current direction if it is not there or may yield a lower optimal cost
        if state_str not in closed_lists[x] or cost < best_gs[x][state_str]:
            closed_lists[x].add(state_str)

        # Pseudocode line 11-14
        # Check whether current expansion can be a potential solution
        # Record the cost in optimal historical cost list from current direction
        best_gs[x][state_str] = cost
        # Record the path in optimal path list from current direction
        best_ps[x][state_str] = path
        # If current state in opposite closed list, i.e., two paths meet and
        # total costs from both directions is lower than upper bound:
        if state_str in closed_lists[x+1] and best_gs[x][state_str] + best_gs[x+1][state_str] < upper_bound:
            # Update upper bound to be total costs from both directions
            upper_bound = best_gs[x][state_str] + best_gs[x+1][state_str]
            # Store the combined path as potential solution
            solution = best_p_f[state_str] + best_p_b[state_str][::-1]

        # Pseudocode line 15-17
        # Check whether current expansion can be a final solution
        # Stop search if lower bound is no larger than upper bound and return solution
        if lower_bound >= upper_bound:
            return solution

        # Pseudocode line 18-21
        # Continuous search if stopping criteria not satisfied
        # For each successor of current node
        for suc in get_successors_list[x](state):
            # Record the state, action, cost of successor
            suc_state, suc_action, suc_cost = suc
            # Put successor into closed list from current direction if it is not there
            if str(suc_state) not in closed_lists[x]:
                # Create a new node for successor with preorder costs and paths
                new_node = (suc_state, suc_action, cost + suc_cost, path + [suc_action])
                # Calculate the priority of new node
                dx_new_node = best_gs[x][state_str] - heuristics[x+1](state, problem)
                fx_new_node = heuristics[x](suc_state, problem) + cost + suc_cost
                bx_new_node = fx_new_node + dx_new_node
                # Put new node into open list
                open_lists[x].push(new_node, bx_new_node)

        # Pseudocode line 22
        # Re-calculate minimum f value in both open lists
        b_min_f = open_list_f.getMinimumPriority()
        b_min_b = open_list_b.getMinimumPriority()
        # The direction next round has lower f value
        if b_min_f < b_min_b:
            x = 0
        else:
            x = -1

    # Pseudocode 24
    # If there is no such node that makes lower bound no less than upper bound, return the solution anyway,
    # which is the "optimal" potential solution ever found
    return solution

    # put the below line at the end of your code or remove it
    util.raiseNotDefined()


# Abbreviations
dfs = depthFirstSearch
bfs = breadthFirstSearch
ucs = uniformCostSearch
gbfs = greedyBestFirstSearch
astar = aStarSearch

ehc = enforcedHillClimbing
bae = bidirectionalAStarEnhanced
