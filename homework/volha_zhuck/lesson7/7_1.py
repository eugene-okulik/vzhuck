import random
n = random.randint(1, 10)
def ugadajka(num):
    while True:
        s = input("Введите число от 1 до 10: ")
        if not s.isnumeric():
            print("Неверный формат данных, введите число от 1 до 10")
        else:
            s = int(s)
            if s != n:
                print("Попробуйте снова")
            else:
                print("Поздравляю! Вы угадали!")
                break
ugadajka(n)
