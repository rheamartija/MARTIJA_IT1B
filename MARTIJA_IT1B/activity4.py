#fahrenheit to celsius converter

fah = eval(input("Enter temperature in FAHRENHEIT:"))

c = ((fah - 32) * 5) / 9

print(round(c,2))

print(f"{fah} degrees in Fahrenheit coverted to celsius is {round(c,2)}")