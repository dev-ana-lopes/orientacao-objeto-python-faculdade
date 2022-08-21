"""Implemente um programa que, a partir de um valor informado pelo usuário,
imprima “positivo” caso o valor digitado seja maior ou igual a zero, ou “negativo”
caso o valor digitado seja menor que zero."""

valor = int(input('Digite um valor: '))

if valor > 0:
    print(str(valor) + " Positivo")
    
else:
    print(str(valor) + " Negativo")