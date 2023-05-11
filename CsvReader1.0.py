
f = open("db.csv","r")
results = open("results.txt","w")
lines = f.readlines()

option1 = input("Quelle colonne voulez vous extraire ?\n> ")

for line in lines:
    table = line.split(",")
    occurence = table.index(option1)
    break


for line in lines:
    virgules = 0
    limit = False
    element = ""
    for i in line: # explore la ligne
        if virgules == occurence: # virgules egales a l'occurence
            element += i # enregistre la ligne
        if i == "\"":
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
