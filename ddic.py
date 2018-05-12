import numpy as np 
import matplotlib.pyplot as plt 
import scipy.ndimage as ndimage
plt.rcParams['image.cmap'] = 'gray'

ressources=['UM','fossile','électricité','nourriture','déchets','pollution']
jauges=['Economique','Environnemental','Social']



# création et édition des cartes

def newcard():
    carte={}
    Ere=int(input('Ere : '))
    Nom=input('Nom de la carte : ') # string
    Type=input('Type de la carte : ') # string
    Cout=int(input('Cout en UM de la carte : ')) # int
    Desc=input('Description et effets de la carte : ') # string
    print('Consommation : ')
    Cons=[]
    for i in range(len(ressources)):
        cons=input('- ' + ressources[i]+' : ')
        if cons=='':
            Cons.append(0)
        else:
            Cons.append(int(cons))
    print('Production : ')
    Prod=[]
    for i in range(len(ressources)):
        prod=input('- ' + ressources[i]+' : ')
        if prod=='':
            Prod.append(0)
        else:
            Prod.append(int(prod))
    print('Modificateurs : ')
    Mod=[]
    for i in range(len(jauges)):
        mod=input('- ' + jauges[i]+' : ')
        if mod=='':
            Mod.append(0)
        else:
            Mod.append(int(mod))
    nbex=input("nombre d'exemplaires : ")
    if nbex=='':
        nbex=0
    else:
        nbex=int(nbex)
    
    carte['Nom']=Nom
    carte['Ere']=Ere
    carte['Type']=Type
    carte['Cout']=Cout
    carte['Description']=Desc
    carte['Consommation']=Cons
    carte['Production']=Prod
    carte['Modificateurs']=Mod
    carte['Exemplaires']=nbex
    np.save(Nom,carte)
    
    DECK1=np.load('DECK1.npy')
    DECK1=np.append(DECK1,[Nom])
    np.save('DECK1',DECK1)
    return carte


def modify_card(nom):
    DECK1=np.load('DECK1.npy')
    DECK1=np.setdiff1d(DECK1,nom)
    res=np.load(nom+'.npy').item()
    champ=input('Champ à modifier : ')
    while champ!='':
        if (champ=='Exemplaires' or champ=='Ere' or champ=='Cout'):
            modif=input("Modification : ")
            res[champ]=int(modif)
        elif (champ=='Nom' or champ=='Type' or champ=='Description'):
            modif=input("Modification : ")
            res[champ]=modif
        elif champ=='Production':
            Prod=[]
            for i in range(len(ressources)):
                prod=input('- ' + ressources[i]+' : ')
                if prod=='':
                    Prod.append(0)
                else:
                    Prod.append(int(prod))
            res[champ]=Prod
        elif champ=='Consommation':
            Cons=[]
            for i in range(len(ressources)):
                cons=input('- ' + ressources[i]+' : ')
                if cons=='':
                    Cons.append(0)
                else:
                    Cons.append(int(cons))
            res[champ]=Cons
        else: # champs==modificateurs
            Mod=[]
            for i in range(len(ressources)):
                mod=input('- ' + ressources[i]+' : ')
                if mod=='':
                    Mod.append(0)
                else:
                    Mod.append(int(mod))
            res[champ]=Mod

        champ=input('Champ à modifier : ')
    np.save(res['Nom'],res)
    DECK1=np.append(DECK1,res['Nom'])
    np.save('DECK1',DECK1)
    return res
        

def modify_champ(nom,champ,valeur):
    DECK1=np.load('DECK1.npy')
    DECK1.remove(nom)
    res=np.load(nom+'.npy').item()
    res[champ]=valeur
    np.save(res['Nom'],res)
    DECK1=np.append(DECK1,res['Nom'])
    np.save('DECK1',DECK1)
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

side = h/32
def disp_squares(x,y,n,color):
	for k in range(n):
		ax.add_patch(patches.Rectangle((x+1.8*k*side,y),side,side,facecolor=color,linewidth=0.5))

