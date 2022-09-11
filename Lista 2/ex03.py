"""Implemente uma função que verifique se um valor é primo."""

def verificaNumeroPrimo():

    number = int(input('Numero: '))
    ePrimo = 0

    for i in range(1, (number + 1)):        
        if number % i == 0:
            ePrimo += 1
        
    if ePrimo  == 2 :
        print('primo')
    else:
        print('nao primo')

verificaNumeroPrimo()