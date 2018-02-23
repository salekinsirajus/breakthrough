# This is where the game runs.
# The agents interact with the Board here
# The Board make sure to enforce the game rules.
#from transition import Board
from agent import agent_smith

#class Game(Borad):
#    """Provide a stage for the Breakthrough game to run."""
#    def __init__(self):
#        pass


from transition import Board

lst = [['X','X','X','X'], 
        ['.','.','.','.'], 
        ['.','.','.','.'], 
        ['O','O','O','O']]
Smith = 'X'
John = 'O'
# initialize the Board
board = Board(lst, Smith)

while True:
    # retrieve the current state
    curr = board.get_current_state()
    # show the current state
    board.display_state()
    whose_turn = board.get_turn()
    # pass it to the agent whose turn
    if whose_turn == Smith:
        print("Smiths turn X")
    elif whose_turn == John:
        print("Johns Turn O")
    else:
        print("Something wrong with the board")
    smiths_move = agent_smith(curr)
    print(smiths_move)
    if smiths_move == []:
        print("end game")
        break
    # perform the turn. Try again if it's wrong turn
    board.move(smiths_move[0], smiths_move[1])
    # show the new state
    board.display_state()

