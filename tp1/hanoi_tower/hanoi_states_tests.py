import unittest

from hanoi_states import StatesHanoi

class StatesHanoiTests(unittest.TestCase):

    def test_eq(self):
        state1 = StatesHanoi([3,2,1], [],[], max_disks=3)
        state2 = StatesHanoi([3,2,1], [],[], max_disks=3)
        self.assertEqual(state1, state2)

if __name__ == 'main':
    unittest.main()
