# Operator
# https://docs.python.org/3/library/operator.html

# Reduce
# https://docs.python.org/3/howto/functional.html
# https://www.geeksforgeeks.org/reduce-in-python/

# Lambda
# https://www.w3schools.com/python/python_lambda.asp

""" Jordan Solution with a couple quick tips """
import operator
from functools import reduce

""" Operator """
# addition = operator.add(1, 2)
# print(addition)

""" Reduce without lambda """
# print(reduce(operator.add, [1, 2, 3]))
# print(reduce(operator.sub, [1, 2, 3]))
# print(reduce(operator.mul, [1, 2, 3]))
# print(reduce(operator.truediv, [1, 2, 3]))


""" Reduce with lambda """
# reduce(lambda x, y: x+y, [1, 2, 3])


""" Reduce with lambda, operators and our number_list variable """
# number_list = [1, 2, 3]
# print(reduce(lambda x, y: operator.add(x, y), number_list))


""" Completed function with the simple reduce and the more confusing one with lambda """
# def dynamic_reducer(number_list, op):
#   my_operators = {
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.truediv
#   }
#   return reduce(my_operators[op], number_list)
#   # return reduce(lambda x, y: my_operators[op](x, y), number_list)

# print(dynamic_reducer([1, 2, 3], "+"))
# print(dynamic_reducer([1, 2, 3], "-"))
# print(dynamic_reducer([1, 2, 3], "*"))
# print(dynamic_reducer([1, 2, 3], "/"))


""" Reduce, Lamba and Operators in a dictionary """
# def dynamic_reducer(number_list, op):
#   my_operators = {
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.truediv
#   }
#   return reduce(my_operators[op], number_list)
#   # return reduce(lambda x, y: my_operators[op](x, y), number_list)

# print(dynamic_reducer([1, 2, 3], "+"))
# print(dynamic_reducer([1, 2, 3], "-"))
# print(dynamic_reducer([1, 2, 3], "*"))
# print(dynamic_reducer([1, 2, 3], "/"))


""" If / Else with Reduce and Lambda"""
# def dynamic_reducer(number_list, op):
#   if op == "+":
#     return reduce(lambda x, y: x + y, number_list)
#   elif op == "-":
#     return reduce(lambda x, y: x - y, number_list)
#   elif op == "*":
#     return reduce(lambda x, y: x * y, number_list)
#   elif op == "/":
#     return reduce(lambda x, y: x / y, number_list)

# print(dynamic_reducer([1, 2, 3], "+"))
# print(dynamic_reducer([1, 2, 3], "-"))
# print(dynamic_reducer([1, 2, 3], "*"))
# print(dynamic_reducer([1, 2, 3], "/"))


""" If / Else with Reduce and no Lambda """
# def dynamic_reducer(number_list, op):
#   if op == "+":
#     return reduce(operator.add, number_list)
#   elif op == '-':
#     return reduce(operator.sub, number_list)
#   elif op == "*":
#     return reduce(operator.mul, number_list)
#   elif op == "/":
#     return reduce(operator.truediv, number_list)

# print(dynamic_reducer([1, 2, 3], "+"))
# print(dynamic_reducer([1, 2, 3], "-"))
# print(dynamic_reducer([1, 2, 3], "*"))
# print(dynamic_reducer([1, 2, 3], "/"))
# print(dynamic_reducer([6, 2, 1], "/"))


""" If / Else without Reduce """
# def dynamic_reducer(number_list, op):
#   if op == "+":
#     total = 0
#     for num in number_list:
#       total += num
#     return total
#   elif op == '-':
#     total = number_list[0]
#     for num in range(1, len(number_list)):
#       total -= number_list[num]
#     return total
#   elif op == "*":
#     total = 1
#     for num in number_list:
#       total *= num
#     return total
#   elif op == "/":
#     total = number_list[0]
#     for num in number_list[1:]:
#       total /= num
#     return total

# print(dynamic_reducer([1, 2, 3], "+"))
# print(dynamic_reducer([1, 2, 3], "-"))
# print(dynamic_reducer([1, 2, 3], "*"))
# print(dynamic_reducer([1, 2, 3], "/"))
# print(dynamic_reducer([4, 5, 2], "/"))

