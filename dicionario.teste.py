pessoas = {'nome': 'maria', 'sexo': 'feminino', 'idade': '19'} #dicionário
print('='*100)
print(pessoas)
print('='*100)
print(pessoas['nome'])
print('='*100)
print(pessoas['idade'])
print('='*100)
print(pessoas['sexo'])
print('='*100)
print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print('='*100)
print(pessoas.keys()) #mostra as chaves
print('='*100)
print(pessoas.values()) #mostra as variáveis/valores
print('='*100)
print(pessoas.items()) #mostra os elementos (chaves com variáveis) separados
print('='*100)
for k in pessoas.keys():
    print(k) #mostra as chaves de forma ordenada
print('='*100)
for k, v in pessoas.items():
    print(f'{k} = {v}') #mostra as chaves e as variáveis de forma ordenada
print('='*100)
