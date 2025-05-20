#  Write a program that will convert various temperatures.
#   Fahrenheit to Centigrade
#   Centigrade to Fahrenheit

# Fahrenheit to Celsius conversion
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

