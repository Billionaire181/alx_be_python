def safe_divide["float(numerator)", "float(denominator)"]:
    try:
        divide = numerator / denominator
        print(f"The result of the division is {divide}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except ValueError:
        print("Error: Please enter numeric values only.")
