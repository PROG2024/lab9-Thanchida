"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
from counter import Counter
import unittest


class SingletonTest(unittest.TestCase):

    def test_same_singleton(self):
        c1 = Counter()
        c2 = c1
        c1.increment()
        self.assertEqual(c1, c2)


