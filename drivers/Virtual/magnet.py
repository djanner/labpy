import visa
import instruments

class Magnet(VirtualInstrument):
    def __init__(self,name,baseintrument,channelno):
		    VirtualInstrument.__init__(self, name,baseinstrument)
        self.status='Ready'
        self.info["Conversion Factor [B/V]"]=0.0
        self.info["Channel #"]=channelno
        self.chan=channelno
        if isinstance(baseintrument,Stanford830):
        	self.setB=baseintrument.set_aux_output
        	self.getB=baseintrument.get_aux_output
        elif isinstance(baseintrument,NIDAQ):
        	self.set=None
        	pass
        self.B=0.0

   	@property
   	def conversionfactor_V2B():
   		return self.info["Conversion Factor [B/V]"]

   	@conversionfactor_V2B.setter
   	def conversionfactor_V2B(value):
        self.info["Conversion Factor [B/V]"]=value

    def setB_field(value):
    	self.setB(self.chan,value*self.conversionfactor_V2B)
    	pass

    def get_Bfield():
    	return self.getB(self.chan)*self.conversionfactor_V2B
