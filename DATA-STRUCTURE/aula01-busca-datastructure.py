def busca_sequencial(lista, procurado):
    for i in range(len(lista)):
        if lista[i] == procurado:
            return i
    return -1
nome = ["Mariana", "jose", "joão", "benedito", "Geraldo", "Antonio"]

posicao = busca_sequencial(nome, "joão")

print(posicao)

