def verificar_nota(nota):
    while notaA < 0 or notaA > 10:
        print("A nota deve estar entre 0 e 10")
        nota = float(input("Digite a nota novamente: "))
    return nota


notaA = float(input('Digite a primeira nota: '))
notaA = verificar_nota(notaA)

notaB = float(input('Digite a segunda nota: '))
notaB = verificar_nota(notaB)

media = (notaA + notaB) / 2
print(media)