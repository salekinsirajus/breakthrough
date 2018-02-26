from transition import Board

def minimax(game_state, whose_turn, utility_func):
    # Examine the game states
    # Makes a decision based on that
    # returns a decision, i.e., a move with the help of from the minimax tree
    
    # Minimax tree analyzes (dummied by human)
    next_move = input("Enter the next move. Example: 11F\n")
    x = int(next_move[0])
    y = int(next_move[1])
    direction = next_move[2]

    return (x,y),direction

class Agent(object):
    """An agent receives a board state, i.e., a 2-d list as input at moment 
    And makes a decision based on that, and sends the next move back to the
    game controlling identity"""

    def __init__(self, current_state, turn,  utility_func, symbol):
        """Agent is initiated with a utility function associated with"""
        self.utility = utility_func
        self.state = current_state
        self.turn = turn
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol

    def update_state(self, new_state):
        """Update the state with the one passed."""
        try:
            self.state = new_state
            return True
        except Exception as e:
            print("Error updating Agent's state: {}".format(e))
            return False

    def next_move(self, current_state, turn):
        """Use the minimax tree and the utility function to figure out the next
        move.

        rtype: a tuple, a string (in that order)
        """
        # Initialize a minimax tree.
        # Pass the utility function
        # return the decision
        decision = minimax(current_state, turn, self.utility)
        
        return decision
