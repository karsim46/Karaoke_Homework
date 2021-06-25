import unittest
from classes.song import Song
from classes.guest import Guest
from classes.karaoke import Karaoke
from classes.rooms import Rooms

class TestKaraoke(unittest.TestCase):
# Karaoke Bar Test setup, named and 2 rooms allocated in positional arguments
    def setUp(self):
        self.karaoke = Karaoke("The Thunder-Zsolt!")
        self.room_1 = Rooms("90's")
        

# Test for bars name
    def test_karaoke_has_name(self):
        self.assertEqual("The Thunder-Zsolt!", self.karaoke.name)

# Test to add a room in the Karaoke bar
    def test_karaoke_can_add_rooms(self):
        self.karaoke.add_room(self.room_1)
        self.assertEqual(1, self.karaoke.room_count())



           
    
    

    