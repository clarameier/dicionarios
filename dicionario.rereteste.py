estado = dict()
br = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    br.append(estado.copy())
for e in br:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
for e in br:
    for v in e.values():
        print(v, end=' ')
    print()