from matplotlib import pyplot as plt
import numpy as np

R1 = 0.6
RS1 = 1
R2 = 6

n_tours = 0.5
k = 0.3 # Parametre de repartition des cases

L_color = ['#55c400','#ff8500','#b100ff']
L_alpha = [0,2*np.pi/3,4*np.pi/3]
dalpha = np.pi/2.3

L_steps = []
for R in np.linspace(RS1 + 0.5,R2,10):
	x = k*(R-(RS1+0.5))/(R2-(RS1+0.5)) + 1
	x = np.log(x)/np.log(k+1)*(R2-(RS1+0.5)) + RS1 + 0.5
	L_steps.append(x)

def plot_circle(R,color = 'black'):
	X,Y = [],[]
	for theta in np.linspace(0,2*np.pi,100):
		X.append(R*np.cos(theta))
		Y.append(R*np.sin(theta))
	plt.plot(X,Y,color = color)

def plot_step(R,L_alpha,dalpha,color = 'black'):
	for alpha in L_alpha:
		r = R
		X,Y = [],[]
		dtheta = n_tours*2*np.pi*r/R2
		x = k*(r-RS1)/(R2-RS1) + 1
		dr = -1.5*np.log(x) - 0.8
		#dr = -1.5*((r-RS1)/(R2-RS1)) - 0.5
		for theta in np.linspace(alpha + dtheta,alpha + dtheta*(r + dr)/r + dalpha,100):
			r += dr/100
			X.append(r*np.cos(theta))
			Y.append(r*np.sin(theta))
		plt.plot(X,Y,color = color)

def rotate(p,alpha):
	return (p[0]*np.cos(alpha) - p[1]*np.sin(alpha),p[1]*np.cos(alpha) + p[0]*np.sin(alpha))

def plot_curve(alpha,color = 'black'):
	X,Y = [],[]
	for r in np.linspace(R1,R2,100):
		theta = n_tours*2*np.pi*r/R2
		x = r*np.cos(theta)
		y = r*np.sin(theta)
		(x,y) = rotate((x,y),alpha)
		X.append(x)
		Y.append(y)
	plt.plot(X,Y,color = color)

def plot_track(alpha,dalpha,color = 'black'):
	plot_curve(alpha,color)
	plot_curve(alpha + dalpha,color)

def paint_track(alpha,dalpha,color):
	for beta in np.linspace(alpha,alpha + dalpha,200):
		plot_curve(beta,color)

plt.figure()

for i in range(3):
	paint_track(L_alpha[i],dalpha,L_color[i])
	plot_track(L_alpha[i],dalpha)

plot_circle(R1)
plot_circle(R2)

for R in L_steps:
	plot_step(R,L_alpha,dalpha)

plt.axis('equal')
plt.axis('off')
plt.show()