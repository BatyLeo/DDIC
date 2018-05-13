import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def cm2inch(*tupl): # Conversion de cm vers inch
    inch = 2.54
    if isinstance(tupl[0], tuple):
        return tuple(i/inch for i in tupl[0])
    else:
        return tuple(i/inch for i in tupl)

def trace_track(x0,y0,vmin,vmax,w,d,color):
	plt.plot([x0,x0+w,x0+w,x0,x0],[y0,y0,y0-d,y0-d,y0],color='k')
	n = vmax-vmin+1
	for k in range(n):
		plt.plot([x0 + k*w/n,x0 + k*w/n],[y0,y0-d],color='k',linewidth=0.5)
		plt.text(x0 + k*w/n,y0-d/2,vmin + k)

W,H = cm2inch(21,29.7) # Dimensions d'une feuille A4

fig = plt.figure(figsize=(H,W))
ax = fig.add_subplot(111,aspect = 'equal')
plt.plot([0,H,H,0,0],[W,W,0,0,W],color='k')

plt.plot([H/2,H/2],[0,W],color='k',linewidth=0.5) #Separatrice

cols_res = ['#ffc800','#000000','#55bcff','#ff0000','#954e00','#8d8d8d']
bornes = [(-10,10),(-10,10),(-10,10),(-10,10),(-10,10),(-10,10),(-10,10)]
d = W/15 #Largeur d'une jauge
s = (W - len(bornes)*d)/7 #Espace inter-jauges
L_n = [1,2,1,1,1,1]

i = 0
for k in range(6):
	for l in range(k):
		x = 
		trace_track()
		i += 1

plt.axis('equal')
plt.axis('off')
plt.show()

#plt.savefig('jauges.png',format='png',dpi=700)