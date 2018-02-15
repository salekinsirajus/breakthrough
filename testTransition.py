import unittest
from transition import Board

class TestBoardMethods(unittest.TestCase):

    def setUp(self):
        self.threeX3List = [['x','x','x'],
                            ['.','.','.'],
                            ['o','o', 'o'],
                            ]
        self.threeX3Board = Board(self.threeX3List)
    
    #@unittest.skip("False value already tested")
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

if __name__ == '__main__':
    unittest.main()
