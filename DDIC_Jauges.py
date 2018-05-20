import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from ddic import *

def cm2inch(*tupl): # Conversion de cm vers inch
	inch = 2.54
	if isinstance(tupl[0], tuple):
		return tuple(i/inch for i in tupl[0])
	else:
		return tuple(i/inch for i in tupl)

def trace_track(x0,y0,limits,w,d,color):
	(vmin, vmax) = limits
	for i in range(101):
		plt.plot([x0+(1+4*i/10000)*w,x0+(1+4*i/10000)*w],[y0-i/100*d/2,y0-d+i/100*d/2],color=color,linewidth=0.4)
	n = vmax-vmin+1
	for k in range(n):
		if color == '#000000':
			c = '#f6f6f6'
		else:
			c = 'k'
		plt.plot([x0 + (k+1)*w/n,x0 + (k+1)*w/n],[y0,y0-d],color=c,linewidth=0.7)
		num = (3-len(str(vmin+k)))*' ' + str(vmin+k)
		if vmin+k == 0:
			ax.add_patch(patches.Rectangle((x0+k*w/n,y0-d),w/n,d,facecolor='#f6f6f6'))
			plt.text(x0 + k*w/n + 0.2*w/n,y0-d/1.8,num,fontsize = 6,color=color)
		else:
			ax.add_patch(patches.Rectangle((x0+k*w/n,y0-d),w/n,d,facecolor=color))
			plt.text(x0 + k * w / n + 0.2 * w / n, y0 - d / 1.8, num, fontsize=6, color='w')
	plt.plot([x0+w,x0,x0,x0+w,x0+1.04*w,x0+w],[y0-d,y0-d,y0,y0,y0-d/2,y0-d],color='k',linewidth=1)

W,H = cm2inch(21,29.7) # Dimensions d'une feuille A4
mid = 1.5*H/2 #Position de la separatrice

fig = plt.figure(figsize=(H,W))
ax = fig.add_subplot(111,aspect = 'equal')
plt.plot([0,H,H,0,0],[W,W,0,0,W],color='k') #Contours A4

cols_res = ['#ffc800','#ff0000','#000000','#55bcff','#954e00','#8d8d8d']
bornes = [(0,20),(-10,10),(0,20),(-20,0),(-10,10),(-10,10),(-10,10)]
d = W/15 #Largeur d'une jauge
s = (W - len(bornes)*d)/7 #Espace inter-jauges
L_n = [1,1,2,1,1,1]

i = 0
for k in range(6):
	for l in range(L_n[k]):
		x0 = 0.07*H/2
		y0 = W - (i*d + (k+1)*s) - l*d/5
		trace_track(x0,y0,bornes[i],0.86*mid,d,cols_res[k])
		i += 1

plt.plot([mid,mid],[0,W],color='k',linewidth=2) #Zones de stockage
plt.plot([mid,H],[2*W/3,2*W/3],color='k',linewidth=2)
plt.plot([mid,H],[W/3,W/3],color='k',linewidth=2)
plt.plot([(H+mid)/2,(H+mid)/2],[W/3,0],color='k',linewidth=2)
plt.text(1.05*mid,9.5*W/12,'$UM$',color=cols_res[0],fontsize=60,alpha=0.5)
plt.text(1.11*mid,5.5*W/12,'$F$',color=cols_res[2],fontsize=60,alpha=0.5)
plt.text(1.025*mid,1.5*W/12,'$P$',color=cols_res[5],fontsize=60,alpha=0.5)
plt.text(1.185*mid,1.67*W/12,'$Env$',color='#20c22e',fontsize=30,alpha=0.5)

plt.axis('equal')
plt.axis('off')
plt.show()

plt.savefig('jauges.png',format='png',dpi=500)
resize('jauges.png')