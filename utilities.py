import random

def u_evasive(input_state, player):
    """Utility function takes a board state as input
    and returns a value between 1 and 10 indicating
    how desirable the state is."""

    #Number of pieces remaining
    p_remaining = 0.
    
    #Check which player it is and calculate the number
    for row in input_state:
    	for column in row:              #of pieces remaining for them
    	    if player == "X":
    	        if column == "X":
                    p_remaining += 1
    	    if player == "O":
    	        if column == "O":
                    p_remaining += 1

    percentange = random.uniform(0,1)   #Generates random number between 0-1
    Num = round(percentange , 2)        #round it down to one decimal
    utility = p_remaining + Num         #utility is evasive

    print(utility)
    return utility


def u_conquerer(input_state, player):
    """Utility function takes a board state as input
    and returns a value between 1 and 10 indicating
    how desirable the state is."""

    #Number of pieces remaining
    p_remaining = 0.
    
    #Check which player it is and calculate the number
    for row in input_state:
    	for column in row:              #of pieces remaining for them
    	    if player == "X":
    	        if column == "X":
                    p_remaining += 1
    	    if player == "O":
    	        if column == "O":
                    p_remaining += 1

    percentange = random.uniform(0,1)   #Generates random number between 0-1
    Num = round(percentange , 2)        #round it down to one decimal
    utility = p_remaining + Num         #utility is evasive

    print(utility)
    return utility


def u_custom1(input_state, player):
    """Utility function takes a board state as input
    and returns a value between 1 and 10 indicating
    how desirable the state is."""

    #Number of pieces remaining
    p_remaining = 0.
    
    #Check which player it is and calculate the number
    for row in input_state:
    	for column in row:              #of pieces remaining for them
    	    if player == "X":
    	        if column == "X":
                    p_remaining += 1
    	    if player == "O":
    	        if column == "O":
                    p_remaining += 1

    percentange = random.uniform(0,1)   #Generates random number between 0-1
    Num = round(percentange , 2)        #round it down to one decimal
    utility = p_remaining + Num         #utility is evasive

    print(utility)
    return utility


def u_custom2(input_state, player):
    """Utility function takes a board state as input
    and returns a value between 1 and 10 indicating
    how desirable the state is."""

    #Number of pieces remaining
    p_remaining = 0.
    
    #Check which player it is and calculate the number
    for row in input_state:
    	for column in row:              #of pieces remaining for them
    	    if player == "X":
    	        if column == "X":
                    p_remaining += 1
    	    if player == "O":
    	        if column == "O":
                    p_remaining += 1

    percentange = random.uniform(0,1)   #Generates random number between 0-1
    Num = round(percentange , 2)        #round it down to one decimal
    utility = p_remaining + Num         #utility is evasive

    print(utility)
    return utility
