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
      
   def test_addIceBoth(self):
      self.cf.addIce(1000,rate=12,time=14)
      self.assertEqual(self.cf.__ice__,1000)
      self.assertEqual(self.cf.__rate__,1000/14)
      self.assertEqual(self.cf.__time__,14)
   
   def test_changeRate(self):
      self.cf.addIce(1000)
      self.cf.changeRate(12);
      self.assertEqual(self.cf.__ice__,1000)
      self.assertEqual(self.cf.__rate__,12)
      self.assertEqual(self.cf.__time__,1000/12)
   
   def test_changeTime(self):
      self.cf.addIce(1000)
      self.cf.changeTime(12);
      self.assertEqual(self.cf.__ice__,1000)
      self.assertEqual(self.cf.__rate__,1000/12)
      self.assertEqual(self.cf.__time__,12)

if __name__ == '__main__':
   unittest.main()
