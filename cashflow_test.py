from cashflow import *
import unittest

class TestCashFlowFunctions(unittest.TestCase):
   def setUp(self):
      self.cf=CashFlow()

   def test_addIce(self):
      self.cf.addIce(1000)
      self.assertEqual(self.cf.__ice__,1000)
      self.assertEqual(self.cf.__time__,0)
      self.assertEqual(self.cf.__rate__,0)

   def test_addIceTime(self):
      self.cf.addIce(1000,time=10)
      self.assertEqual(self.cf.__ice__,1000)
      self.assertEqual(self.cf.__time__,10)
      self.assertEqual(self.cf.__rate__,1000/10)

   def test_addIceRate(self):
      self.cf.addIce(1000,rate=10)
      self.assertEqual(self.cf.__ice__,1000)
      self.assertEqual(self.cf.__rate__,10)
      self.assertEqual(self.cf.__time__,1000/10)

if __name__ == '__main__':
   unittest.main()
