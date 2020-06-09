import ast

import pandas


class Games:

    # Only shows the list
    def show_list(self):
        print(self.df.to_string(index=False))

    # Makes the dataframe
    def import_list(self):
        self.df = pandas.DataFrame(self.dicts).reindex(columns=['ID', 'Name', 'Players', 'Playtime', 'Age'])

    def add_item(self, name, players, time, age):

        temp_dict = {"ID": len(self.dicts) + 1, "Name": name, "Age": age, "Playtime": time, "Players": players}
        self.dicts.append(temp_dict)
        self.print_file()

    def print_file(self):
        f = open("filedata.txt", 'w+')
        f.write(str(self.dicts))
        print("Saving to filedata.txt...")

    def search(self, col, val):
        print(self.df.loc[self.df[col] == val])
    # https://www.geeksforgeeks.org/python-removing-dictionary-from-list-of-dictionaries/

    def remove(self, val):
        for i in range(len(self.dicts)):
            if self.dicts[i]['ID'] == int(val):
                del self.dicts[i]
                break
        self.print_file()

    # reads content in filedata.txt as Python datatype instead of into a string. The use of ast.literal_eval is
    # because it doesnt execute the code if its not a valid python datatype. (security issues)
    # https://stackoverflow.com/questions/15197673/using-pythons-eval-vs-ast-literal-eval
    def read_file(self):
        f = open("filedata.txt", 'r')
        self.dicts = ast.literal_eval(f.read())

    def get_number(self):
        try:
            val = int(input())
        except:
            print("Thats not a number!")
            return 0
        return val

    def Run(self):
        while True:
            self.read_file()
            self.import_list()
            print("What do you want to do? \n 1. Add a game to list. \n 2. Remove game from list. \n 3. Show all.")
            choice = str(input())
            if choice == "1":
                print("Please insert info for game to add, Name, Number of players, playtime, age")
                Name = input("Name: ")
                print("Number of players: ")
                Player_count = self.get_number()
                print("Playtime: ")
                Playtime = self.get_number()
                print("Age: ")
                Age = self.get_number()
                if (Playtime != 0) and (Player_count != 0) and (Age != 0):
                    self.add_item(Name, Player_count, Playtime, Age)
                else:
                    print("You inserted a invalid input somewhere, please redo and use the correct syntax")
            if choice == "2":
                print("Type the id of the game you want to remove")
                self.remove(input())
            if choice == "3":
                self.show_list()
                print("Showing list")
            if choice == "4":
                print("Please insert what column you want to search in; Name, Players, Playtime or age:")
                col = input()
                print("Please insert what value you want to search for in the column, case sensitive")
                val = input()
                self.search(col, val)

test = Games()
test.Run()
