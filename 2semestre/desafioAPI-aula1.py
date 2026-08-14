endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500], #codigo http de /login
[200, 200, 200, 200, 200], #codigo http de /produtos
[201, 500, 502, 201, 500] #codigo http de /pedidos
]

# print(endpoints[1])
# print(status[1])

#FUNÇÃO QUE VERIFICA SE UM CODIGO HTTP DA REQUISICAO DE UM
#ENDPOINT É SUCESSO OU NÃO
# 200--> TRUE
# 401 ---> FALSE

def sucesso(codigo):
    return codigo >= 200 and codigo <= 299

# print(sucesso(200))

#FUNÇÃO QUE VERIFICA SE TEM 2 ERROS SEGUIDOS NA
# LISTA DE REQUISIÇÕES DE 1 ENDPOINT
#
# [200, 200, 401, 200, 500] --> FALSE (NÃO TEM 2 ERROS SEGUIDOS)
# [201, 500, 502, 201, 500] --> TRUE

def dois_erros_seg(lista_req):
    for i in range(len(lista_req)-1 ):
        codigo_atual = lista_req[i]
        prox_codigo = lista_req[i+1]

        if not sucesso(codigo_atual) and not sucesso(prox_codigo):
            return True
    return False

# print(erro(status[0]))

def analisar_endpoint(lista_req):
    qtd_sucessos = 0

    for codigo in lista_req:
        if sucesso(codigo):
            qtd_sucessos += 1

    qtd_total_req = len(lista_req)
    qtd_erros = qtd_total_req - qtd_sucessos
    percentual_sucessos = (qtd_sucessos/qtd_total_req)* 100


    tem_erros_seguidos = dois_erros_seg(lista_req)

    if tem_erros_seguidos:
        classficacao = "CRÍTICO"
    elif percentual_sucessos >= 80:
        classficacao = "ESTÁVEL"
    else:
        classficacao = "INSTÁVEL"

    return (qtd_sucessos, qtd_erros, percentual_sucessos, classficacao)

# PERCORRER A MATRIZ status

qtd_maior_erro = 0
endpoints_maior_erros = ""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    reqs_endpoints = status[i]

    sucessos, erros, percentual, classficacao = analisar_endpoint(reqs_endpoints)

    print(f" Endoint: {nome_endpoint}")
    print(f" Requisicoes: {reqs_endpoints}")
    print(f" Sucessos: {sucessos}")
    print(f" Erros: {erros}")
    print(f" Percentual de sucesso: {percentual}")
    print(f" Clasificacao: {classficacao}")
    print("-" *30)
    print()

if erros > qtd_maior_erro:
    qtd_maior_erro = erros
    endpoints_maior_erros = nome_endpoint

print(f" Endoint Maior erros: {endpoints_maior_erros}")




