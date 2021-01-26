import os
os.system('cls')

'''
Primeira etapa do programa de estágio em Elixir na Stone
'''

# Criando um dicionário de dicionários de compras, para definir cada atributo do produto
lista_de_compras = {
    'item_1': {'leite': {'3 caixas': '399 por caixa'}},
    'item_2': {'ovos': {'30 unidades': '14 por unidade'}},
    'item_3': {'refrigerante': {'2 garrafas': '899 por garrafa'}},
    'item_4': {'macarrão': {'2 pacotes': '458 por pacote'}},
    'item_5': {'queijo branco': {'1 quilo': '1223 por quilo'}},
    'item_6': {'suco': {'3 garrafas': '735 por garrafa'}},
    'item_7': {'creme de leite': {'2 caixas': '280 por caixa'}},
    'item_8': {'azeite': {'1 garrafa': '1829 por garrafa'}},
    'item_9': {'iogurte': {'2 garrafas': '1098 por garrafa'}},
    'item_10': {'sabão em pó': {'1 caixa': '1999 por caixa'}},
    'item_11': {'miojo': {'12 unidades': '99 por unidade'}}
}

# Pode-se adicionar ou remover os itens da lista a qualquer momento

total = 0 # Aqui eu inicializo o valor total corrente das compras, que sempre começará zerado
for k, l in lista_de_compras.items():
    for x, y in l.items():
        for a, b in y.items():
            qtde = str(a.split(' ')[0]) # Extraindo a quantidade registrada na lista em cada produto
            preco = str(b.split(' ')[0]) # Extraindo também o preço do produto por unidade
            k2 = k.replace('_', ' ') # Tornando a saída mais legível...
            print(f'{k2.upper()}: {x} ({a}) - {b} - R${(int(qtde) * int(preco)/100):.2f}')
            total += int(qtde) * int(preco)
    print()

print(f'TOTAL: R${total/100:.2f}') # Optei por imprimir o valor em reais para ficar mais claro
print()

# Uma simples lista de e-mails
emails = ['isabela.rodrigues@stone.com', 'joice.nogueira@globo.com', 'joao.cardoso@gmail.com', 'douglas.ferreira@github.com', 'vitor.xavier@outlook.com', 'fernanda.medeiros@hotmail.com', 'willian.fernandes@ig.com', 'fernando.guedes@mds.gov.br', 'andre.brito@sensedia.com', 'juliana.marques@fgv.edu.br']

# Pode-se adicionar ou remover e-mails da lista a qualquer momento

def funcao_final(): # Esta função é o objetivo principal do programa
    dicio = dict()  # A princípio é um dicionário nulo
    for index in emails:
        dicio.update({index: total/len(emails)}) # Receberá cada e-mail da lista de e-mails como chave, e
    return dicio                                 # quanto cada pessoa deverá pagar para quitar a compra

print('|----------------TABELA----------------|') # Relatório final, mostrando os meus resultados
for x, y in funcao_final().items():
    print(f' {x}: R${round(y/100, 2)}')
    print()
print()