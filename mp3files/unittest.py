import mp3botmain
import unittest

class Project4GameMechanicsTestingWithSameSetUp(unittest.TestCase):
    def setUp(self):
        self.correct_vid_link = "https://www.youtube.com/watch?v=DOTVH4AqTJ4"
        self.correct_playlist_link = "https://www.youtube.com/playlist?list=PLB4kyuAeZPjNFU5VyPomyvnOPxClackCe"
    
    def test_create_empty_board(self):
        self.game_field.make_empty_board()
        self.assertEqual([['0','0','0','0'],['0','0','0','0'],['0','0','0','0'],['0','0','0','0']],self.game_field.get_board())

    

"""class Project4GameMechanicsTestingWithDifferentSetUp(unittest.TestCase):
    def test_creating_board_with_too_little_rows_fails(self):
        with self.assertRaises(game_mechanics.InvalidNumbers):
            game_field = game_mechanics.GameField(1,5)

    def test_creating_board_with_too_little_columns_fails(self):
        with self.assertRaises(game_mechanics.InvalidNumbers):
            game_field = game_mechanics.GameField(5,1)
        
    def test_creating_board_with_too_little_rows_and_columns_fails(self):
        with self.assertRaises(game_mechanics.InvalidNumbers):
            game_field = game_mechanics.GameField(1,1)"""
        
        
if __name__ == '__main__':
    unittest.main()
