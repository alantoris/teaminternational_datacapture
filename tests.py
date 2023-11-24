from data_capture import DataCapture
import unittest

class TestDataCapture(unittest.TestCase):

    def test_example(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        
        self.assertEqual(stats.less(4), 2)
        self.assertEqual(stats.between(3, 6), 4)
        self.assertEqual(stats.greater(4), 2)

    def test_basics(self):
        capture = DataCapture()
        capture.add(100)
        capture.add(200)
        capture.add(300)
        capture.add(600)
        capture.add(998)
        capture.add(999)
        stats = capture.build_stats()
        
        self.assertEqual(stats.less(1000), 6)
        self.assertEqual(stats.greater(998), 1)
        self.assertEqual(stats.between(998, 1000), 2)

    def test_greater_border(self):
        capture = DataCapture()
        capture.add(1000)
        stats = capture.build_stats()
        self.assertEqual(stats.less(4), 0)
        self.assertEqual(stats.greater(999), 1)
        self.assertEqual(stats.greater(1000), 0)

    def test_lower_border(self):
        capture = DataCapture()
        capture.add(1)
        stats = capture.build_stats()
        self.assertEqual(stats.less(2), 1)
        self.assertEqual(stats.greater(999), 0)

    def test_value_error(self):
        capture = DataCapture()
        with self.assertRaises(ValueError) as _:
            capture.add(1001)
        with self.assertRaises(ValueError) as _:
            capture.add(0)


if __name__ == '__main__':
    unittest.main()
