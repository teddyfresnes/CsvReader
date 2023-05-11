option0 = input("A) Entrez le nom de la table à traiter avec l'extention (exemple : db.csv)\n> ")
f = open(option0,"r")
results = open("results.txt","w")
lines = f.readlines()
print("-> Super, le fichier a été correctement importé!")

option1 = input("\n\nB) Quelle colonne voulez vous extraire ? (Sensible à la casse)\n> ")
for line in lines:
    table = line.split(",")
    occurence = table.index(option1)
    break
print("-> Super, la colonne a été trouvé!")

occurence2 = -1
try:
    option2 = input("\n\nC) Importer une autre colonne ? (SKIP si non trouvé)\n> ")
    for line in lines:
        table = line.split(",")
        occurence2 = table.index(option2)
        break
except:
    pass

for line in lines:
    virgules = 0
    limit = False
    element = ""
    for i in line: # explore la ligne
        if virgules == occurence: # virgules egales a l'occurence
            element += i # enregistre la ligne
        if virgules == occurence2:
            element += i 
        if i == "\"": # pour eviter de compter les virgules dans les guillements
            if limit == False:
                limit = True
            else:
                limit = False
        if i == ',' and limit == False: # change virgules
            virgules +=1

    element = element[:-1] # supprime la virgule en fin de chaine
    element += "\n"
    results.write(element)
    
    
results.close()
f.close()
