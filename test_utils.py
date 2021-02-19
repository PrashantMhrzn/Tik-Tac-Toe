import unittest
from Utils.utils import *


class TestUtils(unittest.TestCase):

    def test_valid(self):
        a[0][0] = 'X'
        a[2][2] = 'O'
        self.assertEqual(valid(a[0][0]), False)
        self.assertEqual(valid(a[2][2]), False)
        self.assertEqual(valid(a[0][1]), True)
        a[0][0] = ' '
        self.assertEqual(valid(a[0][0]), True)
        self.assertNotEqual(valid(a[0][0]), False)
        self.assertNotEqual(valid(a[0][0]), None)

    def test_win(self):
        a[0][0] = 'O'
        a[0][1] = 'O'
        a[0][2] = 'O'
        self.assertEqual(win(), True)
        self.assertNotEqual(win(), False)
        self.assertNotEqual(win(), None)
        a[0][2] = 'X'
        self.assertEqual(win(), None)
        self.assertNotEqual(win(), False)
        self.assertNotEqual(win(), True)

    def test_player_turn(self):
        player_turn(1)
        a[1][0] = 'O'
        self.assertListEqual(a[0], a[1])
        self.assertIn('O', a[1])
        self.assertIn('O', a[0])

    def test_player_invalid(self):
        self.assertEqual(player_invalid(),
                         '\nPlayer move invalid turn skipped!')
        self.assertNotEqual(player_invalid(), None)
        self.assertNotEqual(player_invalid(), True)
        self.assertNotEqual(player_invalid(), False)
        self.assertIn('\n', player_invalid())

    def test_print_board(self):
        self.assertEqual(print_board(a), None)
        self.assertNotEqual(print_board(a), True)
        self.assertNotEqual(print_board(a), False)


if __name__ == '__main__':
    unittest.main()
