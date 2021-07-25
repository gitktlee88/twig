
import unittest
from twig.devide import chunks
from twig.devide import input_validation
from twig.devide import yes_or_no

class Test_devide_chunks(unittest.TestCase):

    def test_devide_chunks1(self):
        """in case of empty array"""
        output1 = list(chunks([], 1))
        self.assertEqual(output1, [])

    def test_devide_chunks2(self):
        """in case of normal arrays"""
        output2 = list(chunks([1, 2, 2], 2))
        self.assertEqual(output2, [[1, 2], [2]])

    def test_devide_chunks3(self):
        """in case of arrays got spaces"""
        output2 = list(chunks([1   , 2, 2 ], 2))
        self.assertEqual(output2, [[1, 2], [2]])

if __name__ == '__main__':
    unittest.main()
