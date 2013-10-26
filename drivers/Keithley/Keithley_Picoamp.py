import visa
from instruments import Instrument, Configuration, Parameter

class Keithley_Picoamp(Instrument):
    
    #Initialization
    
    def __init__(self,name,address):
        try:
            self._inst=visa.instrument(address)
        except:
            print "ERROR! Failed to initialize VISA instrument"
            self._inst=None
        if not(self._inst==None):
            self._address=address
        
        logging.info(__name__ + ' : Initializing instrument')
        Instrument.__init__(self, name, address)
        self.status='Ready'
        
    ############## Constants ##############
    _address = None
    _inst = None

    ############## Functions ##############    
    def convert(self,val,type):
        if type=='float':
            y=float(val)
        if type=='int':
            y=int(val)
        if type=='string':
            y=str(val)
        return y 
        
    def ask(self,command):
        return self._inst.ask(command) 
        
    def write(self,command):
        return self._inst.send(command) 

    def read(self):
        val=self.ask("")
        current=val.split('A')
        return float(current[1])