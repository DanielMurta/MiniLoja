def cabeçalho_loja():
    print('='*21)
    print('BEM-VINDO A MINI LOJA')
    print('='*21)


def menu_loja():
    print('MENU:')
    print('COMIDAS [1]     ROUPAS     [3]')
    print('BEBIDAS [2]     BRINQUEDOS [4]')


cabeçalho_loja()
while True:
    print('_'*30)
    menu_loja()
    print()
    escolha_menu = int(input('O que deseja comprar? (0 para finalizar compra): '))
    if escolha_menu == 0:
        break
    lista_de_compras = []
    while True:
        if escolha_menu == 1:
            print('_'*30)
            print('MENU COMIDAS:')
            print('[1] ARROZ - R$4,99 -- '
                '[2] FEIJÃO - R$5,59')

        seleção_de_comidas = int(input('Selecione o produto: '))
        if seleção_de_comidas == 1:
            lista_de_compras.append(int(input('Quantidade de ARROZ: ')) * 4.99)
        elif seleção_de_comidas == 2:
            lista_de_compras.append(int(input('Quantidade de FEIJÃO: ')) * 5.59)



        r = str(input('Deseja continuar comprando?[S/N]: ')).strip().upper()
        if r == 'N':
            break
print(lista_de_compras)
valor_total = sum(lista_de_compras)
print(f'O valor total da sua compra é R${valor_total:.2f}')
print('-'*30)
print('À vista DINHEIRO/CHEQUE [1]\nÀ vista no cartão       [2]\nEm até 2x no cartão '
      '    [3]\n3x ou mais no cartão    [4]')
print('-'*30)
CP = int(input('Qual a condição de pagamento? '))
if CP == 1:
    print("Com desconto de 10% o valor será de R${:.2f}".format(valor_total - (valor_total*0.1)))
elif CP == 2:
    print('Com desconto de 5% o valor será de R${:.2f}'.format(valor_total - (valor_total*0.05)))
elif CP == 3:
    print('R${:.2f} parcelado em 2x'.format(valor_total))
elif CP == 4:
    parcela = int(input('Nº Parcelas: '))
    print('Sua compra será parcelada em {}x.'.format(parcela))
    print('O total será R${:.2f} com juros de 20%.'.format(valor_total + valor_total*0.2))
else:
    print("Opção inválida de pagamento. Tente novamente!")
