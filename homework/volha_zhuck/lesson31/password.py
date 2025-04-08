# password generator
import random
import string


def password_generator(lenght=15):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation
    all_characters = upper + lower + digits + symbols
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols),
    ]
    password += random.choices(all_characters, k=lenght - 4)
    random.shuffle(password)
    return ''.join(password)


print("Your password is:", password_generator())
