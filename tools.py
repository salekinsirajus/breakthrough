

def initial_state(rows, columns, prows):
	big_list = []			#The 2D array holding all the elements

	for i in range(rows - prows):
		if i <= (prows - 1):
			small_list = ["X"] * columns
			big_list.append(small_list)

		else:
			small_list = ["."] * columns
			big_list.append(small_list)

	for i in range (prows):
		small_list = ["O"] * columns
		big_list.append(small_list)

	return big_list




def displayState(board):
    '''Prints out the state passed to this function on the terminal.'''
    # check if it's a 2-d list
    for row in board:
        for column in row:
            print(column, end=' ')
        print("\n")
    print("Done")

brd = [['x','o'],
        ['.','.'],
        ['o','o'],
        ]

displayState(brd)



"""
This is the move generator given an intial position, 
destination and whose turn it is, it will make a single
move from source to destination. 

"""                     

def single_move (src_position, dest_position, turn):
    x = dest_position[0]
    y = dest_position[1]

    src_x = src_position[0]
    src_y = src_position[1]

    #Check whose turn it is
    if turn == "X":  
        if x == src_x + 1 and y == src_y - 1:        #direction is leftbottom
            return src_position[0] + 1, src_position[1] - 1
        if x == src_x + 1 and y == src_y:			#direction is bottom
        	return src_position[0] + 1, src_position[1]
        if x == src_x + 1 and src_y + 1:			#direction is rightbottom
        	return src_position[0] + 1, src_position[1] + 1

    if turn == "O":
    	if x == src_x - 1 and y == src_y - 1:        #direction is lefttop
            return src_position[0] - 1, src_position[1] - 1
        if x == src_x - 1 and y == src_y:			#direction is top
        	return src_position[0] - 1, src_position[1]
        if x == src_x - 1 and src_y + 1:			#direction is righttop
        	return src_position[0] - 1, src_position[1] + 1




        



        





source = (1,1)
destination  = (2,0)
turn = "X"

result = single_move(source, destination, turn)
print(result)



def terminal_state(input_list):

	player1 = False
	player2 = False

	p1list = []
	p2list = []

	
	for row in input_list:
		for element in row:
	#First case, when one of the players pieces is all out
			if element == "X":
				p1list.append(element)
			if element == "O":
				p2list.append(element)
	
	#Second case, when one of the pieces move to the last row
	for element in input_list[-1]:
		if element == "X":
			player1 = True
	for element in input_list[0]:
		if element == "O":
			player2 = True

	#Print the result for both cases 

	if player1 is True:
		print("Game Over. Player 1 won")
	if player2 is True:
		print("Game Over. Player 2 won")

	if len(p1list) == 0:
		print("Game Over. Player 2 won")
	if len(p2list) == 0:
		print("Game Over. Player 1 won")


roi = [["X", "X", "X"], [".", ". ", "."], ["X", "X", "X"]]
terminal_state(roi)