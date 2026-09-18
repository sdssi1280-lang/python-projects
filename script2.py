
import secrets
import string
import random

length = int(input("Enter Password length: "))

if length < 4:
    print("Password must be at least 4 characters long. ")
else :
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),

        ]
    all_chars = string.ascii_letters + string.digits + string.punctuation

    for _ in range(length - 4):
        password.append(secrets.choice(all_chars))

    random.shuffle(password)

    print ("Generated Password: ", "".join (password))


