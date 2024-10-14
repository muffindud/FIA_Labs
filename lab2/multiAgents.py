# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util, sys

from game import Agent


class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()      # Pacman position after moving
        newFood = successorGameState.getFood()               # Remaining food
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        listFood = newFood.asList()                        # All remaining food as list
        ghostPos = successorGameState.getGhostPositions()  # Get the ghost position
        # Initialize with list 
        mFoodDist = []
        mGhostDist = []

        # Find the distance of all the foods to the pacman 
        for food in listFood:
          mFoodDist.append(manhattanDistance(food, newPos))

        # Find the distance of all the ghost to the pacman
        for ghost in ghostPos:
          mGhostDist.append(manhattanDistance(ghost, newPos))

        if currentGameState.getPacmanPosition() == newPos:
          return (-(float("inf")))

        for ghostDistance in mGhostDist:
          if ghostDistance < 2:
            return (-(float("inf")))

        if len(mFoodDist) == 0:
          return float("inf")
        else:
          minFoodDist = min(mFoodDist)
          maxFoodDist = max(mFoodDist)

        return 1000/sum(mFoodDist) + 10000/len(mFoodDist)


def defaultEval(currentGameState):
    return currentGameState.getScore()


def customEval(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """

    """
        Your improved evaluation function here
    """
    foodList = currentGameState.getFood().asList()
    pacmanPos = currentGameState.getPacmanPosition()
    ghostStates = currentGameState.getGhostStates()
    ghostPos = [ghostState.getPosition() for ghostState in ghostStates]
    foodDist = [manhattanDistance(pacmanPos, food) for food in foodList]
    ghostDist = [manhattanDistance(pacmanPos, ghost) for ghost in ghostPos]
    if len(foodDist) == 0:
        return float("inf")
    else:
        minFoodDist = min(foodDist)
        minGhostDist = min(ghostDist)

    return minGhostDist - minFoodDist


def customImprovedEval(currentGameState):
    foodList = currentGameState.getFood().asList()
    pacmanPos = currentGameState.getPacmanPosition()
    ghostStates = currentGameState.getGhostStates()
    foodDist = [manhattanDistance(pacmanPos, food) for food in foodList]
    ghostDist = [manhattanDistance(pacmanPos, ghost.getPosition()) for ghost in ghostStates if ghost.scaredTimer == 0]
    vulnerableGhostDist = [manhattanDistance(pacmanPos, ghost.getPosition()) for ghost in ghostStates if ghost.scaredTimer > 0]
    if len(foodDist) == 0:
        return float("inf")
    else:
        scaredGhosts = False
        minFoodDist = min(foodDist)
        if len(ghostDist) == 0:
            scaredGhosts = True
            minGhostDist = 0
        else:
            minGhostDist = min(ghostDist)
        if len(vulnerableGhostDist) == 0:
            minVulnerableGhostDist = 0
        else:
            minVulnerableGhostDist = min(vulnerableGhostDist)

    if scaredGhosts:
        return minFoodDist + minVulnerableGhostDist
    else:
        return minGhostDist - minFoodDist + minVulnerableGhostDist


class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn='defaultEval', depth='2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
      Here is the place to define your MiniMax Algorithm
    """
    def __init__(self, evalFn='defaultEval', depth='2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        """
            Your code here
        """

        legalActions = gameState.getLegalActions(0)
        bestAction = None
        bestScore = float("-inf")
        for action in legalActions:
            successor = gameState.generateSuccessor(0, action)
            score = self.minimax(successor, self.depth, 1)
            # print("Action: ", action, "Score: ", score)
            # input("Press Enter to continue...")
            if score > bestScore:
                bestScore = score
                bestAction = action
        return bestAction

    def minimax(self, gameState, depth, agentIndex):
        if depth == 0 or gameState.isWin() or gameState.isLose():
            score = self.evaluationFunction(gameState)
            return score

        if agentIndex == 0:
            return self.maxValue(gameState, depth, agentIndex)
        else:
            return self.minValue(gameState, depth, agentIndex)

    def maxValue(self, gameState, depth, agentIndex):
        v = float("-inf")
        legalActions = gameState.getLegalActions(agentIndex)
        for action in legalActions:
            successor = gameState.generateSuccessor(agentIndex, action)
            v = max(v, self.minimax(successor, depth, agentIndex + 1))
        return v

    def minValue(self, gameState, depth, agentIndex):
        v = float("inf")
        legalActions = gameState.getLegalActions(agentIndex)
        for action in legalActions:
            successor = gameState.generateSuccessor(agentIndex, action)
            if agentIndex == gameState.getNumAgents() - 1:
                v = min(v, self.minimax(successor, depth - 1, 0))
            else:
                v = min(v, self.minimax(successor, depth, agentIndex + 1))
        return v


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Here is the place to define your Alpha-Beta Pruning Algorithm
    """
    def __init__(self, evalFn='defaultEval', depth='2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

    def getAction(self, gameState):
        """
          Your code here
        """
        legalActions = gameState.getLegalActions(0)
        bestAction = None
        alpha = float("-inf")
        beta = float("inf")
        bestScore = float("-inf")
        for action in legalActions:
            successor = gameState.generateSuccessor(0, action)
            score = self.alphabeta(successor, self.depth, 1, alpha, beta)
            if score > bestScore:
                bestScore = score
                bestAction = action
        return bestAction

    def alphabeta(self, gameState, depth, agentIndex, alpha, beta):
        if depth == 0 or gameState.isWin() or gameState.isLose():
            score = self.evaluationFunction(gameState)
            return score

        if agentIndex == 0:
            return self.maxValue(gameState, depth, agentIndex, alpha, beta)
        else:
            return self.minValue(gameState, depth, agentIndex, alpha, beta)

    def maxValue(self, gameState, depth, agentIndex, alpha, beta):
        v = float("-inf")
        legalActions = gameState.getLegalActions(agentIndex)
        for action in legalActions:
            successor = gameState.generateSuccessor(agentIndex, action)
            v = max(v, self.alphabeta(successor, depth, agentIndex + 1, alpha, beta))
            if v > beta:
                return v
            alpha = max(alpha, v)
        return v

    def minValue(self, gameState, depth, agentIndex, alpha, beta):
        v = float("inf")
        legalActions = gameState.getLegalActions(agentIndex)
        for action in legalActions:
            successor = gameState.generateSuccessor(agentIndex, action)
            if agentIndex == gameState.getNumAgents() - 1:
                v = min(v, self.alphabeta(successor, depth - 1, 0, alpha, beta))
            else:
                v = min(v, self.alphabeta(successor, depth, agentIndex + 1, alpha, beta))
            if v < alpha:
                return v
            beta = min(beta, v)
        return v


class AStarMinimaxAgent(MultiAgentSearchAgent):
    """
      Your Minimax algorithm with A* path searching improvement agent
    """

    def getAction(self, gameState):
        """
          Your code here
        """
        pass


class AStarAlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your Alpha-Beta pruning algorithm with A* path searching improvement agent
    """

    def getAction(self, gameState):
        """
          Your code here
        """
        pass


def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    pacmanPos = currentGameState.getPacmanPosition()
    ghostList = currentGameState.getGhostStates() 
    foods = currentGameState.getFood()
    capsules = currentGameState.getCapsules()
    # Return based on game state
    if currentGameState.isWin():
        return float("inf")
    if currentGameState.isLose():
        return float("-inf")
    # Populate foodDistList and find minFoodDist
    foodDistList = []
    for each in foods.asList():
        foodDistList = foodDistList + [util.manhattanDistance(each, pacmanPos)]
    minFoodDist = min(foodDistList)
    # Populate ghostDistList and scaredGhostDistList, find minGhostDist and minScaredGhostDist
    ghostDistList = []
    scaredGhostDistList = []
    for each in ghostList:
        if each.scaredTimer == 0:
            ghostDistList = ghostDistList + [util.manhattanDistance(pacmanPos, each.getPosition())]
        elif each.scaredTimer > 0:
            scaredGhostDistList = scaredGhostDistList + [util.manhattanDistance(pacmanPos, each.getPosition())]
    minGhostDist = -1
    if len(ghostDistList) > 0:
        minGhostDist = min(ghostDistList)
    minScaredGhostDist = -1
    if len(scaredGhostDistList) > 0:
        minScaredGhostDist = min(scaredGhostDistList)
    # Evaluate score
    score = defaultEval(currentGameState)
    """
        Your improved evaluation here
    """
    return score


# Abbreviation
better = betterEvaluationFunction

