def validaSenha(senhaCorreta):
    qtdVezes = 2
    i = qtdVezes
    tentativaSenha = []

    while i >= 1:
        senha = input("Digite sua senha: ")
        tentativaSenha.append(senha)

        if senha == senhaCorreta:
            print("Login realizado com sucesso")
            break
        
        elif senha != senhaCorreta:
            i = i - 1

            if i == 0:
                print("Tente mais tarde!!")
                break

            else:
                print("Você erro, mas ainda tem " + str(i) + " tentativas")

        

validaSenha("Amora")