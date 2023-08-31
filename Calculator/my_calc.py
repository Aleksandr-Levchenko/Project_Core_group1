print("Pleas input: first-operand, then operator(+-*/), then second operand, 'exit' - to end program")
triger = False
operand = 0
result = 0
while True:

    while True:
        user_input = input(">>> ")
        if user_input == "exit":
            break
        if user_input and not triger and not operand:
            try:
                operand = int(user_input)
                triger = True
            except ValueError:
                print(f"{user_input} not integer")
    if user_input and not triger:
        operator = user_input
        triger = False
    if user_input and operand and not triger:
        try:
            if operator == "+":
                result = operand + user_input
            if operator == "-":
                result = operand - user_input
            if operator == "*":
                result = operand * user_input
            if operator == "/":
                result = operand / user_input
        except Exception:
            print("Incorrect input. Pleas try agen")
        break
print(f"Result: {operand} {operator} {user_input} = {result}")

