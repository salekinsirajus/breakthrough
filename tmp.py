from transition import Board
from minmax import Minimax_Agent
from agent import Agent
from utilities import *

lst = [["X","X","X"],
        [".",".","."],
        ["O","O", "O"]]

#b = Board(lst, 'O')
dec = Minimax_Agent(lst, "O", u_evasive)
x = dec.get_val()
print(x)
