jogadora = dict()
partidas = list()

jogadora['nome'] = str(input('Nome da jogadora: '))
tot = int(input(f'Quantas partidas a {jogadora["nome"]} jogou? '))

for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jogadora['gols'] = partidas[:]
jogadora['total'] = sum(partidas)

print('='*100)
print(jogadora)
print('='*100)

for a, b in jogadora.items():
    print(f'{a} = {b}')

print('='*100)

print(f'A jogadora {jogadora["nome"]} jogou {len(jogadora["gols"])} partidas.')
for c, b in enumerate(jogadora['gols']):
    print(f' -> na partida {c}, fez {b} gols.')
print(f'Foi um total de {jogadora["total"]} gols.')