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
    while True:
        if escolha_menu == 1:
            print('_'*30)
            print('MENU COMIDAS:')
            print('[1] ARROZ - R$4,99 -- '
                '[2] FEIJÃO - R$5,59')

        lista_de_compras = {}
        seleção_de_comidas = int(input('Selecione o produto: '))
        if seleção_de_comidas == 1:
            quant_de_arroz = int(input('Quantidade de ARROZ: '))
            lista_de_compras['arroz'] = valor_total_arroz = quant_de_arroz * 4.99
        elif seleção_de_comidas == 2:
            quant_de_feijao = int(input('Quantidade de FEIJÃO: '))
            lista_de_compras['feijao'] = valor_total_feijao = quant_de_feijao * 5.59

        r = str(input('Deseja continuar comprando?[S/N]: ')).strip().upper()
        if r == 'N':
            break
print(lista_de_compras)
#print('-'*30)
#print('À vista DINHEIRO/CHEQUE [1]\nÀ vista no cartão       [2]\nEm até 2x no cartão '
#      '    [3]\n3x ou mais no cartão    [4]')
#print('-'*30)
#CP = int(input('Qual a condição de pagamento? '))
#if CP == 1:
#    print("Com desconto de 10% o valor será de R${:.2f}".format(Preço - Preço*0.1))
#elif CP == 2:
#    print('Com desconto de 5% o valor será de R${:.2f}'.format(Preço - Preço*0.05))
#elif CP == 3:
#    print('R${:.2f} parcelado em 2x'.format(Preço))
#elif CP == 4:
#    parcela = int(input('Quantas parcelas? :'))
#    print('Sua compra será parcelada em {}x.'.format(parcela))
#    print('O total será R${:.2f} com juros de 20%.'.format(Preço + Preço*0.2))
#else:
#    print("Opção inválida de pagamento. Tente novamente!")
