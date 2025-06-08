ننFAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    try:
        temp_input = input("ادخل درجة الحرارة: ")
        temp = float(temp_input)
        unit = input("هل الدرجة بالـ (C) سلسيوس أم (F) فهرنهايت؟ اكتب C أو F: ").strip().upper()
        if unit == 'C':
            converted = convert_to_fahrenheit(temp)
            print(f"{temp} درجة سلسيوس = {converted:.2f} درجة فهرنهايت")
        elif unit == 'F':
            converted = convert_to_celsius(temp)
            print(f"{temp} درجة فهرنهايت = {converted:.2f} درجة سلسيوس")
        else:
            print("خطأ: الرجاء إدخال وحدة صحيحة إما C أو F.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

