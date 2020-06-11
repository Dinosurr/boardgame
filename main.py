import ast
import os.path
import pandas


class Games():
    def __init__(self):
        self.datafile = "filedata.txt"

    def make_file(self):
        with open(self.datafile, 'w+') as f:
            f.write("[]")

    def print_list(self):
        print(self.df.to_string(index=False))

    def make_dataframe(self):
        self.df = pandas.DataFrame(self.dicts).reindex(columns=['ID', 'Name', 'Players', 'Playtime', 'Age'])

    def add_item(self, name, players, time, age):
        if (self.df['Name'] == name).any():
            print("What you're trying to add already exists")
        else:
            temp_dict = {"ID": len(self.dicts) + 1, "Name": name, "Age": age, "Playtime": time, "Players": players}
            self.dicts.append(temp_dict)
            self.save_content(str(self.dicts))

    def save_content(self, content):
        with open(self.datafile, 'w+') as f:
            f.write(content)
            print(f"Saving to {self.datafile} ...")

    def search(self, col, val):
        if col in self.df:
            if col != "Name":
                val = int(val)
            print(self.df.loc[self.df[col] == val])
        else:
            print("Please use a valid column")

    # https://www.geeksforgeeks.org/python-removing-dictionary-from-list-of-dictionaries/
    def remove_item(self, val):
        for i in range(len(self.dicts)):
            if self.dicts[i]['ID'] == int(val):
                del self.dicts[i]
                break
        self.save_content(str(self.dicts))

    # reads content in filedata.txt as Python datatype instead of into a string. The use of ast.literal_eval is
    # because it doesnt execute the code if its not a valid python datatype. (security issues)
    # https://stackoverflow.com/questions/15197673/using-pythons-eval-vs-ast-literal-eval
    def read_file(self):
        if not os.path.isfile(self.datafile):
            self.make_file()
        with open(self.datafile, 'r') as f:
            self.dicts = ast.literal_eval(f.read())

    def get_number(self):
        try:
            val = int(input())
        except ValueError:
            print("Thats not a number!")
            return 0
        return val

    # Menu selection functions below

    def menu_add_item(self):
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

    def menu_remove_item(self):
        print("Type the id of the game you want to remove")
        self.remove_item(input())

    def menu_show_items(self):
        if not self.df.empty:
            print("Showing list")
            self.print_list()
        else:
            print("List is empty!")

    def menu_filter_items(self):
        print("Please insert what column you want to search in; Name, Players, Playtime or age:")
        col = input()
        print("Please insert what value you want to search for in the column, names are case sensitive!")
        val = input()
        self.search(col.capitalize(), val)

    def Run(self):
        while True:
            self.read_file()
            self.make_dataframe()
            print("What do you want to do? \n 1. Add a game to list. \n 2. Remove game from list. \n 3. Show all. \n "
                  "4. Filter in list \n 5. Exit program")
            choice = str(input())
            if choice == "1":
                self.menu_add_item()

            elif choice == "2":
                self.menu_remove_item()

            elif choice == "3":
                self.menu_show_items()

            elif choice == "4":
                self.menu_filter_items()

            elif choice == "5":
                print("Quitting . . .")
                break
            else:
                print("Invalid input please try again!")


test = Games()
test.Run()
