# 0 --> SAIR DO PROGRAMA
# 1 --> ENTRAR NO PROGRAMA
# NENHUM --> ERRO

escolha_usuario = 0

match escolha_usuario:
    case 0:
        print("Sair do programa")
    case 1:
        print("Entrar do programa")
    case _:
        print("Erro!!")
