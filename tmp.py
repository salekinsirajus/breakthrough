from transition import Board

lst = [['X','.','.'],
        ['X','.','O'],
        ['X','.', '.']]

b = Board(lst, 'O')
#all_moves = {(0,0):['F', 'L'], (0,1):['L', 'F', 'R']}
print (b.terminal_state())


"""
for move in all_moves:
    make_move = all_moves[move]
    for each in make_move:
        new_list = b.get_current_state()
        child_board = Board(new_list, 'x')
        child_board.move(move, each)
        child_board.display_state()
        b.display_state()
"""
