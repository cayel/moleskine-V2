import unittest
from artist import Artist
from release import Release
from release_list import ReleaseList

class TestReleaseList(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Nick Cave & The Bad Seeds", 1, "Australie")
        self.release1 = Release(1, self.artist, "Tender Prey", "1988-01-01")
        self.release2 = Release(2, self.artist, "The Good Son", "1990-01-01")
        self.release3 = Release(3, self.artist, "Let Love In", "1994-01-01")    
        self.release_list = ReleaseList(1, "Les 10 meilleurs albums de Nick Cave", "La liste des 10 meilleurs albums de Nick Cave", True)

    def test_add_release(self):
        result = self.release_list.add_release(self.release1)
        self.assertTrue(result)
        self.assertEqual(len(self.release_list.releases), 1)
        self.assertEqual(self.release_list.releases[0], self.release1)

    def test_add_duplicate_release(self):
        self.release_list.add_release(self.release1)
        result = self.release_list.add_release(self.release1)
        self.assertFalse(result)
        self.assertEqual(len(self.release_list.releases), 1)

    def test_str(self):
        self.release_list.add_release(self.release1)
        self.release_list.add_release(self.release2)
        self.assertEqual(str(self.release_list), "(1) - Les 10 meilleurs albums de Nick Cave : 2 releases")

    def test_release_exists(self):
        self.release_list.add_release(self.release1)
        self.release_list.add_release(self.release2)
        self.assertTrue(self.release_list.release_exists(1))
        self.assertTrue(self.release_list.release_exists(2))
        self.assertFalse(self.release_list.release_exists(3))

    def test_get_release_rank(self):
        self.release_list.add_release(self.release1)
        self.release_list.add_release(self.release2)
        self.assertEqual(self.release_list.get_release_rank(self.release2), 2)

    def test_add_release_rank(self):
        self.release_list.add_release(self.release1)
        self.release_list.add_release(self.release2)
        self.release_list.add_release_rank(self.release3, 2)
        self.assertEqual(self.release_list.get_release_rank(self.release3), 2)
        self.assertEqual(self.release_list.get_release_rank(self.release2), 3)
    
    def test_clear_releases(self):
        self.release_list.add_release(self.release1)
        self.release_list.add_release(self.release2)
        self.release_list.clear_releases()
        self.assertEqual(len(self.release_list.releases), 0)

if __name__ == '__main__':
    unittest.main()