def confirmaSenha():
    qtdVezes = 2
    i = qtdVezes

    while i >= 1:
        senha = input("Digite sua nova senha: ")

        confirmaSenha = input("Confirme sua nova senha: ")

        if senha != confirmaSenha:
            i = i - 1
            print("As senhas são diferentes, você ainda tem " + str(i) + " tentativas.")

        else:
            print("Parabéns, você confirmou sua senha.")
            break

confirmaSenha()