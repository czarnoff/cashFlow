class CashFlow:
   __ice__=0
   __time__=0;
   __rate__=0;

   def addIce(self,iceBlock, time=0,rate=0):
      self.__ice__=iceBlock
      self.__time__=time
      self.__rate__=rate
      
      if (rate != 0):
         __time__=__ice__/__rate__
      
      if (time != 0):
         __rate__=__ice__/__time__

