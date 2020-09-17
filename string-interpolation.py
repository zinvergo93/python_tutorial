# process Python code inside of strings

# name = 'Zac'
# greeting = f'Hi {name}'
# print(greeting)

# greeting = f'This is my {{bracket}} blog post'
# print(greeting)

# product = 'Python elearning course'
# import operator
# from functools import reduce

# zac = {
#     "name": "Zac",
#     "age": "27",
#     "products": [
#         {
#             "name": "Tortured Souls action figure",
#             "price": "$55",
#         },
#         {
#             "name": "Figma Silent Hill: Bubble Nurse action figure",
#             "price": "$65"
#         }
#     ]

# }



# email_content = f"""

# Hi {zac["name"]},

# Thank you for purchasing {zac["products"][0]["name"]} and {zac["products"][1]["name"]}.

# Each figure costs {zac["products"][0]["price"]} and {zac["products"][1]["price"]}, respectively.

# Bringing your total to

# Regards,

# Sales Team
# """

# print(email_content)


# name = 'Zac'
# age = "27"
# product = "Tortured Souls action figure"
# from_account = "Sales Team"

# greeting = "Hi {0}, you are {1} years old and bought the {2}.\n \n -from \n \n {3}" .format(name, age, product, from_account)

# print(greeting)

# sentence = "The quick brown fox jumps over the lazy dog"

# query = sentence.find('quick') ---- '4'
# query_two = sentence.index('quick') ---- '4'

# print(query)
# print(query_two) 

# query = sentence.find('oops') ---- '-1'
# query_two = sentence.index('oops') ----- error

# print(query)
# print(query_two) 

# query = 'fox' in sentence
# query_two = "oops" in sentence

# print(query) ---- True
# print(query_two) ---- False

if "Zac" in name:
    print("You're pretty cool")