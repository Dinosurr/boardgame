import ast
from typing import Set, Dict, List, Any, Union, Tuple

import pandas


class Games:
    def show_list(self):
        print(self.df)

    def import_list(self):
        self.df = pandas.DataFrame(self.dicts).reindex(columns=['ID', 'Name', 'players', 'playtime', 'age'])

    def add_item(self, item_id, name, players, time, age):

        temp_dict = {"ID": len(self.dicts) + 1, "Name": name, "age": age, "playtime": time, "players": players}
        self.dicts.append(temp_dict)
        self.print_file()

    def print_file(self):
        f = open("filedata.txt", 'w+')
        f.write(str(self.dicts))
        print("Saving to filedata.txt...")

    # https://www.geeksforgeeks.org/python-removing-dictionary-from-list-of-dictionaries/
    def remove(self, val):
        for i in range(len(self.dicts)):
            if self.dicts[i]['ID'] == int(val):
                del self.dicts[i]
                break
        self.print_file()

    def remove_item(self, key):
        list(filter(lambda person: person['id'] == 2, self.dicts))

    # reads content in filedata.txt as Python datatype instead of into a string. The use of ast.literal_eval is
    # because it doesnt execute the code if its not a valid python datatype. (security issues)
    # https://stackoverflow.com/questions/15197673/using-pythons-eval-vs-ast-literal-eval
    def read_file(self):
        f = open("filedata.txt", 'r')
        self.dicts = ast.literal_eval(f.read())

    def Run(self):
        while True:
            self.read_file()
            self.import_list()
            print("What do you want to do? \n 1. Add a game to list. \n 2. Remove game from list. \n 3. Search for "
                  "game in list.")
            choice = str(input())
            if choice == "1":
                print("Adding item....")
                self.add_item(2, "ABC", 1, 5, 2)
            if choice == "2":
                print("Type the id of the game you want to remove")
                self.remove(input())
            if choice == "3":
                self.show_list()
                print("Showing list")


test = Games()
test.Run()
