###########################################################################
# Import libraries
###########################################################################
import sys
import scipy
import time
import uuid
import visa
import serial
from collections import OrderedDict

###########################################################################
# Function definitions
###########################################################################

class Information():
	def __init__(self):
		self.__data=OrderedDict()
	def __getitem__(self,item):
		return self.__data[item]
	def __setitem__(self,item,value):
		self.__data[item]= value
	def __delitem__(self,item):
		del self.__data[item]
	def printinfo(self):
		for key, value in self.__data.items():
			print key, ' :', value

class Instrument():
	def __init__(self,name='',address=None,insttype='Physical'):
		if name=='':
			name=uuid.uuid1()
			print("No name assigned to instrument! Referenced as %s" % name)
			self.uuid=name
		else:
			self.uuid=uuid.uuid1()
		self.info=Information()
		self.info['Name']= name
		self.info['UUID']= self.uuid
		self.info['Type']= insttype
		self.info['Address']= address
		self.info['Status']= 'Waiting for initialization'

	def get_info(self):
		return self.info.printinfo()

	@property
	def status(self):
		return self.info['Status']
		
	@status.setter
	def status(self,value):
		self.info['Status']=value

class VirtualInstrument(Instrument):
	def __init__(self,name,baseinstrument=None):
		Instrument.__init__(self,name,insttype='Virtual')
		self.__baseinstr=None
		if baseinstrument==None:
			self.info['Instrument_base']='None'
		else:
			self.add_baseinstrument(baseintrument)

	def add_baseinstrument(self,baseintrument):
		if isinstance(baseinstrument,Instrument):
			self.__baseinstr=baseintrument
			self.info['Instrument_base']=(baseinstrument.info['Name'],baseinstrument.info['UUID'])
		else:
			print "Error! base_instrument must be of Instrument() type or derived."

class Configuration(Information):
	def __init__(self):
		pass

class Parameter(Information):
	def __init__(self):
		pass