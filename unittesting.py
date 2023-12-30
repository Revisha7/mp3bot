from mp3botmain import *
from pytube import YouTube, Playlist
import unittest

class MP3BOTTESTING(unittest.TestCase):
    def setUp(self):
        self.correct_vid_link = "https://www.youtube.com/watch?v=DOTVH4AqTJ4"
        self.correct_playlist_link = "https://www.youtube.com/playlist?list=PLB4kyuAeZPjNFU5VyPomyvnOPxClackCe"
    
    def test_check_title_false_forward_slash(self):
        self.assertFalse(check_title("hey/no"))
    
    def test_check_title_false_backwards_slash(self):
        self.assertFalse(check_title("hey\what"))

    def test_check_title_true(self):
        self.assertTrue(check_title("CHILLEN"))


        
        
if __name__ == '__main__':
    unittest.main()
