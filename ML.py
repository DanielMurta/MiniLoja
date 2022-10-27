def cabecalho_loja():
    print('='*30)
    print('   BEM-VINDO A MINI LOJA')
    print('='*30)


def menu_loja():
    print('MENU:')
    print('COMIDAS [1]     ROUPAS     [3]')
    print('BEBIDAS [2]     BRINQUEDOS [4]')


lista_de_compras = []
cabecalho_loja()
while True:
    print('_'*30)
    menu_loja()
    print()
    valor_total = sum(lista_de_compras)
    if valor_total != 0:
        print(f'O valor parcial da sua compra é R${valor_total:.2f}')
    escolha_menu = int(input('O que deseja comprar? (0 para finalizar compra): '))
    if escolha_menu == 0:
        break
    while True:
        if escolha_menu == 1:
            print('_'*50)
            print('MENU COMIDAS:')
            print('[1] ARROZ - R$4,99  -- [2] FEIJÃO - R$5,59'
                  '\n[3] PÃO   - R$5,49  -- [4] FRANGO - R$11,99'
                  '\n[5] Carne - R$25,50 -- [6] QUEIJO - R$15,97')

            print()
            selecao_de_comidas = int(input('Selecione o produto: ').strip())
            if selecao_de_comidas == 1:
                lista_de_compras.append(int(input('Quantidade de ARROZ: ')) * 4.99)
            elif selecao_de_comidas == 2:
                lista_de_compras.append(int(input('Quantidade de FEIJÃO: ')) * 5.59)
            elif selecao_de_comidas == 3:
                lista_de_compras.append(int(input('Quantidade de LEITE: ')) * 5.49)
            elif selecao_de_comidas == 4:
                lista_de_compras.append(int(input('Quantidade de FRANGO: ')) * 11.99)
            elif selecao_de_comidas == 5:
                lista_de_compras.append(int(input('Quantidade de CARNE: ')) * 25.50)
            elif selecao_de_comidas == 6:
                lista_de_compras.append(int(input('Quantidade de QUEIJO: ')) * 15.97)
            else:
                print('Esse número digitado não corresponde a nenhuma produto!')

        elif escolha_menu == 2:
            print('_'*50)
            print('MENU BEBIDAS')
            print('[1] LEITE - R$4,69 -- [2] REFRIGERANTE 2L - R$9,50'
                  '\n[3] SUCO  - R$3,59 -- [4] CAFÉ            - R$1,99')

            print()
            selecao_de_bebidas = int(input('Selecione o Produto: ').strip())
            if selecao_de_bebidas == 1:
                lista_de_compras.append(int(input('Quantidade de LEITE: ')) * 4.69)
            elif selecao_de_bebidas == 2:
                lista_de_compras.append(int(input('Quantidade de REFRIGERANTE: ')) * 9.5)
            elif selecao_de_bebidas == 3:
                lista_de_compras.append(int(input('Quantidade de SUCO: ')) * 3.59)
            elif selecao_de_bebidas == 4:
                lista_de_compras.append(int(input('Quantidade de CAFÉ: ')) * 1.99)
            else:
                print('Esse número digitado não corresponde a nenhuma produto!')


        r = str(input('Deseja continuar comprando?[S/N]: ')).strip().upper()
        if r == 'N':
            break
print(lista_de_compras)
valor_total = sum(lista_de_compras)
print(f'Valor total: R${valor_total:.2f}')
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
