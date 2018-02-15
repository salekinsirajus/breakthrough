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
            (a,b) = dst
            srcSym = self.get_sym(src)
            dstSym = self.get_sym(dst)
            print ("From get symbol method ", dstSym, srcSym)
            if None in [srcSym, dstSym]:
                print("Out of bound error, both negative and larger than size")
                return False
            print ("symbols from is_valid function ", dstSym, srcSym, src, dst)
            # Negative indices DOES NOT raise indexError in Python

            # source and destiation cannot be the same location
            # If the direction is horizontal, return False
            # Same applies for src = dst. This takes care of both
            if x == a:
                print("Error: src=dst")
                return False
                
            # Determine the move direction
            # If src is `O`, the valid dest direction is upwards, 
            if srcSym == self.playerO:
                if x == (a + 1):
                    pass
                else:
                    print("The direction is not upward")
                    return False
            # for `x`
            # the valid dest direction is downwards
            if srcSym == self.playerX:
                if x == (a - 1):
                    pass
                else:
                    print("The direction is not downward")
                    return False

            # The jump cannot be more than one unit forward or diagonal
            col_diff = abs(y - b)
            print ("col diff: ", col_diff)
            if col_diff > 1 or col_diff < 0:
                return False
 
            # Have the destination occupied by player of the same team
            if dstSym == srcSym:
                print("")
                return False
            else:
                return True

        except IndexError as e:
            print ("out of the board {0} {1}".format(dst, e))
            return False
    
    def get_sym(self, position):
        try:
            (x, y) = position
            for i in position:
                if i < 0:
                    return None
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

    def get_direction(self, posit):
        try:
            sym = self.get_sym(posit)
            direction = None
            if sym == 'O':
                direction = 'U'
            elif sym == 'X':
                direction = 'D'
            else:
                direction = None
            return direction
        # Need to look have a consistent exception behavior across
        # methods
        except Exception:
            return None

    def get_moves(self, posit):
        try:
            (x,y) = posit
            direction = self.get_direction(posit)
            all_moves = []
            valid_moves = []
            if direction == 'U':
                print("direction is up")
                # direction upwards, (x-1, y-1): diagonal left,
                # (x-1, y): forward, (x-1, y+1): diagonal right
                all_moves = [(x-1, y-1), (x-1, y), (x-1,y+1)]
            elif direction == 'D':
                print("direction downwards")       
                # direction upwards, (x+1, y-1): diagonal left,
                # (x+1, y): forward, (x+1, y+1): diagonal right
                all_moves = [(x+1, y-1), (x+1, y), (x+1,y+1)]
            # Think about ways to reuse this method without repeating.
            # The following else is the crucial part
            elif direction == '.':
                print ("dot")
                pass
            else:
                # last elif and this else can be combined
                pass
            # Filtering the valid moves
            # valid_moves = list(filter(lambda x: self.is_valid(posit, x) == True, all_moves))
            print("all_moves ", all_moves)
            for move in all_moves:
                if self.is_valid(posit, move) == True:
                    valid_moves.append(move)
                else:
                    print("is_valid returned False")
            return valid_moves
        except TypeError:
            print("Invalid position, TypeError raised.")
            return []

                         
brd = [['x','x'],
        ['.','.', '.'],
        ['o','o'],
        ]

b = Board(brd)
print (b.is_valid((0,1), (1,1)))
for i, r in enumerate(brd):
    for j, c in enumerate(r):
        
        print("Testing is_valid method : ", b.is_valid((i,j),(i-1,j-1)), i-1, j-1)
        print("Testing is_valid method : ", b.is_valid((i,j),(i-1,j)), i-1, j)
        print("Testing is_valid method : ", b.is_valid((i,j),(i-1,j+1)), i-1,j+1)
        print("Testing is_valid method : ", b.is_valid((i,j),(i+1,j-1)), i+1,j-1)
        print("Testing is_valid method : ", b.is_valid((i,j),(i+1,j)), i+1, j)
        print("Testing is_valid method : ", b.is_valid((i,j),(i+1,j+1)),i+1,j+1)
        
        print("Element in list ", i, j)
        print("Player: ", b.get_sym((i, j)))
        print("Direction: ", b.get_direction((i,j)))
        print("Possible moves: ", b.get_moves((i,j)))
