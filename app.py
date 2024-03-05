import pandas as pd
import openpyxl 
import random

tabela_nomes = pd.read_excel('planilha_nomes (1).xlsx')
qntd_linhas_tabela_nomes = len(tabela_nomes)
# print(tabela_nomes)
# print(qntd_linhas_tabela_nomes)

# lista_nomes = []
# for linha in enumerate(tabela_nomes):
#     _, nome, *_ = linha
#     print(nome)
#     lista_nomes.append(nome)
# print(lista_nomes)


tabela_sobrenomes = pd.read_excel('planilha_sobrenomes (1).xlsx')
qntd_linhas_tabela_sobrenomes = len(tabela_sobrenomes)
# print(tabela_sobrenomes)
# print(qntd_linhas_tabela_sobrenomes)

# lista_sobrenomes = []
# for linha in enumerate(tabela_sobrenomes):
#     _, sobrenome, *_ = linha
#     print(sobrenome)
#     lista_sobrenomes.append(sobrenome)
# print(lista_sobrenomes)



lista_nomes_completos = []
nome = None
sobrenome_1 = None
sobrenome_2 = None

while True:
    try:
        qntd_nomes = int(input('Quantos nomes você deseja? '))
        break
    except:
        print('Digite apenas números!\n')
        continue

for i in range(qntd_nomes):

    linha_random_nome = random.randint(1, qntd_linhas_tabela_nomes-1)
    nome = tabela_nomes.iloc[linha_random_nome, 0]
    # nome = random.choice(tabela_nomes)
    # print(nome)
    
    linha_random_sobrenome_1 = random.randint(0, qntd_linhas_tabela_sobrenomes-1)
    sobrenome_1 = tabela_sobrenomes.iloc[linha_random_sobrenome_1, 0]
    # sobrenome_1 = random.choice(tabela_sobrenomes)

    # print(sobrenome_1)

    while True:
        linha_random_sobrenome_2 = random.randint(1, qntd_linhas_tabela_sobrenomes-1)
        sobrenome_2 = tabela_sobrenomes.iloc[linha_random_sobrenome_2, 0]
        # sobrenome_2 = random.choice(tabela_sobrenomes)

        # print(sobrenome_2)
        
        if sobrenome_2 == sobrenome_1:
            continue
        break

    nome_completo = f'{nome} {sobrenome_1} {sobrenome_2}'

    # nova_linha = pd.DataFrame([nome_completo], columns=tabela_nomes_aleatorios.columns)
    # tabela_nomes_aleatorios = tabela_nomes_aleatorios.append(nova_linha, ignore_index=True)

    lista_nomes_completos.append(nome_completo)
    # print(nome_completo)

# print()
# print(lista_nomes_completos)

dataframe = pd.DataFrame(lista_nomes_completos, columns=['Nomes'])
dataframe.to_excel('planilha_nomes_aleatorios.xlsx', index=False)
tabela_nomes_aleatorios = pd.read_excel('planilha_nomes_aleatorios.xlsx')
print()
print(tabela_nomes_aleatorios)