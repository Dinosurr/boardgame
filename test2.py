import json

games = [{"ID": 1, "Name": "ABC", "age": 2, "playtime": 5, "players": 1},
       {"ID": 1, "Name": "ABC", "age": 2, "playtime": 5, "players": 1},
       {"ID": 2, "Name": "ABC", "age": 2, "playtime": 5, "players": 1},
       {"ID": 2, "Name": "ABC", "age": 2, "playtime": 5, "players": 1},
       {"ID": 2, "Name": "ABC", "age": 2, "playtime": 5, "players": 1},
       {"ID": 2, "Name": "ABC", "age": 2, "playtime": 5, "players": 1},
       {"ID": 2, "Name": "ABC", "age": 2, "playtime": 5, "players": 1},
       {"ID": 2, "Name": "ABC", "age": 2, "playtime": 5, "players": 1}]

y = json.loads(games)

print(y["Name"])