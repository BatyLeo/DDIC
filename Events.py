import numpy as np 
import matplotlib.pyplot as plt
import os.path


ressources=['UM','fossile','électricité','nourriture','déchets','pollution']
jauges=['Economique','Environnemental','Social']


def newevent():
    event={}
    Ere=int(input('Ere : '))
    Nom=input('Nom de la carte : ') # string
    Type=input('Type de la carte : ') # string
    Piste=int(input('Piste : '))
    Seuils=[]
    nbseuils=int(input('nb seuils : '))
    for k in range(nbseuils):
        Seuils.append(input('seuil '+str(k)+ ': '))
    Desc=[]
    for k in range(nbseuils):
        Desc.append(input('Description '+str(k)+' : '))
    Agreg=input('Agregateur : ')
    Nbex=input("nombre d'exemplaires : ")
    if Nbex=='':
        Nbex=0
    else:
        Nbex=int(Nbex)
    event['Nom']=Nom
    event['Ere']=Ere
    event['Type']=Type
    event['Piste']=Piste
    event['Seuils']=Seuils
    event['Agreg']=Agreg
    event['Description']=Desc
    event['Exemplaires']=Nbex
    np.save('Events/'+event['Nom'],event)
    d=np.load('DeckEvents1.npy')
    d=np.append(d,[Nom])
    np.save('DeckEvents1',d)
    return event


def modify_card(nom):
    deck=np.load('DeckEvents1.npy')
    deck=np.setdiff1d(deck,nom)
    res=np.load('Events/'+nom+'.npy').item()
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
            for i in range(len(ressources)):
                mod=input('- ' + ressources[i]+' : ')
                if mod=='':
                    Mod.append(0)
                else:
                    Mod.append(int(mod))
            res[champ]=Mod

        champ=input('Champ à modifier : ')
    np.save('Cards/'+res['Nom'],res)
    DECK1=np.append(DECK1,res['Nom'])
    np.save('DECK1',DECK1)
    return res


def load_event(nom):
    res=np.load('Events/'+nom+'.npy').item()
    return res