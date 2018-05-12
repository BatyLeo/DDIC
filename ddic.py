import numpy as np 
import matplotlib.pyplot as plt 
import scipy.ndimage as ndimage
plt.rcParams['image.cmap'] = 'gray'

ressources=['UM','fossile','électricité','nourriture','déchets','pollution']
jauges=['Economique','Social','Environnemental']

# création et édition des cartes

def newcard():
    carte={}
    Ere=input('Ere : ')
    Nom=input('Nom de la carte : ') # string
    Type=input('Type de la carte : ') # string
    Cout=input('Cout en UM de la carte : ') # int
    Desc=input('Description et effets de la carte : ') # string
    print('Consommation : ')
    Cons=[]
    for i in range(len(ressources)):
        Cons.append(input('- ' + ressources[i]+' : '))
    print('Production : ')
    Prod=[]
    for i in range(len(ressources)):
        Prod.append(input('- ' + ressources[i]+' : '))
    print('Modificateurs : ')
    Mod=[]
    for i in range(len(jauges)):
        Mod.append(input('- ' + jauges[i]+' : '))
    
        
    carte['Nom']=Nom
    carte['Type']=Type
    carte['Cout']=Cout
    carte['Description']=Desc
    carte['Consommation']=Cons
    carte['Production']=Prod
    carte['Modificateurs']=Mod
    np.save(Nom,carte)
    return carte

def modify(nom,champ,valeur):
    res=np.load(nom+'.npy').item()
    res[champ]=valeur
    np.save(res['Nom'],res)
    return res
    
def load_card(nom):
    res=np.load(nom+'.npy').item()
    return res
    
    
    
# traitement des images

def load_image(name,crop_window=-1): 
    I=plt.imread(name)
    if crop_window!=-1:
        I=I[crop_window[0]:crop_window[1],crop_window[2]:crop_window[3]]
    I=I.astype('float')
    #if len(I.shape)>2 and I.shape[2]==3:
        #I=0.2989 * I[:,:,0] + 0.5870 * I[:,:,1] + 0.1140 * I[:,:,2]
    return I

def resize(name):
    I=load_image(name)
    # bande supérieure
    i=0
    j=I.shape[1]//2
    while I[i,j,0]==1:
        i+=1
    I=I[i:,:,:]
    # bande gauche
    j=0
    while I[i,j,0]==1:
        j+=1
    I=I[:,j:,:]
    # bande droite
    j=I.shape[1]-1
    while I[i,j,0]==1:
        j-=1
    I=I[:,:j+1,:]
    # bande inférieure
    i=I.shape[0]-1
    while I[i,j,0]==1:
        i-=1
    I=I[:i+1,:,:]
    plt.imsave(name,I,dpi=500)
    #plt.imshow(I)
    #plt.show()
    
    
def cm2inch(*tupl): # Conversion de cm vers inch
    inch = 2.54
    if isinstance(tupl[0], tuple):
        return tuple(i/inch for i in tupl[0])
    else:
        return tuple(i/inch for i in tupl)

W,H = cm2inch(21,29.7) # Dimensions d'une feuille A4
w,h = cm2inch(4.2,6.4) # Dimensions des cartes

