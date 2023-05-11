import glob
import time


class CsvReader():

    def __init__(self):
        
        self.column_occurence_table = {}
        self.initGUI()


    def initGUI(self):

        self.file_open()
        
        self.content = self.f.readlines()
        self.number_lines = len(self.content)

        print("-> Super, le fichier",self.filename,"a été correctement importé!")

        option4 = int(input("\n\nQue voulez faire ?\n[1] Extraire une/des colonnes   (Stable)\n[2] Rechercher un élément dans une colonne   (Beta)\n[3] Rechercher un élément dans la table   (HS)\n> "))
        if option4 == 1:
            self.append_column()
            self.work_isolation()
        elif option4 == 2:
            self.append_column()
            self.work_search_column()
        elif option4 == 3:
            self.work_search_column(mode=1)
            
        self.file_close()

        print("\n\n\nTraitement terminé, résultat disponible dans results.txt!\n")

        print("Le programme s'arrête dans 5 secondes...")
        time.sleep(5)


    def append_column(self):
        
        print("\n\nB) Quelle colonne voulez vous extraire ?\n")
        index = 0
        option1 = -1
        for line in self.content: # ajouter une colonne dans la table
            table = line.split(",")
                
            for i in table: # affichage des options (nom de colonnes)
                print("["+str(index+1)+"]",table[index])
                index += 1
            print("\n(Conseil : Appuyez sur le numéro de la colonne pour l'ajouter, appuyer sur 0 pour lancer le script)\n")

            while (option1 != 0 or len(self.column_occurence_table) < 1):
                option1 = int(input("> "))
                if option1 != 0:
                    occurence = table[option1 - 1]
                    self.column_occurence_table[occurence] = option1 - 1
                    
                if (option1 != 0):
                    print("\""+occurence+"\" ajouté.")
                    
            break


    def file_open(self):

        files_table = glob.glob("./*.txt") + glob.glob("./*.csv")
        index = 0
        for file_name in files_table:
            print("["+str(index+1)+"]",files_table[index])
            index += 1
        print("["+str(index+1)+"] Autre ?")

        option0 = int(input("\nA) Entrez le numéro de la table à traiter\n> "))

        if option0 == index+1:
            self.filename = input("Entrez le nom de votre fichier avec l'extention (exemple : db.csv) :\n> ")
        else:
            self.filename = str(files_table[option0 - 1][2:])

        self.f = open(self.filename,"r")
        self.f2 = open("results.txt","w")
        

    def file_close(self):

        self.f2.close()
        self.f.close()


    def work_isolation(self):

        print("\n\nTraitement en cours dans results.txt...\n\n")

        percentage = 0
        index = 0
        
        for line in self.content:
            
            index +=1
            if (index >= self.number_lines * (percentage/100)):
                print(str(percentage)+"%")
                percentage += 1
            
            virgules = 0
            limit = False
            element = ""
            for i in line: # explore la ligne
                for occurence in self.column_occurence_table.values():     
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


    def work_search_column(self,mode=0):

        findit = input("\n\nQue cherchez vous ?\n> ")
        foundit = {}

        if mode == 0:
            print("\n\nRecherche en cours de \""+str(findit)+"\" dans la/les columne(s)...\n\n")
        else:
            print("\n\nRecherche en cours de \""+str(findit)+"\" dans la table...\n\n")

        if mode == 1:
            for line in self.content:
                table = line.split(",")
            for i in range(len(table)):
                self.column_occurence_table[table[i]] = i

        findit = findit.lower()
        percentage = 0
        index = 0
        
        for line in self.content:
            
            index +=1
            if (index >= self.number_lines * (percentage/100)):
                print(str(percentage)+"%	scannée...")
                percentage += 1
            
            virgules = 0
            limit = False
            
            element = ""
            saveIt = False
            position = 0
            

            for i in line: # pour tt les characteres
                for name, occurence in self.column_occurence_table.items(): # pour tt le nom et le nb de virgules choisis
                    
                    if virgules == occurence: # virgules egales a l'occurence
                        try:
                            if i.lower() == findit[position]:
                                #print("1 : "+str(i.lower())+"   2 : "+str(findit[position]))
                                element += i  # enregistre la ligne
                        except:
                            pass
                        position += 1

                        if element.lower() == findit:
                            saveIt = True

                        
                    if saveIt == True:
                        foundit[index] = (name, element)
                        element += i
                        
                if i == "\"": # pour eviter de compter les virgules dans les guillements
                    if limit == False:
                        limit = True
                    else:
                        limit = False
                if i == ',' and limit == False: # change virgules
                    virgules +=1
                    position = 0
                    saveIt = False
                    element = ""
                    

            element = element[:-1] # supprime la virgule en fin de chaine

        print(foundit)
        
        print("\n\n"+str(len(foundit))+" occurences trouvé aux lignes :\n")
        for ligne, items in foundit.items():
            print("["+str(ligne)+"] occurence \""+str(items[1])+"\" dans la colonne \""+items[0]+"\"")

        choice = int(input("\n\nChoississez la ligne à afficher ou appuyez sur 0 pour terminer :\n> "))
        data = self.content[choice-1]
        print(data)

        self.f2.write("Vous avez sélectionné(e) :\n\n")
        self.f2.write(data)
        self.f2.write("\n\n\nLignes trouvées :\n\n")
        for line in foundit.keys():
            data = self.content[line]
            self.f2.write(data)
            self.f2.write("\n")

        


CsvReader()

