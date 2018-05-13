import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def cm2inch(*tupl): # Conversion de cm vers inch
	inch = 2.54
	if isinstance(tupl[0], tuple):
		return tuple(i/inch for i in tupl[0])
	else:
		return tuple(i/inch for i in tupl)

def trace_track(x0,y0,limits,w,d,color):
	(vmin, vmax) = limits
	plt.plot([x0+w,x0,x0,x0+w,x0+1.04*w,x0+w],[y0-d,y0-d,y0,y0,y0-d/2,y0-d],color='k')
	n = vmax-vmin+1
	for k in range(n):
		plt.plot([x0 + (k+1)*w/n,x0 + (k+1)*w/n],[y0,y0-d],color='k',linewidth=0.5)
		num = (3-len(str(vmin+k)))*' ' + str(vmin+k)
		if vmin+k != 0:
			plt.text(x0 + k*w/n + 0.1*w/n,y0-d/1.8,num,fontsize = 6,color=color)
		else:
			ax.add_patch(patches.Rectangle((x0+k*w/n,y0-d),w/n,d,facecolor=color))
			plt.text(x0 + k * w / n + 0.1 * w / n, y0 - d / 1.8, num, fontsize=6, color='w')

W,H = cm2inch(21,29.7) # Dimensions d'une feuille A4

fig = plt.figure(figsize=(H,W))
ax = fig.add_subplot(111,aspect = 'equal')
plt.plot([0,H,H,0,0],[W,W,0,0,W],color='k') #Contours A4

plt.plot([H/2,H/2],[0,W],color='k',linewidth=0.5) #Separatrice

cols_res = ['#ffc800','#000000','#55bcff','#ff0000','#954e00','#8d8d8d']
bornes = [(0,20),(-10,10),(-20,0),(-10,10),(-10,10),(-10,10),(-10,10)]
d = W/15 #Largeur d'une jauge
s = (W - len(bornes)*d)/7 #Espace inter-jauges
L_n = [1,2,1,1,1,1]

i = 0
for k in range(6):
	for l in range(L_n[k]):
		x0 = 0.05*H/2
		y0 = W - (i*d + (k+1)*s)
		trace_track(x0,y0,bornes[i],0.85*H/2,d,cols_res[k])
		i += 1

plt.axis('equal')
plt.axis('off')
plt.show()

#plt.savefig('jauges.png',format='png',dpi=700)
