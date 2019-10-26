###########################################################################
# Import libraries
###########################################################################
import sys
import scipy
import time
import Instrument


###########################################################################
# Function definitions
###########################################################################

class Measure():
	def __init__(self):
		print("Initializing measurements")

	def VI_curve(Vstart,Vstop,Vsteps=20,Configuration):

def pippo(x):
	return x
def pluto(y):
	return y**2

funs=[[pippo,[1,2,3],0.5],[pluto,[0,2],0.5]]

def sweep(funs):
	i=1
	for v in funs:
		f[i]=v[0]
		ar[i]=v[1]
		dt[i]=v[2]
		i=i+1
	idx=len(gen)
	for i in range(idx):
		g=exec_single(g[idx-i],ar[idx-i],dt[idx-1])

def exec_single(f,x,dt):
	while True:
		for i in x:
			f(i)
			yield i
