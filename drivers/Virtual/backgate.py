import visa
import instruments

class Backgate(VirtualInstrument):
    def __init__(self,name,baseintrument,channelno):
        VirtualInstrument.__init__(self, name,baseinstrument)
        self.status='Ready'
        self.info["Gain"]=20.0
        self.info["Channel #"]=channelno
        self.chan=channelno
        if isinstance(baseintrument,Stanford830):
        	self.setbg=baseintrument.set_aux_output
        	self.getbg=baseintrument.get_aux_output
        elif isinstance(baseintrument,NIDAQ):
        	self.set=None
        	pass
        self.B=0.0

   	@property
   	def gain():
   		return self.info["Gain"]

   	@gain.setter
   	def conversionfactor_V2B(value):
        self.info["Gain"]=value

    def set_backgate(value):
    	self.setbg(self.chan,value*self.gain)
    	pass

    def get_backgate():
    	return self.getbg(self.chan)*self.gain