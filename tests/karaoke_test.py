import unittest
from classes.song import Song
from classes.guest import Guest
from classes.karaoke import Karaoke

class TestKaraoke(unittest.TestCase):
# Karaoke Bar Test setup, named and 2 rooms allocated in positional arguments
    def setUp(self):
        self.karaoke = Karaoke("Big Floppy Donkey Dick!",2)

# Test for bars name
    def test_karaoke_has_name(self):
        self.assertEqual("Big Floppy Donkey Dick!", self.karaoke.name)

           
    
    

    