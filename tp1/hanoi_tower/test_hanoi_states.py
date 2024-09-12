import unittest

from hanoi_states import StatesHanoi

class StatesHanoiTests(unittest.TestCase):

    def test_eq_states_are_eq(self):
        state1 = StatesHanoi([3,2,1], [],[], max_disks=3)
        state2 = StatesHanoi([3,2,1], [],[], max_disks=3)
        self.assertEqual(state1, state2)
    def test_different_states_are_not_eq(self):
        state1 = StatesHanoi([3,2], [1],[], max_disks=3)
        state2 = StatesHanoi([3,2,1], [],[], max_disks=3)
        self.assertNotEqual(state1, state2)
    def test(self):
        explored = [StatesHanoi([3,2], [1],[], max_disks=3), StatesHanoi([3,2,1], [],[], max_disks=3)]
        explored_state = StatesHanoi([3,2], [1],[], max_disks=3)
        self.assertTrue(explored_state in explored)
        not_explored_state = StatesHanoi([3,2], [],[1], max_disks=3)
        self.assertFalse(explored_state not in explored)
if __name__ == 'main':
    unittest.main()
