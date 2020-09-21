players = {
    "SS": "Correa",
    "2B": "Altuve",
    "3B": "Bregman",
    "DH": "Gattis",
    "OF": "Springer",        
}

# *****************************
# print(players.keys())
# print(players.values())
# print(players.items())
print(list(players.keys()))
print(list(players.values()))
# CANNOT VIEW AS LISTS WITH INDEX
# *****************************
# second_base = players['2B']
# designated_hitter = players['DH']
# print(players)
# print(second_base)
# print(designated_hitter)
# CASE SENSITIVE
# ******************************
# player_names = list(players.copy().values())
# print(player_names)

# teams = {
#     "astros": ["Altuve", "Correa", "Bregman"],
#     "angels": ["Trout", "Pujols"],
#     "yankees": ["Judge", "Stanton"],
# }
# teams = {
#     "astros": ["Altuve", "Correa", "Bregman"],
#     "angels": ["Trout", "Pujols"],
#     "yankees": ["Judge", "Stanton"],
#     "red sox": ["Price", "Betts"],
# }

# team_groupings = teams.items()

# print(list(team_groupings)[1][1][0])
# the first [1] finds 'angels, the 2nd [1] finds "Trout", "Pujols", the [0] finds "Trout"
# **********************************

# del teams['angels']
# removed_team = teams.pop('mets', 'Team not found')

# print(teams)
# print(removed_team)

# featured_team = teams.get('mets', 'no featured team') --- prints 'no featured team'
# featured_team = teams.get('yankees', 'no featured team')

# print(featured_team)
# teams['red sox'] = ['Price', 'Betts']

# print(teams)
# print(teams['astros'][0:3])
# print(teams['yankees'])

# **********************************
# person = {
#     "name": "Daniel",
#     "age": 36,
#     "class_mates": [
#         {"name": "Cory"},
#         {"name": "Zac"},
#         {"name": "Boli"},
#         {"name": "Eva"},
#         {"name": "Jayden"},
#     ]
# }

# person["state"] = "Utah"

# person["class_mates"].append({"name":"Sally"})

# print(person)
# print(person["class_mates"][0]["name"])
# print(person["class_mates"][1]["name"])
# print(person["class_mates"][2]["name"])
# print(person["class_mates"][3]["name"])
# print(person["class_mates"][4]["name"])