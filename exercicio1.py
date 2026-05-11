senha = input("Digite a senha: ")

# 1. Verifica o tamanho logo de cara
if len(senha) < 8:
    print("Senha muito curta!")
else:
    # 2. Se o tamanho estiver OK, vamos checar o resto
    tem_numero = False
    
    for letra in senha:
        if letra.isdigit(): # Verifica se a letra é um número
            tem_numero = True

    if tem_numero == True:
        print("Senha forte!")
    else:
        print("Falta um número na senha!")