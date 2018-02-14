# Define the transition function

class Board(object):
    
    def __init__(self, list2d):
        self.board = list2d
        self.playerO = 'O'
        self.playerX = 'X'
    
    def is_valid(self, src, dst):
        '''Checking to see if it's possible to move from src to dst.
        Position is indicated by a tuple of the form (row, column).
        NB: It works only when the `O` player moves UP and `X` moves
        down'''
        # check board bound
        # check whether the same kind or the other (opponent or own)
        try:
            (x,y) = src
            dstSym = self.board[x][y]
            (a,b) = dst
            srcSym = self.board[a][b]
            dstSym = dstSym.upper() 
            srcSym = srcSym.upper()

            # Determine the move direction
            # If src is `O`, the valid dest direction is upwards, 
            if srcSym == self.playerO:
                if x == (a - 1):
                    pass
                else:
                    return False 
            # for `x`
            # the valid dest direction is downwards
            if srcSym == self.playerX:
                if x == (a + 1):
                    pass
                else:
                    return False 
            # Have the destination occupied by player of the same team
            if dstSym == srcSym:
                return False
            else:
                return True

        except IndexError:
            return False
    
    def get_sym(self, position):
        try:
            (x, y) = position
            sym = self.board[x][y].upper()
            if sym == self.playerO:
                return 'O' # or self.playerO
            elif sym == self.playerX:
                return 'X'
            elif sym == '.':
                return '.'
            else:
                return None
        except IndexError:
            return None


    def get_moves(self, posit):
        pass
     
brd = [['x','o'],
        ['.','.'],
        ['o','o'],
        ]

b = Board(brd)
print (b.is_valid((0,1), (1,1)))
for i, r in enumerate(brd):
    for j, c in enumerate(r):
        print(b.get_sym((i, j)))
