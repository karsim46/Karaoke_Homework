import unittest
from classes.rooms import Rooms
from classes.guest import Guest
from classes.karaoke import Karaoke
from classes.song import Song

class TestRooms(unittest.TestCase):
    def setUp(self):
        self.rooms = Rooms("90's")