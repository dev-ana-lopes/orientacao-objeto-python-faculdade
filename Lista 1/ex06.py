"""Implemente um algoritmo que conte quantos valores primos existem entre um
intervalo fechado [a, b]."""

def verificaNumeroPrimo(a, b):

    count = 0
    
    for i in range(a, b + 1):
        
        if i == 1:
            verf = False
    
        else:
            verf = True
        
        for j in range(2, b + 1):
            
            if i % j == 0 and i != j:
                
                verf = False
                
                break 
            
        if verf:
            count += 1

    print("Existem " + str(count) + " números primos no intervalo fechado [" + str(a) + ", " + str(b) + "]")

                

verificaNumeroPrimo(1, 20)        