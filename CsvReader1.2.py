def append_column():
    option1 = input("\n\nB) Quelle colonne voulez vous extraire ? (Sensible à la casse)\n> ")
    for line in lines:
        table = line.split(",")
        occurence = table.index(option1)
        column_occurence_table.append(occurence)
        break
    print("-> Super, la colonne a été trouvé!")
    option2 = int(input("Voulez vous extraire une autre colonne ?\n[1] Oui\n[2] Non"))
    if option2 == 1:
        append_column()


option0 = input("A) Entrez le nom de la table à traiter avec l'extention (exemple : db.csv)\n> ")
f = open(option0,"r")
results = open("results.txt","w")
lines = f.readlines()
print("-> Super, le fichier a été correctement importé!")

column_occurence_table = []
append_column()
            

for line in lines:
    virgules = 0
    limit = False
    element = ""
    for i in line: # explore la ligne
        for occurence in column_occurence_table:     
            if virgules == occurence: # virgules egales a l'occurence
                element += i # enregistre la ligne
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
