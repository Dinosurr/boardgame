import ast
from typing import Set, Dict, List, Any, Union, Tuple

import pandas


class Games:

    def list(self):
        df = pandas.DataFrame(self.dicts).reindex(columns=['ID', 'Name', 'players', 'playtime', 'age'])
        print(df)

    def add_item(self, item_id, name, players, time, age):

        temp_dict = {"ID": item_id, "Name": name, "age": age, "playtime": time, "players": players}
        self.dicts.append(temp_dict)
        self.print_file()

    def print_file(self):
        f = open("file.txt", 'w+')
        f.write(str(self.dicts))
        print("Saving to file...")

    def remove_item(self, key):
        for i in range(len(self.dicts)):
            if self.dicts[i]['ID'] == 2:
                del self.dicts[i]
                break

    # reads content in file as Python datatypes instead of into a string. The use of ast.literal_eval is because it
    # doesnt execute the code if its not a valid python datatype. (security issues)
    # https://stackoverflow.com/questions/15197673/using-pythons-eval-vs-ast-literal-eval
    def read_file(self):
        f = open("file.txt", 'r')
        self.dicts = ast.literal_eval(f.read())

    def Run(self):
        while True:
            self.read_file()
            print("What do you want to do? \n 1. Add a game to list. \n 2. Remove game from list. \n 3. Search for "
                  "game in list.")
            choice = str(input())
            if choice == "1":
                print("Adding item....")
                self.add_item(2, "ABC", 1, 5, 2)
            if choice == "2":
                print("Type the id of the game you want to remove")
                self.remove_item(int(input()))
            if choice == "3":
                self.list()
                print("Showing list")


test = Games()
test.Run()
