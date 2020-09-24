import random

def weighted_lottery(weights):
    result_list = []

    for (name, weight) in weights.items():
        for _ in range (weight):
            result_list.append(name)

    return random.choice(result_list)

weights = {
    'win' : 1,
    'break-even' : 6,
    'lose' : 10,
}

print(weighted_lottery(weights))


# Jordan's solution

# import random

# def weighted_lottery(weights):
#     container_list = []

#     for (name, weight) in weights.items():
#         for _ in range(weight):
#             container_list.append(name)

#     return random.choice(container_list)

# weights = {
#     'win' : 1,
#     'break-even' : 6,
#     'lose' : 10,
# }


# print(weighted_lottery(weights))