def trace_card(x0,y0,name):
    card=load_card(name)
    
    Nom=card['Nom']
    Type=card['Type']
    Cout=card['Cout']
    Desc=card['Description']
    Cons=card['Consommation']
    Prod=card['Production']
    Ere=card['Ere']
    Mod=card['Modificateurs']
    Nbex=card['Exemplaires']

   h0,h1,h2,h3,h4,h5,h6,h7,h8 = y0,y0-2*h/16,y0-3*h/16,y0-4*h/16,y0-9*h/16,y0-10*h/16,y0-11*h/16,y0-15*h/16,y0-h
	plt.plot([x0,x0+w,x0+w,x0,x0],[y0,y0,y0-h,y0-h,y0],color = 'k') #Contours
	plt.plot([x0,x0+w],[h1,h1],color='k',linewidth=0.8) #Cout/nom
	plt.plot([x0+2*w/10,x0+3*w/10],[h1,h0],color='k',linewidth=0.5)
	plt.plot([x0+5*w/10,x0+6*w/10,x0+w],[h1,h2,h2],color='k',linewidth=0.5) #Type
	plt.plot([x0,x0+2.2*w/10,x0+3.2*w/10],[h2-h/46,h2-h/46,h1],color='k',linewidth=0.5) #Ere
	plt.plot([x0+w/10,x0+9*w/10,x0+9*w/10,x0+w/10,x0+w/10],[h3,h3,h4,h4,h3],color='k',linewidth=0.5) #Texte
	plt.plot([x0,x0+4*w/10,x0+5*w/10,x0+6*w/10,x0+w],[h5,h5,h6,h5,h5],color='k',linewidth=0.5) #Consommation/production
	plt.plot([x0,x0+w],[h6,h6],color='k',linewidth=0.5)
	plt.plot([x0+w/2,x0+w/2],[h6,h7],color='k',linewidth=0.8)
	plt.plot([x0,x0+w],[h7,h7],color='k',linewidth=0.8) #Modificateurs
	plt.plot([x0+w/3,x0+w/3],[h7,h8],color='k',linewidth=0.8)
	plt.plot([x0+2*w/3,x0+2*w/3],[h7,h8],color='k',linewidth=0.8)
	
	plt.text(x0 + 1.5*w/20,h0 - 1.3*h/15,str(Cout),fontsize = 9)
	plt.text(x0 + 3.5*w/10,h0 - 1.3*h/15,Nom,fontsize = 9)
	plt.text(x0 + 2.2*w/20,h1 - h/15.5,Ere*'I',fontsize = 8)
	plt.text(x0 + 6.3*w/10,h1 - 0.65*h/15,Type,fontsize = 4)
	plt.text(x0 + 0.8*w/20,h5 - 0.65*h/15,'Consommation',fontsize = 4)
	plt.text(x0 + 12.8*w/20,h5 - 0.65*h/15,'Production',fontsize = 4)
	
	cols_res = ['#ffc800','#000000','#55bcff','#ff0000','#954e00','#8d8d8d']	
	i = 0 #Affichage de la consommation
	for k in range(6):
		res = Cons[k]
		if res:
			i+=1
			yi = h6 - i*h/18
			plt.text(x0 + 0.5*w/10,yi,'-',fontsize = 8)
			if res < 5:
				disp_squares(x0 + 1.2*w/10,yi,res,cols_res[k])
			else :
				disp_squares(x0 + 1.2*w/10,yi,1,cols_res[k])
				plt.text(x0 + 1.2*w/10 + 2*side,yi + side/10,'x',fontsize = 5)
				plt.text(x0 + 1.2*w/10 + 3.5*side,yi,str(res),fontsize = 6)
	i = 0 #Affichage de la production
	for k in range(6):
		res = Prod[k]
		if res:
			i+=1
			yi = h6 - i*h/18
			plt.text(x0 + w/2 + 0.5*w/10,yi + side/8,'+',fontsize = 5)
			if res < 5:
				disp_squares(x0 + w/2 + 1.2*w/10,yi,res,cols_res[k])
			else :
				disp_squares(x0 + w/2 + 1.2*w/10,yi,1,cols_res[k])
				plt.text(x0 + w/2 + 1.2*w/10 + 2*side,yi + side/10,'x',fontsize = 5)
				plt.text(x0 + w/2 + 1.2*w/10 + 3.5*side,yi,str(res),fontsize = 6)

	cols_mod = ['#8321d2','#1ca200','#af1d1d']
	for k in range(3):
		mod = Mod[k]
		if mod > 0:
			ax.add_patch(patches.Rectangle((x0+k*w/3,h8),w/3,h/16,facecolor=cols_mod[k]))
			plt.text(x0 + w/8 + k*w/3,h7 - h/22,'+' + str(mod),fontsize = 6,color = 'w')
		elif mod < 0:
			ax.add_patch(patches.Rectangle((x0+k*w/3,h8),w/3,h/16,facecolor=cols_mod[k]))
			plt.text(x0 + w/8 + k*w/3,h7 - h/22,'–' + str(-mod),fontsize = 6,color = 'w')

def test(): 
    fig = plt.figure(figsize=(W,H))
    ax = fig.add_subplot(111,aspect = 'equal')
    plt.plot([0,W,W,0,0],[H,H,0,0,H],color='k')
    
    testcard = ['USINES','Infrastructure',13,'blabla',[0,1,3,0,0,0],[6,0,0,2,1,1],2,[1,0,-4],10]
    for pos in cards_grid():
	     trace_card(pos[0],pos[1],"Usines basiques")

    plt.axis('equal')
    plt.axis('off')
    plt.show()

    plt.savefig('test.png',format='png',dpi=700)
    
    resize('test.png')
    
