"""Implemente um programa que leia dois valores inteiros, A e B e troque os valores
de maneira que A possua o valor de B e B possua o valor de A. Imprima o
resultado na tela."""

a, b = 2, 3

a = a + b
b = a - b
a = a - b

print("a = " + str(a) + " b = " + str(b))
