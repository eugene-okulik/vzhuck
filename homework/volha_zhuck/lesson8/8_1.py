import random

salary = int(input("Введите зарплату: "))
bonus = random.choice([True, False])
if bonus is True:
    salary += random.randint(5, 1000)
print(f"{salary}, {bonus} - '${salary}'")
