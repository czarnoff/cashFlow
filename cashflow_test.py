from cashflow import *
import unittest

class TestCashFlowFunctions(unittest.TestCase):
   def setUp(self):
      self.cf=CashFlow()
      self.x=1

   def test_unit(self):
      self.cf.addIce(1000)
      self.assertEqual(self.cf.__ice__,1000)

if __name__ == '__main__':
   unittest.main()
