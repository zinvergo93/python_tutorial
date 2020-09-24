#  for-in loop (will loop for as many times as you stop)
#  while loop (will continue going until you tell it to stop)
# ***********Loops with lists*******************

# players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

# for player in players:
#     print(player)

# value "player" can be any word. could say "for people in players"
# and it'll give the same value

# *********Loops with Dictionaries************

# Make sure to indent, and add ',' after each dictionary item
# players = {
#     '2B': 'Altuve',
#     '3B': 'Bregman',
#     'SS': 'Correa',
#     'DH': 'Gattis',
# }

# for position, player in players.items():
#     print(position)
#     print(player)
#     print('Position', position) # i.e. prints 'Position 2B', etc.
#     print('Player', player) # i.e. prints 'Player Altuve', etc.

# **************Practice******************
# Create and arrat called "members" with 5 elements. Write a for-in
# loop that iterates through the array and prints each member

# members = ['Zac', 'Rudy', 'Mandy', 'Kirstie', 'Frankie']

# for name in members:
#     print(name)

# ***********more practice************
# For-in loop, listing items with text added


# user = {
#         "username": "Daniel",
#         "email": "danielfloyd@bottega.tech",
#         "phone": "888-827-9890",
# }


# for key, value in user.items():
    # print('Items => ' + key, value)
    # print(f'"{key}" : "{value}""')

# for key in user.keys():
    # print('Key => ' + key)
    # print('Key => ', key)
    # print(f'Key=> {key}')
    # print('Key => {0}'.format(key))

# for value in user.values():
    # print('Value => ' + value)
    # print('Value => ', value)
    # print(f'Value => {value}')
    # print('Value => {0}'.format(value))

# for-in as list of multiple dictionaries 
#(WAY too messy, don't do unless you need to)

# user = [
#     {"username": "Daniel"},
#     {"email": "danielfloyd@bottega.tech"},
#     {"phone": "888-827-9890"}
# ]

# for key, value in user[0].items():
#     print(key, value)
# for key, value in user[1].items():
#     print(key, value)
# for key, value in user[2].items():
#     print(key, value)

# *****math examples******
# print(f'{2 + 2}')
# print(f'{8 * 6}')
# print(f'{16 / 2}')
# print(f'{5 / 2}')
# print(f'{26 - 13}')


# user = {
#     "name": "Zac",
#     "age": "27",
#     "location": "Illinois",
# }

# for key, value in user.items():
#     # print(f'His {key} is {value}')
#     print('His ' + key + ' is ' + value)



# *****Print each letter in name in for-in loop***

# name = "Zachary"

# for letter in name:
#     print(letter)


# *******print for-in with range*********

# for num in range(1, 10):
#   print(num)

# for num in range(1, 10, 2):
#   print(num)

# for num in range (1, 15, 3):
#     print(num)

# for num in range (6, 16):
#     print(num)

# for num in range (10, 31, 2):
#     print(num)

# ****************Continue/Break*************
# usernames = [
#     'Jon',
#     'Tyrion',
#     'Theon',
#     'Cersei',
#     'Sansa'
# ]

# for username in usernames:
#     if username == 'Cersei':
#         print(f'Sorry, {username}, you are not allowed')
#         continue
#     else:
#         print(f'{username} is allowed')

# for username in usernames:
#     if username == 'Cersei':
#         print(f'{username} was found at index {usernames.index(username)}')
#         break
#     print(username)

# **************Practice with for-in break/continue

favorite_cereals = [
    'Cinnamon Toast Crunch',
    'Frosted Flakes',
    'Cocoa Puffs',
    'Honey Nut Cheerios',
    'Fruit Loops',
]

# print(favorite_cereals)

favorite_cereals.insert(3,'Shredded Wheat')

# print(favorite_cereals)

for cereal in favorite_cereals:
    if cereal == 'Shredded Wheat':
        print(f'{cereal} is awful and no one should ever eat it.')
        break
    else:
        print(f'Even though {cereal} isn\'t nutritionally sound, at least it tastes good.')