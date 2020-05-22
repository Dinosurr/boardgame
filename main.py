import os

class Games:
    dicts = [

    ]

    def add_item(self, name, id, players, time, age):

        temp_dict = {"id" : id, "Name" : name, "age": age, "time_to_play:": time, "players" : players }
        self.dicts.append(temp_dict)
        test.print_file()

    def print_file(self):
        f = open("file.txt", 'a+')
        f.write(str(self.dicts))
        print("Saving to file...")

    def Run(self):
            print("What do you want to do? \n 1. Add a game to list. \n 2. Remove game from list. \n 3. Search for "
                  "game in list.")
            choice = str(input())
            if choice == "yes":
                self.add_item("test", 2, 4, 4, 1)
                print("Adding item....")


test = Games()
test.Run()