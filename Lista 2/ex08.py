def calculaPotencia(a, b):
    i = 1
    resultado = 0 

    while b >= i:
        potencia = a * a
        resultado = resultado + potencia
        i = i + 1

        if b == i:
            print("Resultado: " + str(resultado))
            break
    

calculaPotencia(12, 2)
