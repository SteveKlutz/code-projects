import random
import string

password_length = 8

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

all_characters = uppercase_letters + lowercase_letters + digits + symbols

password = "".join(random.sample(all_characters, password_length))

print('Here is your generated password: ', password)
