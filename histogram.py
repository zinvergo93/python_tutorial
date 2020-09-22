sales = {
    "Google": 50,
    "Facebook": 30,
    "Twitter": 15,
    "offline": 12,

}

# print('G ' + sales['Google'] * '$')
# print('F ' + sales['Facebook'] * '$')
# print('T ' + sales['Twitter'] * '$')
# print('O ' + sales['offline'] * '$')


for key, value in sales.items():
    print(key[0] + " " + value * "$")

for page in sales.items():
    print(page)