import time

def convert_temperature(Fahrenheit, Celcius):
       Fahrenheit = Celcius * 9.0 / 5.0 +32
       Celcius = (Fahrenheit - 32) * 5.0 / 9.0
       return Fahrenheit, Celcius
print("Welcome to the temperature converter.")
time.sleep(1)

input_direction = input("To which direction do you want to convert? (C to F or F to C): ")
time.sleep(1)

if input_direction == "C to F":
    input_value = float(input("Enter the temperature value to be converted: "))
    fahrenheit, _ = convert_temperature(None, input_value)
    print(f"The temperature in Fahrenheit is: {fahrenheit:.2f} F")
elif input_direction == "F to C":
    input_value = float(input("Enter the temperature value to be converted: "))
    _, celsius = convert_temperature(input_value, None)
    print(f"The temperature in Celsius is: {celsius:.2f} C")
    
else:
    print("Error: Invalid direction. Please enter 'C to F' or 'F to C'.")
