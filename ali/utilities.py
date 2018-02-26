#Part 2 of the lab
import random


#Utility function takes a board state as input
#and returns a value between 1 and 10 indicating
#how desirable the state is 


#Evasive uses the number of pieces remaining for the player
#and values it based on how many is left

def evasive(input_state, player):
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
	return utility

	


def conqueror(input_state, player):
	p_remaining = 0.  #Number of pieces remaining
	
	for row in input_state:		#Check which player it is and calculate the number
		for column in row:			#of pieces remaining for them
			if player == "X":
				if column == "O":
					p_remaining += 1
			if player == "O":
				if column == "X":
					p_remaining += 1

	percentange = random.uniform(0,1)	#Generates random number between 0-1
	Num = round(percentange , 2)		#round it down to one decimal
	utility = (0 - p_remaining) + Num         #utility is conquerer
	return utility
