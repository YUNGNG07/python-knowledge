import random
import string

def generate_password():
    # password_length = random.randint(16,22)
    password_length = 15
    password_characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(password_characters, k=password_length))

    return password

print(generate_password())
