import numpy as np 
import matplotlib.pyplot as plt
import os.path


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
    np.save('Cards/'+Nom,carte)
    
    DECK1=np.load('DECK22.npy')
    DECK1=np.append(DECK1,[Nom])
    np.save('DECK22',DECK1)
    return carte


def loadDeck(name):
    deck=np.load(name+'.npy')
    return deck


def actualiseDECK1():
    deck=loadDeck('DECK1')
    for card in deck:
        if(not os.path.isfile('Cards/' + card + '.npy')):
            deck=np.setdiff1d(deck,card)
    print(deck)
    np.save('DECK1',deck)


def modify_card(nom):
    DECK1=np.load('DECK3.npy')
    DECK1=np.setdiff1d(DECK1,nom)
    res=np.load('Cards2/'+nom+'.npy').item()
    print(res)
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
            for i in range(len(jauges)):
                mod=input('- ' +jauges[i]+' : ')
                if mod=='':
                    Mod.append(0)
                else:
                    Mod.append(int(mod))
            res[champ]=Mod

        champ=input('Champ à modifier : ')
    np.save('Cards2/'+res['Nom'],res)
    DECK1=np.append(DECK1,res['Nom'])
    np.save('DECK3',DECK1)
    return res
        

def modify_champ(nom,champ,valeur):
    DECK1=np.load('DECK3.npy')
    DECK1.remove('Cards2/'+nom)
    res=np.load(nom+'.npy').item()
    res[champ]=valeur
    np.save('Cards2/'+res['Nom'],res)
    DECK1=np.append(DECK1,res['Nom'])
    np.save('DECK"',DECK1)
    return res
    
def load_card(nom):
    res=np.load('Cards/'+nom+'.npy').item()
    return res