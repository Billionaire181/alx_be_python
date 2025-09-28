FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(Fahrenheit):
    return (Fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(Celsius):
    return Celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    temperature = float(input("Enter the temperature to convert: "))
    operation = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if operation == "C":
        convert = convert_to_celsius(temperature)
        print(convert)

    elif operation == F:
        convert = convert_to_fahrenheit(temperature)
        print(convert)

    else:
        print("Invalid temperature. Please enter a numeric value.")   

main() 
