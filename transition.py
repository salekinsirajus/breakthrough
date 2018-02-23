# Define the transition function
# Modified from 'turn functionality commit'

class Board(object):
    
    def __init__(self, list2d, cursor_at):
        self.board = list2d
        self.playerO = 'O'
        self.playerX = 'X'
        self.cursor_at = cursor_at

    def is_valid(self, src, dst):
        """Checking to see if it's possible to move from src to dst.
        Position is indicated by a tuple of the form (row, column).
        NB: It works only when the `O` player moves UP and `X` moves
        down"""

        try:
            (x,y) = src
            (a,b) = dst
            srcSym = self.get_sym(src)
            dstSym = self.get_sym(dst)
            
            # CP1(CheckPoint1): Invalid Index, negative and outside of list
            if None in [srcSym, dstSym]:
                print("Out of bound error, both negative and larger than size")
                return False
            print ("symbols from is_valid function ", dstSym, srcSym, src, dst)

            # CP2: source /= destination, same row movement not permitted either
            if x == a:
                print("Error: src=dst")
                return False
            
            # CP3: Wrong Move Direction    
            # For player `O`, the valid dest direction is upwards
            if srcSym == self.playerO:
                if x == (a + 1):
                    pass
                else:
                    print("The direction is not upward")
                    return False
            # For `X` the valid dest direction is downwards
            if srcSym == self.playerX:
                if x == (a - 1):
                    pass
                else:
                    print("The direction is not downward")
                    return False

            # CP4: Movement of more than one unit
            # The jump cannot be more than one unit forward or diagonal
            col_diff = abs(y - b)
            print ("col diff: ", col_diff)
            if col_diff > 1 or col_diff < 0:
                return False
            
            # CP5: Occupied by the same player
            # A move can be made when the dst is either `.` or enemy
            if dstSym == srcSym:
                print("")
                return False
            else:
                return True

        except IndexError as e:
            print ("out of the board {0} {1}".format(dst, e))
            return False


    def display_state(self):
        """Prints out the state passed to this function on the terminal."""
        for row in self.board:
            for column in row:
                print(column, end=' ')
            print("\n")
        print("Done")


    
    def get_sym(self, position):
        """Returns the symbol/character at position passed. 
           Returns None if it's neither `O` nor `X`"""
        try:
            (x, y) = position
     
            # Negative indices DOES NOT raise indexError in Python
            # Board contains only positive (x,y) values.
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

    
    def terminal_state(self):
        """Check if current state is a terminal one."""
        # Need to change the variable names to make things more consistent
        player1 = False
        player2 = False

        p1list = []
        p2list = []


        for row in self.board:
            for element in row:
        #First case, when one of the players pieces is all out
                if element is self.playerX:
                    p1list.append(element)
                if element is self.playerO:
                    p2list.append(element)

        #Second case, when one of the pieces move to the last row
        for element in self.board[-1]:
            if element == "X":
                player1 = True
        for element in self.board[0]:
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
    
    def switch_turn(self):
        if self.cursor_at == self.playerO:
            self.cursor_at = self.playerX
        if self.cursor_at == self.playerX:
            self.cursor_at = self.playerO

        return self.cursor_at
            

    def move(self, posit, turn):
        """Move to the direction =['R','L','F'] asked to from position passed"""
        # print("Come inside the function move") 
        try:
            # Check if it's current players turn
            if self.cursor_at != self.get_sym(posit):
                print("Not your turn yet. Illegal try.")
                return False

            # print("Come inside the try block")
            # Identify the destination
            (x, y) = posit
            # Initialize the destination tuple
            a = 99999999
            b = 99999999
            flow = self.get_direction(posit)
            # print("The positon passed ({},{})".format(x,y))
            # print("The dest before assignment = ({},{})".format(a,b))
            # print("The flow is: ", flow)
            # print("The turn is: ", turn)
            # Figuring out the dest X (=a) value
            if flow == 'U':
                a = x - 1                
                # Figuring out the dest Y (=b) value
                if turn == 'R':
                    b = y + 1
                elif turn == 'L':
                    b = y - 1
                elif turn == 'F':
                    b = y
                else:
                    print ("Invalid move direction")
                    return False
            elif flow == 'D':
                a = x + 1

                if turn == 'R':
                    b = y - 1
                elif turn == 'L':
                    b = y + 1
                elif turn == 'F':
                    b = y
                else:
                    print ("Invalid move direction")
                    return False

            else:       
                # When get_direction == None, return Failure
                return False
            
            # validate move
            dest = (a,b)
            if self.is_valid(posit, dest) != True:
                return False
            
            # Move the current player to the dest, assign `.` at empty spot
            #(a, b) = dest
            self.board[a][b] = self.board[x][y]
            self.board[x][y] = '.'
            
            # Flip the turn to the other player
            self.switch_turn()
            return True

        except Exception as e:
            # Anything goes wrong
            print(e)
            return False
            
