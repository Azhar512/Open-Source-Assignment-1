def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

# Example usage:
celsius = 25
fahrenheit = celsius_to_fahrenheit(celsius)
kelvin = celsius_to_kelvin(celsius)

print(f"{celsius}°C is equal to {fahrenheit}°F and {kelvin} K")