def cards_grid():
	Nx = int(W//w)
	Ny = int(H//h)
	dx = (W%w)/(Nx+1)
	dy = (H%h)/(Ny+1)
	pos = []
	for nx in range(Nx):
		for ny in range(Ny):
			pos.append((dx + nx*(w + dx),H - dy - ny*(h + dy)))
	return pos

def trace_card(x0,y0,name):
    card=load_card(name)
    
    Nom=card['Nom']
    Type=card['Type']
    Cout=card['Cout']
    Desc=card['Description']
    Cons=card['Consommation']
    Prod=card['Production']

    h0,h1,h2,h3,h4,h5,h6,h7,h8 = y0,y0-2*h/16,y0-3*h/16,y0-4*h/16,y0-10*h/16,y0-11*h/16,y0-12*h/16,y0-15*h/16,y0-h
    plt.plot([x0,x0+w,x0+w,x0,x0],[y0,y0,y0-h,y0-h,y0],color = 'k') # Contour
    plt.plot([x0,x0+w],[h1,h1],color='k',linewidth=0.8) # Cout/nom
    plt.plot([x0+2*w/10,x0+3*w/10],[h1,h0],color='k',linewidth=0.5)
    plt.plot([x0+5*w/10,x0+6*w/10,x0+w],[h1,h2,h2],color='k',linewidth=0.5) # Type
    plt.plot([x0,x0+2.2*w/10,x0+3.2*w/10],[h2-h/46,h2-h/46,h1],color='k',linewidth=0.5) # Ere
    plt.plot([x0+w/10,x0+9*w/10,x0+9*w/10,x0+w/10,x0+w/10],[h3,h3,h4,h4,h3],color='k',linewidth=0.5) # Texte
    plt.plot([x0,x0+4*w/10,x0+5*w/10,x0+6*w/10,x0+w],[h5,h5,h6,h5,h5],color='k',linewidth=0.8) # Consommation/production
    plt.plot([x0,x0+w],[h6,h6],color='k',linewidth=0.5)
    plt.plot([x0+w/2,x0+w/2],[h6,h7],color='k',linewidth=0.8)
    plt.plot([x0,x0+w],[h7,h7],color='k',linewidth=0.8) # Pistes
    plt.plot([x0+w/3,x0+w/3],[h7,h8],color='k',linewidth=0.5)
    plt.plot([x0+2*w/3,x0+2*w/3],[h7,h8],color='k',linewidth=0.5)
    


"""
def trace_cardbis(x0,y0,card):
	[name,type,cost,text,cons,prod,mod] = card
	h0,h1,h2,h3,h4,h5,h6,h7,h8 = y0,y0-2*h/16,y0-3*h/16,y0-4*h/16,y0-10*h/16,y0-11*h/16,y0-12*h/16,y0-15*h/16,y0-h
	plt.plot([x0,x0+w,x0+w,x0,x0],[y0,y0,y0-h,y0-h,y0],color = 'k')
	plt.plot([x0,x0+w],[h1,h1],color='k',linewidth=0.8)
	plt.plot([x0+2*w/10,x0+3*w/10],[h1,h0],color='k',linewidth=0.5)
	plt.plot([x0+5*w/10,x0+6*w/10,x0+w,x0+w,x0+4*w/10],[h1,h2,h2,h1,h1],color='k',linewidth=0.5)
	plt.plot([x0+w/10,x0+9*w/10,x0+9*w/10,x0+w/10,x0+w/10],[h3,h3,h4,h4,h3],color='k',linewidth=0.5)
	plt.plot([x0,x0+4*w/10,x0+5*w/10,x0+6*w/10,x0+w],[h5,h5,h6,h5,h5],color='k',linewidth=0.8)
	plt.plot([x0,x0+w],[h6,h6],color='k',linewidth=0.5)
	plt.plot([x0+w/2,x0+w/2],[h6,h7],color='k',linewidth=0.8)
	plt.plot([x0,x0+w],[h7,h7],color='k',linewidth=0.8)
	plt.plot([x0+w/3,x0+w/3],[h7,h8],color='k',linewidth=0.5)
	plt.plot([x0+2*w/3,x0+2*w/3],[h7,h8],color='k',linewidth=0.5)
	
        plt.text(x0 + 1.5*w/20,h0 - 1.3*h/15,str(cost),fontsize = 9)
	plt.text(x0 + 3.5*w/10,h0 - 1.3*h/15,name,fontsize = 9)
	plt.text(x0 + 2.2*w/20,h1 - h/15.5,era*'I',fontsize = 8)
	plt.text(x0 + 6.3*w/10,h1 - 0.65*h/15,type,fontsize = 4)


def test2(): 
    fig = plt.figure(figsize=(W,H))
    plt.plot([0,W,W,0,0],[H,H,0,0,H],color='k')
    
    testcard = ['USINES','Infrastructure',13,'blabla',[1,0],[1,1,0,0,0,0],[0,0,0]]
    #testcard='Usines'
    for pos in cards_grid():
        trace_cardbis(pos[0],pos[1],testcard)
    
    plt.axis('equal')
    plt.axis('off')
    plt.show()
    
    plt.savefig('cards.png',format='png',dpi=500)
"""

def test(): 
    fig = plt.figure(figsize=(W,H))
    plt.plot([0,W,W,0,0],[H,H,0,0,H],color='k')
    
    testcard='Usines'
    for pos in cards_grid():
        trace_card(pos[0],pos[1],testcard)
    
    plt.axis('equal')
    plt.axis('off')
    #plt.show()
    
    plt.savefig('test.png',format='png',dpi=500)    
    
    resize('test.png')
    
