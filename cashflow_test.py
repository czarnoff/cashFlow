from cashflow import *
import unittest

class TestCashFlowFunctions(unittest.TestCase):
   def setUp(self):
      self.cf=CashFlow()
      self.x=1

   def test_addIce(self):
      self.cf.addIce(1000)
      self.assertEqual(self.cf.__ice__,1000)

   def test_addIceTime(self):
      self.cf.addIce(1000,time=10)
      self.assertEqual(self.cf.__ice__,1000,time=10)

if __name__ == '__main__':
   unittest.main()
