temperaturas = [[28, 31, 34, 33],
                [25, 27, 29, 28],
                [32, 35, 36, 34],
                [24, 26, 25, 27]]

for i, sala in enumerate(temperaturas):
    # print(sala)
    qtd_criticos = 0
    for temperatura in sala:
        # print(temperatura)
        if temperatura >= 33:
            qtd_criticos += 1

    media = sum(sala) / len(sala)
    print(f"Sala {i+1}")
    print(media)
    print(qtd_criticos)
    print()







