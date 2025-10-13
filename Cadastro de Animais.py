from datetime import date
data_atual = date.today()
animal = dict()
grupo = list()
print('-=-= CADASTRO VETERINÁRIA =-=-')
while True:
    grupo.clear()
    animal['Nome'] = str(input('Digite o nome do animal: ')).upper()
    print("""Tipos de animais:
          [1]Peixes
          [2]Mamíferos
          [3]Anfíbios
          [4]Aves
          [5]Repteis""")
    while True:
        animal['Tipo'] = int(input('Digite o tipo do animal: [1 a 5]'))
        if animal['Tipo'] < 6:
            break
        print('Erro! Digite apenas as opções 1,2,3,4 ou 5.')
    while True:
        animal['Sexo'] = str(input('Digite o sexo do animal: [M/F]')).upper()[0]
        if animal['Sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F.')
    while True:
        animal['Vacinado'] = str(input('Vacinado? [S/N]')).upper()[0]
        if animal['Vacinado'] in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    while True:
        animal['Descrição'] = str(input('Descreva a situação do animal: ')).upper()
        campo = 10
        if len(animal['Descrição']) > campo:
            break
        print('Erro! Preencha a descrição com o mínimo 10 caracteres...')
    grupo.append(animal.copy())
    while True:
        resp = str(input('Realizar outro cadastro? [S/N]')).upper()[0]
        if resp in 'SN':
            break
            print('Erro! Digite apenas Sim ou Não.')
    if resp == 'N':
        break
print('-='*50)
print(f'Animais cadastrados dia: {data_atual.day} / {data_atual.month} / {data_atual.year}')
print('-='*50)
for i in animal.keys():
    print(f'{i:<15}', end='')
print()
print('-'*100)
for k, v in enumerate(grupo):
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()



