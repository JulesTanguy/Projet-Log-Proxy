# Testé avec Python 3.9.0

# Import des modules
import os
import re

# Localisation des fichiers log_proxy_
listeFichiers = os.listdir()
fichiersLogs = []
for x in listeFichiers :
    y = re.search(r"\blog_proxy_", x)
    if y != None:
        fichiersLogs.append(y.string)

# Feedback
if len(fichiersLogs) == 0:
    print("Aucun fichier 'log_proxy_YYYY-MM-DD.txt' n'a été détecté dans le répertoire courant")
    exit()
NomUser = input("Indiquez le nom de l'utilisateur de la base Oracle : ")
SeqOracle = input("Indiquez le nom de votre séquence Oracle : ")

sortief=open('insert_final.sql','a', encoding='utf-8')

# Boucle tant que qu'il y a des fichiers log_proxy_
i = 0
while i<len(fichiersLogs) :

    # Ouverture du fichier log_proxy_YYYY-MM-DD.txt
    NomDuFichier = fichiersLogs[i]
    entree=open(NomDuFichier,'r', encoding='utf-8')

    # Identification de la date
    x=((len(NomDuFichier)-24)+10)
    y=((len(NomDuFichier)-24)+20)
    date=NomDuFichier[x:y]

    # Localisation des champs puis écriture des commandes sql
    sortie=open('insert_'+date+'.sql','w', encoding='utf-8')
    
    # Création des commandes SQL INSERT
    for ligne in entree :
        champs = ligne.split()
        heure = (champs[0])
        adresseIP = (champs[1])
        url = (champs[4])
        jourheure=date+' '+heure
        sortie.write('\nINSERT INTO "'+NomUser+'"."PROXY" ("id", "adresseIP", "jourheure", "URL") '
        "values("+SeqOracle+".nextVal, '"+adresseIP+"', TO_DATE('"+jourheure+"', 'yyyy-mm-dd hh24:mi:ss'), '"+url+"');")
        sortief.write('\nINSERT INTO "'+NomUser+'"."PROXY" ("id", "adresseIP", "jourheure", "URL") '
        "values("+SeqOracle+".nextVal, '"+adresseIP+"', TO_DATE('"+jourheure+"', 'yyyy-mm-dd hh24:mi:ss'), '"+url+"');")

    # Feedback + incrémentation
    print('insert_'+date+'.sql a été créé avec succès')
    i+=1
print('Les commandes SQL ont bien été ajoutées au fichier insert_final.sql')
