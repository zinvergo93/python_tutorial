# tags = ['python', 'development', 'tutorials', 'code']

# number_of_tags = len(tags)
# last_item = tags[-1]
# -1 grabs last element of tags
# index_of_last_item = tags.index(last_item)
# index 0, 1, 2, 3  ** will print 3 **

# print(number_of_tags)
# print(last_item)
# print(index_of_last_item)

# len() grabs length of tags

# tags.sort()
# puts in alphabetical order
# tags.sort(reverse = True)
# reverse order of what's defined
# print(tags)

# totals = [234, 1, 543, 2345]

# print(totals)

# totals.sort()

# print(totals)

# totals.sort(reverse = True)

# print(totals)


# tag_range = tags[1:2]
# prints 'development'
# tag_range = tags[1:3]
# prints 'development, 'tutorials'
# tag_range = tags[1:]
# prints 'development, 'tutorials', 'code'
# tag_range = tags [:2]
# prints 'python', 'development'
# tag_range = tags[:]
# prints all tags in defined order

# print(tag_range)

tags = [
    'python',
    'development',
    'tutorials',
    'code',
    'programming',
    'computer science'
]

# tag_range = tags[1:-1]
# prints from index 1 ('development') to index -1 
# *one backward from the last index*('programming')

# tag_range = tags[:-1:2]
# prints every other tag, starting from first spot
# 'python', 'tutorials', 'programming'
# tag_range = tags [::-1]
# prints all in reverse
# print(tag_range)

# print(tags[0][::-1])
# print(tags[1][::-1])
# prints listed tags spelled backwards

# sorted_tags = tags.sort(reverse = True)
# returns 'None', immutable when stored in a variable as a new string

# print(sorted_tags)

# tags.sort(reverse = True)

# print(tags)

# sale_prices = [
#   100,
#   83,
#   220,
#   40,
#   100,
#   400,
#   10,
#   1,
#   3
# ]

# # sale_prices.sort()
# sorted_list = sorted(sale_prices, reverse = True)
# # Keeps original list values intact, and allows to sort in separate variable

# print(sale_prices)
# print(sorted_list)