# Unimelb COMP90054 Search Algorithms

## Acknowledgments

I would like to thank the UC Pacman Projects and the Unimelb COMP90054 2022S2 teaching team for providing the code framework.

## Project Introduction

There are 4 tasks that I have completed in this project.

First, I implemented a series of basic search algorithms and observe their performance in the Pacman maze. These algorithms include:

* Depth First Search Algorithm
* Breadth First Search Algorithm
* Uniform Cost Search Algorithm
* Greedy Best First Search Algorithm
* A Star Search Algorithm

Second, I implemented **Enforced Hill Climbing Algorithm**, using Manhattan Distance as the heuristic.

Third, I implemented **Bidirectional A Star Enhanced Algorithm**, which is a search algorithm that searches in both directions, from the intial state to the goal state, and from the goal state towards the initial state, and keeps track of solutions found when the two directions meet, using Manhattan Distance as both the forward heuristic and backward heuristic.

Finally, I modeled a more complex problem using the **Bidirectional A Star Enhanced Algorithm** and created an agent to eat all the food in a maze, called `BidirectionalFoodSearchProblem`. I designed the state representation, implemented functions for the initial state and goal states, and created successor functions for both forward and backward searches. Additionally, I implemented two heuristics to guide the search, ensuring that they are admissible and consistent.

## Code Instructions

This code repository must run in a Python 3.6 environment. My code only occupies part of the files `/search.py` and `/searchAgents.py`, indicated by the comment `*** YOUR CODE HERE ***`, while the rest of the code is from the UC Pacman Projects and the Unimelb COMP90054 teaching team framework.

### Pacman Game

First, you can run the following code to load the Pacman program, which is a simple Pacman game.

```
python pacman.py
```

### Basic Search Algorithms in Pacman Maze

You can use the following command to apply different search algorithms in various mazes.

```
python pacman.py -l MazeName -p SearchAgent -a fn=SearchAlgorithmName
```

The available options for `MazeName` are:

* `tinyMaze`
* `smallMaze`
* `mediumMaze`
* `bigMaze`

The available options for `SearchAlgorithmName` are:

* `dfs`: Depth First Search
* `bfs`: Breadth First Search
* `ucs`: Uniform Cost Search
* `gbfs`: Greedy Best First Search
* `astar`: A Star Search

### Enforced Hill Climbing Algorithm

You can use the following command to perform search in different mazes with **Enforced Hill Climbing Algorithm**, utilizing Manhattan Distance as heuristic function：

```
python pacman.py -l MazeName -p SearchAgent -a fn=ehc,heuristic=manhattanHeuristic
```

The available options for `MazeName` are:

* `tinyMaze`
* `smallMaze`
* `mediumMaze`
* `bigMaze`

### Bidirectional A Star Enhanced Algorithm for Single-Object Search

You can use the following command to perform bidirectional search in different mazes, with **singe object**, with **Bidirectional A Star Enhanced Algorithm**, utilizing Manhattan Distance as both forward and backward heuristic functions：

```
python pacman.py -l MazeName -p BidirectionalSearchAgent -a fn=bae,heuristic=manhattanHeuristic,backwardsHeuristic=backwardsManhattanHeuristic
```

The available options for `MazeName` are:

* `tinyMaze`
* `smallMaze`
* `mediumMaze`
* `bigMaze`

### Bidirectional A Star Enhanced Algorithm for Multi-Object Search

You can use the following command to perform bidirectional search in different mazes, with **multiple objects**, with **Bidirectional A Star Enhanced Algorithm**, utilizing customized forward and backward heuristic functions：

```
python pacman.py -l MazeName -p BidirectionalFoodSearchAgent -a fn=bae,heuristic=bidirectionalFoodProblemHeuristic,backwardsHeuristic=bidirectionalFoodProblemBackwardsHeuristic
```

The available options for `MazeName` are:

* `tinyCorners`
* `smallCorners`
* `mediumCorners`
* `mediumDottedMaze`
* `bigCorners`

## Project Evaluation

You can use the following command to evaluate this project.

Use this command for theUC Pacman Projects case:

```
python ./autograder.py --test-directory=test_cases
```

Use this command for the Unimelb case:

```
python ./autograder.py --test-directory=test_cases_project
```
