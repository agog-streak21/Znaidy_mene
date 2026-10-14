
def calculate():
    print("--- Простой калькулятор ---")

    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: введите корректные числа")
        return

    operation = input("Выберите операцию (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Ошибка: на ноль делить нельзя")
            return
        result = num1 / num2
    else:
        result = "Неизвестная операция"

    print(f"Результат: {result}")


calculate()
