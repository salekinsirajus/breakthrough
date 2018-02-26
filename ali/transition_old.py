# Define the transition function
import traceback
import sys

class Board(object):
    
    def __init__(self, list2d):
        self.board = list2d
        self.playerO = 'O'
        self.playerX = 'X'


    '''Checking to see if it's possible to move from src to dst.
        Position is indicated by a tuple of the form (row, column).
        NB: It works only when the `O` player moves UP and `X` moves
        down'''



    def get_current_state(self):
        return self.board

    def is_valid(self, src, dst):

        try:
            (x,y) = src
            (a,b) = dst
            srcSym = self.get_sym(src)
            dstSym = self.get_sym(dst)
            
            # CP1(CheckPoint1): Invalid Index, negative and outside of list
            if None in [srcSym, dstSym]:
                #print("Out of bound error, both negative and larger than size")
                return False
            #print ("symbols from is_valid function ", dstSym, srcSym, src, dst)

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
            #print ("col diff: ", col_diff)
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



    '''Prints out the state passed to this function on the terminal.'''
        # check if it's a 2-d list

    def displayState(self):
        
        for row in self.board:
            for column in row:
                print(column, end=' ')
            print("\n")




    
    def get_sym(self, position):
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


    def get_positions(self, player):
        """Returns all the position occupied by a certain player"""
        try:
            if player not in [self.playerX, self.playerO]:
                print("Incorrect marker passed for player's symbol.")
                raise ValueError
                traceback.print_stack(file=sys.stdout)

            positions_found = []
            for x, row in enumerate(self.board):
                for y, column in enumerate(row):
                    if column == player:
                        positions_found.append((x,y))
            
            return positions_found

        except Exception as e:
            print(e)
            traceback.print_stack(file=sys.stdout)


    def get_moves(self, posit):
        try:
            (x,y) = posit
            direction = self.get_direction(posit)
            all_moves = []
            valid_moves = []
            if direction == 'U':
                #print("direction is up")
                # direction upwards, (x-1, y-1): diagonal left,
                # (x-1, y): forward, (x-1, y+1): diagonal right
                all_moves = [(x-1, y-1), (x-1, y), (x-1,y+1)]
            elif direction == 'D':
                #print("direction downwards")       
                # direction upwards, (x+1, y-1): diagonal left,
                # (x+1, y): forward, (x+1, y+1): diagonal right
                all_moves = [(x+1, y-1), (x+1, y), (x+1,y+1)]
            # Think about ways to reuse this method without repeating.
            # The following else is the crucial part
            elif direction == '.':
                #print ("dot")
                pass
            else:
                # last elif and this else can be combined
                pass
            # Filtering the valid moves
            # valid_moves = list(filter(lambda x: self.is_valid(posit, x) == True, all_moves))
            #print("all_moves ", all_moves)
            for move in all_moves:
                if self.is_valid(posit, move) == True:
                    valid_moves.append(move)
                #else:
                    #print("is_valid returned False")
            return valid_moves
        except TypeError:
            print("Invalid position, TypeError raised.")
            return None








    def all_moves(self, player):
        """Returns a data structure full of possible moves by a player"""
        
        all_positions = self.get_positions(player)
        movement_dict = {}
        #print(all_positions)
        for position in all_positions:
            # A single source
            (x,y) = position
            # Is this moving upwards or downwards
            flow = self.get_direction(position)
            # All the moves for this position in a list
            moves_for_this_position = self.get_moves(position)
            #print(moves_for_this_position)
            for i, move in enumerate(moves_for_this_position):
                (x1, y1) = move
                if flow == 'U':
                    if y1 == y + 1:      # to the right
                        # Replacing the destination with letter
                        moves_for_this_position[i] = 'R'
                    elif y1 == y - 1:      # to the left
                        # Replacing the destination with letter
                        moves_for_this_position[i] = 'L' 
                    elif y1 == y:      # to forward
                        # Replacing the destination with letter
                        moves_for_this_position[i] = 'F'
                    else:
                        print("Sth wrong in the get_moves function")

                elif flow == 'D':
                    if y1 == y - 1:      # to the right
                        # Replacing the destination with letter
                        moves_for_this_position[i] = 'R'
                    elif y1 == y + 1:      # to the left
                        # Replacing the destination with letter
                        moves_for_this_position[i] = 'L' 
                    elif y1 == y:      # to forward
                        # Replacing the destination with letter
                        moves_for_this_position[i] = 'F'
                    else:
                        print("Sth wrong in the get_moves function")
                else:
                    print("Direction is neither up nor down. Invalid")

            movement_dict[position] = moves_for_this_position

        return movement_dict





    def move(self, posit, turn):
        '''Move to the direction =['R','L','F'] asked to from position passed'''
        # print("Come inside the function move") 
        try:
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
                
            return True

        except Exception as e:
            # Anything goes wrong
            print(e)
            return False


    


#Takes a state as input, and checks if it is a game ending
#state. 1: One of the players pieces are out
#    2: One of the players piece reached that last row


    def terminal_state(self):
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
            print("Player 1 won. Reached last row")
        if player2 is True:
            print("Player 2 won. Reached last row")


        if len(p1list) == 0:
            print("Player 2 won. Other player's pieces out")
        if len(p2list) == 0:
            print("Player 1 won. Other player's pieces out")

        else:
            return None


    def example(self):
        x = {(0,1):["F","R"], (0,0):["L","F"]}
        return x


"""

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

"""
