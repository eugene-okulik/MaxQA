# Задание №1

secret_number = 5

while True:
    input_number = int(input("Enter a number: "))
    if input_number == secret_number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("попробуйте снова")
