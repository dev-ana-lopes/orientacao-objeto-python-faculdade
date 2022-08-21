"""Oh, não! O seu sapo de estimação caiu no fundo de um poço que tem N metros
de profundidade. Infelizmente, você não conseguirá tirar ele de lá, portanto, ele
terá que sair sozinho. A cada dia, o sapo conseguirá subir M metros, mas ao final
do dia, por já estar sem forças, ele escorregará X% do que conseguiu subir no dia.
Desenvolva um algoritmo que leia N, M e X do usuário e responda quantos dias
seu sapo levará para sair do poço.
a. Valores para testes:
Se N = 10, M = 1 e X = 0.3, então a quantidade de dias deve ser 14.
Se N = 30, M = 1 e X = 0.5, então a quantidade de dias deve ser 59."""

def salvaSapo(n, m, x):
    dias = 0
    mDiario = m * (1 - x)
    mFaltantes = n - mDiario

    while mFaltantes > 0:
        
        mFaltantes = mFaltantes - mDiario
        dias = dias + 1
        
        if mFaltantes <= 0:
            break
    
        
    print(dias)
    
salvaSapo(10, 1, 0.3)