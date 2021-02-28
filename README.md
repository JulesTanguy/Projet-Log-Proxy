# Projet-Log-Proxy

## Consignes

Pour être en conformité avec les obligations légales concernant la mise à disposition d’Internet, la société STESIO a mis en place un proxy pour journaliser les accès au web réalisés par ses salariés. A partir de ce journal, le responsable du système d’information (S.I.) souhaite établir des statistiques comme :
- les sites les plus visités
- la liste des utilisateurs les plus consommateurs 

et dans les cas où cela est nécessaire (enquête de police par exemple) être capable de répondre à une requête du type :
-  qui a consulté tel site, tel jour, à telle heure ?

Le fichier de log du proxy est un simple fichier texte (log_proxy.txt) contenant des informations sur les accès au web comme l’adresse IP, la date, l’heure, la commande HTTP utilisée (GET ou POST) , l’URL des différents éléments constituant la page téléchargée (images, bandeau, …). Ce journal étant d’une part, un fichier texte et d’autre part étant très volumineux,  il est difficile à utiliser directement pour répondre facilement à ces besoins.

Le responsable du SI vous demande de créer une base de données sur ORACLE  qui contiendra les tables suivantes :

SALARIES (num, nom, prenom, adresseIP) - clef primaire : num

PROXY (id, adresseIP, jourheure, URL)  - clef primaire : id
