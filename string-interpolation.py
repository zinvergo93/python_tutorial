# process Python code inside of strings

name = 'Zac'
greeting = f'Hi {name}'
print(greeting)

greeting = f'This is my {{bracket}} blog post'
print(greeting)

product = 'Python elearning course'

email_content = f"""

Hi {name},

Thank you for purchasing {product}

Regards,

Sales Team
"""

print(email_content)