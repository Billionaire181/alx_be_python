FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR * Celsius - 32)

def convert_to_fahrenheit(Celsius):
    return CELSIUS_TO_FAHRENHEIT_FACTOR * Fahrenheit + 32

def main():
    temperature = float(input("Enter the temperature to convert: "))
    operation = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if operation == C:
        convert = convert_to_celsius(fahrenheit)
        print(convert)

    elif operation == F:
        convert = convert_to_fahrenheit(celsius)
        print(convert)

    else:
        print("Invalid temperature. Please enter a numeric value.")   

main() 
