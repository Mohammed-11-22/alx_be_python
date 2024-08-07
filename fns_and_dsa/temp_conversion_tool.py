FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32
    return fahrenheit
def main():
    temperature_input = input("Enter the temperature to convert: ")
    if temperature_input.replace('.', '', 1).isdigit() or (temperature_input.startswith('-') and temperature_input[1:].replace('.', '', 1).isdigit()):
        temperature = float(temperature_input)
    else:
        print("Invalid temperature. Please enter a numeric value.")
        return
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
if __name__ == "__main__":
    main()