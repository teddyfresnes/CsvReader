class DatabaseReader():

    def __init__(self):
        
        self.column_occurence_table = []
        self.initGUI()


    def initGUI(self):

        option0 = input("A) Entrez le nom de la table à traiter avec l'extention (exemple : db.csv)\n> ")
        self.f = open(option0,"r")
        self.f2 = open("results.txt","w")
        
        self.content = self.f.readlines()
        print("-> Super, le fichier a été correctement importé!")

        #option4 = int(input("Que voulez faire ?"))
        self.append_column()
        
        print("\n\nTraitement en cours dans results.txt...")

        self.work_isolation()
            
        self.f2.close()
        self.f.close()

        print("\n\n\nTraitement terminé !\n")


    def append_column(self):
        
        option1 = input("\n\nB) Quelle colonne voulez vous extraire ? (Sensible à la casse)\n> ")
        for line in self.content:
            table = line.split(",")
            occurence = table.index(option1)
            self.column_occurence_table.append(occurence)
            break
        print("-> Super, la colonne a été trouvé!")
        option2 = int(input("\nVoulez vous extraire une autre colonne ?\n[1] Oui\n[2] Non\n> "))
        if option2 == 1:
            self.append_column()


    def work_isolation(self):

        for line in self.content:
            virgules = 0
            limit = False
            element = ""
            for i in line: # explore la ligne
                for occurence in self.column_occurence_table:     
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
            self.f2.write(element)




DatabaseReader()

