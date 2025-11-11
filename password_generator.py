import random
import string

def generate_password(length):
    # characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # generate random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# ask user for password length
length = int(input("Enter password length: "))

# generate and display password
password = generate_password(length)
print("Your generated password is:", password)
