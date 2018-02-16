import unittest
from transition import Board

class TestBoardMethods(unittest.TestCase):

    def setUp(self):
        self.threeX3List = [['x','x','x'],
                            ['.','.','.'],
                            ['o','o', 'o'],
                            ]
        self.threeX3Board = Board(self.threeX3List)
    
    # @unittest.skip("False value already tested")
    def test_is_valid_false(self):
        pairs_false = [[(0,0),(0,0)], # False, src = dst
                        [(0,0),(0,2)],   # False, two units, same row
                        [(0,0),(-1,0)],  # False, out of index
                        [(0,0),(0,1)],   # False, same row
                        [(0,0),(1,-1)],   # False, out of index
                        [(0,0),(1,2)],   # False, moving two units
                        [(0,0),(2,0)],   # False, moving two units
                        [(0,0),(2,2)],   # False, moving two units
                        [(0,0),(11,11)]   # False, out of index
                        ]
        for pair in pairs_false:
            with self.subTest(pair=pair):
                self.assertIs(self.threeX3Board.is_valid(pair[0],pair[1]), False)

    def test_is_valid_true(self):
        pairs_true = [[(0,0),(1,0)], # True, forward
                        [(0,0),(1,1)],   # True, diagonal left
                        [(0,1),(1,0)],  # True, diagonal left
                        [(0,1),(1,1)],   # True, forward
                        [(0,1),(1,2)],   # True, diagonal right
                        [(2,0),(1,0)],   # True, forward
                        [(2,0),(1,1)],   # True, diagonal right
                        [(2,2),(1,2)],   # False, forward
                        [(2,1),(1,0)]   # True, diagonal left
                        ]
        for pair in pairs_true:
            with self.subTest(pair=pair):
                self.assertTrue(self.threeX3Board.is_valid(pair[0],pair[1]))

    def test_get_moves_returns_empty(self):
        # For point where the returned list will be empty
        dots = [(1,0),     # [], no player, column-0
                (1,1),     # [], no player, middle
                (1,2)      # [], no player, rightmost column
                    ] 

        for each in dots:
            with self.subTest(each=each):
                self.assertEqual(self.threeX3Board.get_moves(each), [])

    def test_get_moves_for_playerO(self):
        # For point where the returned list will be empty
        dots = [(2,0),     # [], playerO, column-0
                (2,1),     # [], playerO, middle
                (2,2)      # [], playerO, rightmost column
                    ] 
        self.assertEqual(self.threeX3Board.get_moves(dots[0]), [(1,0),(1,1)])
        self.assertEqual(self.threeX3Board.get_moves(dots[1]), [(1,0),(1,1),(1,2)])
        self.assertEqual(self.threeX3Board.get_moves(dots[2]), [(1,1),(1,2)])

    def test_get_moves_for_playerX(self):
        # For point where the returned list will be empty
        dots = [(0,0),     # [], playerX, column-0
                (0,1),     # [], playerX, middle
                (0,2)      # [], playerX, rightmost column
                    ] 
        self.assertEqual(self.threeX3Board.get_moves(dots[0]), [(1,0),(1,1)])
        self.assertEqual(self.threeX3Board.get_moves(dots[1]), [(1,0),(1,1),(1,2)])
        self.assertEqual(self.threeX3Board.get_moves(dots[2]), [(1,1),(1,2)])
            
if __name__ == '__main__':
    unittest.main()
