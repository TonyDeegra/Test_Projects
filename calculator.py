def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Ошибочка: Деление на ноль!"
    return x / y
while True:
    print("Операции: \n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. Выход")
    choice = input("Выберите операцию (1/2/3/4/5): ")
    if choice == '5':
        break
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второй число: "))
        if choice == '1':
            print("Результат: ", add(num1, num2))
        elif choice == '2':
            print("Результат: ", subtract(num1, num2))
        elif choice == '3':
            print("Результат: ", multiply(num1, num2))
        elif choice == '4':
            print("Результат: ", divide(num1, num2))
    else:
        print("Неверный ввод. Пожалуйста, выберите операцию между 1 и 5.")

          

    
