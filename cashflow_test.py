from cashflow import *
import unittest

class TestCashFlowFunctions(unittest.TestCase):
   def setUp(self):
      self.cf=CashFlow()
      self.x=1

   def test_unit(self):
      self.assertEqual(self.x, 1)

if __name__ == '__main__':
   unittest.main()
