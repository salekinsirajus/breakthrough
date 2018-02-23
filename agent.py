# Defines an AI agent
from transition import Board

"""An agent receives a board state, i.e., a 2-d list as input at moment 
And makes a decision based on that, and sends the next move back to the
game controlling identity"""

def agent_smith(game_state):
    # Examine the game states
    # Makes a decision based on that
    # returns a decision, i.e., a move with the help of from the minimax tree
    
    # printing the current state
    # for row in game_state:
    #    for column in row:
    #        print(column, end='')
    #    print("\n")
    
    # Minimax tree analyzes (dummied by human)
    next_move = input("Enter the next move. Example: 11F")
    x = int(next_move[0])
    y = int(next_move[1])
    direction = next_move[2]

    return (x,y),direction

def utility(arg1, arg2):
    result  = arg1 + arg2
    print (result)
    return result 

class Agent(object):
    def __init__(self, utility_func):
        """An agent is initiated with a utility function associated with"""
        self.utility = utility_func

    def run_utility(self, a,b):
        r = self.utility(a,b)
        print("Ran the passed function ",r)

    def make_move(self, current_state):
        # analyze it
        # return decision
        pass

a = Agent(utility)
a.run_utility(5,6)

