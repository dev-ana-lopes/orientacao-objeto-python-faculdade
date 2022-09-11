"""Implemente uma função que verifique se um número informado pelo usuário é:
a. Somente divisível por 3;
b. Somente divisível por 5;
c. Divisível por 3 e por 5 ao mesmo tempo."""

def verificaDivisibilidade(num):
    
    if num % 3 == 0 and num % 5 == 0:
        print("Divisivel por 3 e por 5")
           
    elif num % 3 == 0:
        print("Divisivel por 3")
        
    elif num % 5 == 0:
        print("Divisivel por 5")
        

        
        
verificaDivisibilidade(10)
        
    