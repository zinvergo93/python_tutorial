import operator
from functools import reduce

"""
dynamic_reducer([1, 2, 3], '+') -> 6
dynamic_reducer([1, 2, 3], '-') -> -4
dynamic_reducer([1, 2, 3], '*') -> 6
dynamic_reducer([1, 2, 3], '/') -> 0.166666667
"""

# my attempt*****
# def dynamic_reducer(arr, op):
#     result = arr + op
#     print(f"{arr} + {op}" == result)
#     return result
    

# arr = [1, 2, 3]
# op = ['+', '-', '*', '/']

# reduce(dynamic_reducer)


def dynamic_reducer(collection, op):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    return reduce((lambda total, element: operators[op](total, element)), collection)

print(dynamic_reducer([1, 2, 3], '+'))
print(dynamic_reducer([1, 2, 3], '-'))
print(dynamic_reducer([1, 2, 3], '*'))  
print(dynamic_reducer([1, 2, 3], '/'))
