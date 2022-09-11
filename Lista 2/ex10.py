def calculaTabuada():
    a = int(input('informe um número: '))
    b = int(input('informe um número: '))
    i = b


    for b in range (1, a + 1):
            
        for a in range (1, i + 1):

            resultado = a * b

            print(str(b) + " X " + str(a) + " = " + str(resultado))  
