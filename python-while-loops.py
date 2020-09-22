# nums = list(range (1, 100))

# for num in nums:
#     print(num)

# while len(nums) > 0:
    # print(nums.pop())


# *************Guessing Game***************


# def guessing_game():
#     while True:
#         print('What is your guess?')
#         guess = input()

#         if guess == '46':
#             print('You guessed correctly!!')
#             return False
#         else:
#             print(f'No, {guess} isn\'t the answer. Please try again\n')


# guessing_game()

dog_house = ['Diesel', 'Buster', 'Shadow', 'Otis']

data = 0
while data < len(dog_house):
    print(dog_house[data])
    data = data + 1