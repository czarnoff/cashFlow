class CashFlow:
   __ice__=0
   __time__=0;
   __rate__=0;

   def addIce(self,iceBlock, time=0,rate=0):
      self.__ice__=iceBlock
      self.__time__=time
      self.__rate__=rate
      
      if (time == 0 and rate != 0):
         self.__time__=self.__ice__/self.__rate__
      
      if (time != 0 and rate == 0):
         self.__rate__=self.__ice__/self.__time__

