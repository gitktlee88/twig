
import unittest
from twig.devide import chunks

class Test_divide_chunks(unittest.TestCase):

    def test_divide_chunks1(self):
        output1 = list(chunks([], 1))
        self.assertEqual(output1, [])
        #print(os.path.abspath(os.getcwd()))

    def test_divide_chunks2(self):
        output2 = list(chunks([1, 2, 2], 2))
        self.assertEqual(output2, [[1, 2], [2]])
        #print(os.path.dirname(os.path.abspath(__file__)))


if __name__ == '__main__':

    unittest.main()
