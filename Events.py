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
    np.save('Events2/'+event['Nom'],event)
    d=np.load('DeckEvents2.npy')
    d=np.append(d,[Nom])
    np.save('DeckEvents2',d)
    return event


def modify_event(nom):
    deck=np.load('DeckEvents2.npy')
    deck=np.setdiff1d(deck,nom)
    res=np.load('Events2/'+nom+'.npy').item()
    print(res)
    champ=input('Champ à modifier : ')
    while champ!='':
        if (champ=='Exemplaires' or champ=='Ere' or champ=='Piste'):
            modif=input("Modification : ")
            res[champ]=int(modif)
        elif (champ=='Nom' or champ=='Type' or champ=='Agreg'):
            modif=input("Modification : ")
            res[champ]=modif
        elif (champ=='Description' or champ=='Seuils'):
            A=[]
            n=int(input('nb'+champ+' : '))
            for k in range(n):
                A.append(input(champ+' '+str(k)+' : '))
            res[champ]=A
        champ=input('Champ à modifier : ')
    np.save('Events2/'+res['Nom'],res)
    deck=np.append(deck,res['Nom'])
    np.save('DeckEvents2',deck)
    return res


def load_event(nom):
    res=np.load('Events/'+nom+'.npy').item()
    return res