"""Implemente um programa que calcule a área de:
a. um quadrado (tipo = 1);
b. um círculo (tipo = 2);
c. um triângulo (tipo = 3).
Nesse exercício é necessário criar uma variável do tipo int para verificar qual tipo de
área se está querendo calcular (quadrado, círculo ou triângulo). A partir do tipo definido
na variável, calcule a área e apresente o resultado."""
from math import pi

decide = int(input("Informe o número para calcular a área de (1)quadrado, (2)circulo e (3)triângulo: "))

if decide == 1:
    x = float(input("informe o comprimento do quadrado: "))
    area = x **2

elif decide == 2:
    raio = float(input("informe o raio do circulo: "))
    area = pi * raio **2
    
elif decide == 3:
    base = float(input("informe a base do triângulo: "))
    altura = float(input("informe a altura do triângulo: "))
    area = (base * altura) /2
    
print("A área solicitada é: " + str(round(area, 2)))