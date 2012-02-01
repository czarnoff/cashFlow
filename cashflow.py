class CashFlow:
   __ice__=0
   __time__=0;
   __rate__=0;
   __pool__=0;

   def addIce(self,iceBlock, time=0,rate=0):
      self.__ice__=iceBlock
      self.__time__=time
      
      if ( rate != 0):
         self.changeRate(rate)
         
      if ( time != 0 ):
         self.changeTime(time)

   def changeRate(self,rate):
      self.__rate__=rate
      self.__time__=self.__ice__/self.__rate__
   
   def changeTime(self, time):
      self.__time__=time
      self.__rate__=self.__ice__/self.__time__

   def getPool(self,curTime=0):
      return self.__pool__+curTime*self.__rate__
