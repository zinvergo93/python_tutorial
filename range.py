starter_sentence = 'The quick brown fox jumped'
print(starter_sentence[1])
# will print 'h' from 'The'

# starter_sentence[12] = A ***will not work*** 
# cannot change values of string once defined

first = starter_sentence[0]
second = starter_sentence[1]
third = starter_sentence[2]
new_sentence = first + second + third                          
print(new_sentence)
# will print 'The' because 012 is the first 3 values
# of the string

first_word = starter_sentence[0:3]
new_sentence = first_word
print(new_sentence)
# will print 'The' [0:3] will read until spot 3
#  [0:2] will only print 'Th'


# #######################

# # [start:stop:step]
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1 

#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6  (slice position)
#    0   1   2   3   4   5    (index position)

starter_sentence = 'The quick brown fox jumps'

# new_sentence = 'Thy' + starter_sentence[3:25]
new_sentence = 'Thy' + starter_sentence[3:]

print(new_sentence)