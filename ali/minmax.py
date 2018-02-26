from transition import *
from utilities import *
from Tree import *
import copy


class Minimax_Agent(object):
	def __init__(self, state, turn, utility_func):
		self.utility_func = utility_func
		self.state = state
		self.turn = turn   #Can be either "X" or "O"
		self.min_val = 9999999999999
		self.max_val = -999999999999
		

	def get_val(self):
		
		board = Board(self.state, self.turn)
		root = Node(self.state)

		moves_dic = board.all_moves(turn)

		source = ()
		direction = "" 
		result = []
	
		for key in moves_dic:			#The set of keys in the dictionary
			
			val = moves_dic[key]		#The set of values that are "R", "L", "F"

			for dis in val:
				new_state = copy.deepcopy(self.state)
				child_board = Board(new_state, self.turn)
				child_board.move(key, dis)			#For the possible moves, make each one and create an instance of the state


				child = Node(new_state)
				root.add_child(child)				#add it as the child of the node

				self.set_utility(child)				#Get a utility for the node's children, and assign the minimum to the child
				
				if child.utility > self.max_val:		#Get the maximum and pass to the root
					self.max_val = child.utility
					direction = dis
					source = key

		
		result.append(source)
		result.append(direction)
		return result
		



	def set_utility(self,node_child):

		node_child = node_child
		sec_board = Board(node_child.state, self.turn)

		if self.turn == "X":
			moves_dic2 = sec_board.all_moves("O")
		elif self.turn == "O":
			moves_dic2 = sec_board.all_moves("X")


		for key in moves_dic2:						#Set of possible moves for each child of the node tree
			val = moves_dic2[key]
				
			for dis in val:
				gnew_state = copy.deepcopy(node_child.state)

				gchild_board = Board(gnew_state)
				gchild_board.move(key, dis)
		
				utility = self.utility_func(gnew_state, turn)
				if utility < self.min_val:				#Take the minimum of the nodes and assign to the children
					self.min_val = utility

		node_child.utility = utility



state = [["X","X", "X"], [".",".", "."], ["O","O", "O"]]
turn = "X"

board = Minimax_Agent(state, turn, evasive)
x = board.get_val()
print(x)

