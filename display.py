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
