tags = ['python', 'development', 'tutorials', 'code']

# Nope
# tags[-1] = 'Programming'
# override and replaced 'code' with 'programming'

# In Place
# tags.extend('programming')
# extends by listing each letter of "Programming" as separate elements
tags.extend(['programming'])

# New List
new_tags = tags + ['programming']
# new_tags = tags.extend(['programming']) ---- will return 'None'

# print(new_tags)

print(tags)