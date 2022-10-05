#teste1
pessoas = {'nome': 'maria', 'sexo': 'feminino', 'idade': '19'} #dicionário
del pessoas['sexo'] #apaga o elemento escolhido
for k, v in pessoas.items():
    print(f'{k} = {v}') #mostra as chaves e as variáveis de forma ordenada
print('='*100)

#teste2
persona = {'nome': 'mário', 'sexo': 'masculino', 'idade': '20'} #dicionário
persona['nome'] = 'joão' #altera o nome mário para joão
for k, v in persona.items():
    print(f'{k} = {v}') #mostra as chaves e as variáveis de forma ordenada
print('='*100)

#teste2
persona = {'nome': 'mário', 'sexo': 'masculino', 'idade': '20'} #dicionário
persona['peso'] = '78.45' #adiciona uma chave e uma variável no dicionário
for k, v in persona.items():
    print(f'{k} = {v}') #mostra as chaves e as variáveis de forma ordenada
print('='*100)

#teste3
brasil = []
estado1 = {'uf': 'rio de janeiro', 'sigla': 'rj'}
estado2 = {'uf': 'são paulo', 'sigla': 'sp'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil) #aparece os dois dicionários
print(brasil[1]) #aparece apenas o segundo dicionário da lista
print(brasil[0]['uf']) #aparece apenas a variável "uf" do primeiro dicionário
print('='*100)