def perform_operation(num1, num2, operation):
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    operation = (input("Choose an operation: +, -, *, /"))
    match operation:
        case "add":
            addition = num1 + num2
            return addition
        case "subtract":
            subtraction = num1 - num2
            return subtraction
        case "multiply":
            multiplication = num1 * num2
            return multiplication
        case "divide":
            if num2 == 0:
                print("Zero cannot be divided")
            elif numb2 > 0:
                division = num1 / num2
                return division
        else:
            print("Enter a valid number")
