celsius = lambda c: (c * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = celsius(celsius)
print(f"{celsius}°C is equivalent to {fahrenheit}°F.")
