def verificaSenha(senha):
    max, min = 15, 10
    tamanhoSenha = len(senha)

    if tamanhoSenha >= max and tamanhoSenha <= min:
        print("O número de caracter não corresponde com o solicitado")
    
    else:
        print("Senha Cadastrada")


verificaSenha("asdfghjkl")