import unittest
from exercise2 import LotteryContainer


class TestLotteryContainer(unittest.TestCase):

    def setUp(self):
        self.c = LotteryContainer(10)

    def test_init(self):
        self.assertEqual(len(self.c.balls), 10)
        self.assertEqual(self.c.balls, [i for i in range(1, 10+1)])

    def test_reset(self):
        self.c.picking(2)
        self.assertEqual(len(self.c.balls), 8)

        self.c.reset()
        self.assertEqual(len(self.c.balls), 10)
        self.assertEqual(self.c.balls, [i for i in range(1, 10+1)])

    def test_error_picking(self):
        with self.assertRaises(ValueError):
            self.c.picking(-5)

        with self.assertRaises(ValueError):
            self.c.picking(12)

    def test_picking(self):
        picking_list = self.c.picking(2)
        self.assertEqual(len(picking_list), 2)

        all_balls = picking_list + self.c.balls
        all_balls.sort()
        self.assertEqual(all_balls, [i for i in range(1, 10+1)])

    def test_picking_sort_number(self):
        picking_list = self.c.picking(5, True)
        
        start_number = 0
        for number in picking_list:
            self.assertTrue(start_number < number)
            start_number = number
        

if __name__ == '__main__':
    unittest.main()
