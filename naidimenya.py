def calculate():
    print("--- Простой калькулятор ---")

    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")

    operation = input("Выберите операцию (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2  
    elif operation == "-":
        result = num1 - num2  
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        result = "Неизвестная операция"

    print(f"Результат: {result}")


calculate()