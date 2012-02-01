import unittest

class TestCashFlowFunctions(unittest.TestCase):
   def setUp(self):
      self.x=1

   def test_unit(self):
      self.assertEqual(self.x, 1)

if __name__ == '__main__':
   unittest.main()
