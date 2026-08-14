eng2sp = dict()
print(eng2sp)

eng2sp['one'] = "uno"
print(eng2sp)

eng2sp = {
    'one': 'uno',
    'two': 'dos',
}
print(eng2sp)
print(eng2sp['two'])

print('uno' in eng2sp)

# CONTAGEM DE LETRAS

def count_letters(s):
    d = dict() # {}
    for c in s: # s = uva | c = "u"
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

dict_contagem = count_letters("uva")
print(dict_contagem)


