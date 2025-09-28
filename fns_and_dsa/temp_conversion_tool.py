FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 * (temperature - 32)
CELSIUS_TO_FAHRENHEIT_FACTOR = (temperature * 9/5) + 32

def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR
    els

def convert_to_fahrenheit(celsius):
    return CELSIUS_TO_FAHRENHEIT_FACTOR

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
