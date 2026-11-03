import numpy as np

input_värden={"W_R":1,"W_L":2,"B":1,"TETA_O":0,"X_O":0,"Y_O":0}
W=(input_värden["W_R"]+input_värden["W_L"])/2
D_W=(input_värden["W_R"]-input_värden["W_L"])/input_värden["B"]
(W_R,W_L,B,TETA_O,X_O,Y_O)=input_värden.values()

teta = lambda t: D_W * t + TETA_O
x_t = lambda t: (W/D_W)*(np.sin(teta(t))-np.sin(TETA_O))+X_O
y_t = lambda t:(W/D_W)*(-np.cos(teta(t))+np.cos(TETA_O))+Y_O

def mittpunkt():
	'''
	returnerar mittpunktens koordinater
	
	x_mitt=x-koord
	y_mitt=y_koord
	'''
	x_mitt= X_O - (W/D_W)*(np.sin(TETA_O))
	y_mitt= Y_O + (W/D_W)*(np.cos(TETA_O))
	return x_mitt,y_mitt
	
def radie():
	'''
	returnerar radien pâ cirkeln
	
	radien=radie
	'''
	radien=(W/D_W)
	return radien
	
def t_lap():
	'''
	tid_lap=tiden det tar att göra ett varv
	'''
	tid_lap=(2*(np.pi))/D_W
	return tid_lap


if __name__=="__main__":
	svar=input("Vill du välja andra input-värden ? [J/N]")
	if svar == "J":
		(W_R,W_L,B,TETA_O,X_O,Y_O)=input("W_R,W_L,B,TETA_O,X_O,Y_O")
		W=(W_R+W_L)/2
		D_W=(W_R-W_L)/B
	else:
		print("Du svarade nej, värden är:")
		print(input_värden)
		(W_R,W_L,B,TETA_O,X_O,Y_O)=input_värden.values()
		W=(W_R+W_L)/2
		D_W=(W_R-W_L)/B
	print("x_mitt,y_miit=",mittpunkt())
	print("radie",radie())
	print("tiden för en lapp:",t_lap())
	
	
