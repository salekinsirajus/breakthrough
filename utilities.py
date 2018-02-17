#Part 2 of the lab
import random


#Utility function takes a board state as input
#and returns a value between 1 and 10 indicating
#how desirable the state is 

def u_evasive(input_state, player):
	p_remaining = 0.  #Number of pieces remaining
	
	for row in input_state:		#Check which player it is and calculate the number
		for column in row:			#of pieces remaining for them
			if player == "X":
				if column == "X":
					p_remaining += 1
			if player == "O":
				if column == "O":
					p_remaining += 1

	percentange = random.uniform(0,1)	#Generates random number between 0-1
	Num = round(percentange , 2)		#round it down to one decimal
	utility = p_remaining + Num         #utility is evasive
	print(utility)

	

roi = [["X", "X", "X"], [".", ". ", "."], ["X", "X", "X"]]
player = "X"

u_evasive(roi, player)
