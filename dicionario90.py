final = dict()
situ = list()

final['nome'] = str(input('Nome da(o) aluna(o): '))
final['media'] = float(input('Média das notas: '))
if final['media'] >= 7:
    final['resultado'] = 'Aprovado!'
elif 5 <= final['media'] < 7:
    final['resultado'] = 'Recuperação!'
else:
    final['resultado'] = 'Reprovado!'
situ.append(final.copy())
print('='*100)

for b, c in final.items():
    print(f'{b} é igual a {c}')
