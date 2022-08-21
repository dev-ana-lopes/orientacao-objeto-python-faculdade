"""Implemente um programa que recebe como entrada uma temperatura em
Fahrenheit e converta para Celsius."""

fahrenheit = float(input("Informe uma temperatura em Fahrenheit: "))

celsius = round((fahrenheit - 32)/1.8, 2)

print(str(celsius) + "° Celsius")