FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def get_valid_temperature():
    while True:
        temp_input = input("Enter the temperature to convert: ")
        try:
            return float(temp_input)
        except ValueError:
            print("❌ Invalid temperature. Please enter a numeric value.")

def get_valid_unit():
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ['C', 'F']:
            return unit
        else:
            print("❌ Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

def main():
    temperature = get_valid_temperature()
    unit = get_valid_unit()

    if unit == 'F':
        celsius = convert_to_celsius(temperature)
        print(f"{temperature:.2f}°F is {celsius:.2f}°C")
    else:  # unit == 'C'
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature:.2f}°C is {fahrenheit:.2f}°F")

if __name__ == "__main__":
    main()
