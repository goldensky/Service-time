import unittest

from simple_task_np import totalTime


class TestTotalTime(unittest.TestCase):
    def test_total_time1(self):
        self.assertEqual(totalTime([], 1), 0)

    def test_total_time2(self):
        self.assertEqual(totalTime([], 5), 0)

    def test_total_time3(self):
        self.assertEqual(totalTime([5], 1), 5)

    def test_total_time4(self):
        self.assertEqual(totalTime([5, 4, 3], 1), 12)

    def test_total_time5(self):
        self.assertEqual(totalTime([10, 2, 3, 3], 2), 10)

    def test_total_time6(self):
        self.assertEqual(totalTime([2, 3, 10], 2), 12)

    def test_total_time7(self):
        self.assertEqual(totalTime([5], 2), 5)

    def test_total_time8(self):
        self.assertEqual(totalTime([5, 4], 6), 5)
        
    def test_total_time9(self):
        self.assertEqual(totalTime([10, 2, 3, 5, 8, 4, 3, 7, 1, 2], 4), 14)
        
if __name__ == '__main__':
    unittest.main()

