def perform_operation(num1, num2, operations):
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    operation = (input("Choose an operation: +, -, *, /"))
    match operation:
        case "+":
            addition = num1 + num2
            return addition
        case "-":
            subtraction = num1 - num2
            return subtraction
        case "*":
            multiplication = num1 * num2
            return multiplication
        case "/":
            if num2 == 0:
                print("Zero cannot be divided")
            else:
                division = num1 / num2
                return division
