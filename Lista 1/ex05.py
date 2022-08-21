"""Implemente um programa que calcule o mínimo múltiplo comum (m.m.c.) de dois
valores inteiros."""

x1 = int(input("informe um número inteiro:"))
x2 = int(input("informe outro número inteiro:"))

if x1 > x2:
    maior = x1
    
else:
    maior = x2
    
while True:
    
    if maior % x1 == 0 and maior % x2 == 0:
        print(maior)
        break
    
    else:
        maior += 1