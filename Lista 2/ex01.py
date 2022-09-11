"""Implemente uma função que verifique se um número é par. Utilizando essa
função, crie uma outra para identificar se um número é ímpar."""

def verificaSeEhPar(num):

    if num % 2 == 0:
        par = True
        print("É par")
    
    else:
        par = False

    return par

def verificaSeEhimpar(num):
    
    par = verificaSeEhPar(num)
    
    if  par == False:
       print("È impar") 

verificaSeEhPar(10)
verificaSeEhimpar(15)
