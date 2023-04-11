import unittest

from models.album import Album

class TestAlbum(unittest.TestCase):
    
    def setUp(self):
        self.album = Album("This Place Will Be Your Tomb", "Metal", 1)

def test_album_has_name(self):
    self.assertEqual("This Place Will Be Your Tomb", self.album.name)


