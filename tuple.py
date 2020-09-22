# list: []
# dictionary: {}
# tuple: ()

# Tuple: immutable (cannot alter)
# List: Mutable(can alter)

# post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# title = post[0]
# sub_heading = post[1]
# content = post[2]

# title, sub_heading, content = post

# Both prints the same thing

# print(title)
# print(sub_heading)
# print(content)

# **************************************

# post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# print(id(post))

# post = post + ('published',)
# or
# post += ('published',)
# CREATES NEW TUPLE/Override, not the same object
# print(id(post))
# NEW ID shows its a different item

# title, sub_heading, content, status = post

# print(title)
# print(sub_heading)
# print(content)
# print(status)

# print(post) 
# Is new Tuple


# ****************************

# post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# tags = ['python', 'coding', 'tutorial']

# post += (tags,)

# print(post)
# print(post[-1])
# print(post[-1][2])
# ******************************

# How to slice tuples
# post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# print(post[1::2])

# ***********************

# How to "remove elements" from a tuple

# post = ('Python Basics', 'Intro guide to python', 'Some cool python content', 'published')

# Removing elements from end
# post = post[:-1]
# print(post)
# removed last item ('published')

# Removing elements from the beginning
# post = post[1:]
# print(post)
# Removed 'Python Basics'

# Removing specific element (messy/not recommended!!)
# post = list(post)
# post.remove('published')
# post.remove('Intro guide to python')
# post = tuple(post)
# print(post)

# *****************************

# Tuple as Dictionary key

# priority_index = {
#     (1, 'premier'): [1, 34, 12],
#     (1, 'mvp'): [84, 22, 24],
#     (2, 'standard'): [93, 81, 3],
# }

# print(list(priority_index.keys()))
# print(list(priority_index.values()))

# *******************************

# Zip function

# positions = ['2B', '3/B', 'SS', 'DH']
# players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

# scoreboard = zip(positions, players)

# print(list(scoreboard))
# combines list into tuples that correlates each value to their respective
# index, i.e. each player to their appropriate positions

# *********************************

# Set Data structure/how to query
# tags = {
#     'python',
#     'coding',
#     'tutorials',
# }

# print(tags)
# print(tags[0]) - Does not work


# query_one = 'python' in tags
# query_two = 'ruby' in tags
# print(query_one)
# print(query_two)
# Prints boolean 'True' or 'False' 

# for tag in tags:
#     print(tag)

# sorted_tags = sorted(tags)
# print(type(sorted_tags))
# print(set(sorted_tags))

# **************************

# Merging Python sets

tags_one = {
    'python',
    'coding',
    'tutorials', 
    'coding',
}
tags_two = {
    'ruby',
    'coding',
    'tutorials', 
    'development',
}

# Merged Tags
# merged_tags = tags_one  | tags_two
# print(merged_tags)
# prints all, but skips repeated values

# tags in tags_one but not in tags_two

# exclusive_to_tags_one = tags_one - tags_two
# print(exclusive_to_tags_one)
# 'python' is the only item exclusive to tags_one
# exclusive_to_tags_two = tags_two - tags_one
# print(exclusive_to_tags_two)
# 'ruby' and 'development' exclusive to tags_two

# tags found in both tags_one and tags_two
universal_tags = tags_one & tags_two
print(universal_tags)
# 'coding' and 'tutorials' are the only tags that are shared, therefore print
# *********************************
# extending a list


tags = ['python', 'coding', 'tutorials']


# tags.append('programming')
# tags.extend(['programming'])
print(tags)
# Both do the same thing, add 'programming' to the list

tags.extend('programming')
print(tags)
# adds 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g' to list