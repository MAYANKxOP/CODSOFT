import string
import random

length = int(input("Enter the length to generate password : "))

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
digit = string.digits
special_char = string.punctuation

all_char = lower_case + upper_case + digit + special_char

password = ''.join(random.sample(all_char, length))

print(password)

