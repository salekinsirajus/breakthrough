import unittest
from transition import Board

class TestBoardMethods(unittest.TestCase):

    threeX3List = [['x','x','x'],
                        ['.','.','.'],
                        ['o','o', 'o'],
                        ]
    self.threeX3Board = Board(threeX3List)

    def test_is_valid(self):
        self.assertTrue(self.threeX3Board.is_valid((0,0),(1,0)))

if __name__ == '__main__':
    unittest.main()
