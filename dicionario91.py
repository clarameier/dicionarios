from random import randint
from time import sleep
from operator import itemgetter

print('='*100)

jogo = {'1° jogador': randint(1,6),
        '2° jogador': randint(1,6),
        '3° jogador': randint(1,6),
        '4° jogador': randint(1,6)}
ordem = dict()
print('Respectivos jogadores e valores sorteados: ')
for a, b in jogo.items():
        print(f'{a} tirou o valor {b} no dado.')
        sleep(1)

print('='*100)


ordem = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Em ordem do maior para o menor número tirado foi: ')
for c in ordem:
    print(f'{c}')

print('='*100)
