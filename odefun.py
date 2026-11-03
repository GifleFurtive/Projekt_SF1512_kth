import numpy as np
from robotcircle import input_värden
(W_R,W_L,B,TETA_O,X_O,Y_O)=input_värden.values()

vL=lambda t: aL*t+W_L
vR=lambda t: aR*t+W_R

def odefun(t,U,b,vL,vR):
	"""
	t=tid
	U=startvärde
	b=nân bredd eller nât
	vL=hastighetsfunktion för hjul left*
	vR=hastighet för right
	
	return x_t
	y_t
	teta_t
	"""
	
	
	
if __name__=="__main__":
	odefun(t,V,B,vL,vR)
