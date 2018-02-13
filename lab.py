

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