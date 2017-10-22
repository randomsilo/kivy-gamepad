import unittest
import sys
sys.path.append("../")
from gamepad.core import IGamePad, CGamePad

class TestGamePad(unittest.TestCase):
    """ TestGamePad tests ABC implementation """
    def setUp(self):
        pass

    def test_func1(self):
        """ func1 function confirmation """
        self.assertTrue(true)

if __name__ == '__main__':
    unittest.main()
