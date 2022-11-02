def cabecalho_loja():
    print('='*30)
    print('  \033[4;30;46m BEM-VINDO A MINI LOJA \033[m')
    print('='*30)


def menu_loja():
    print('\033[45m MENU: \033[m')
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
        print(f'O valor parcial da sua compra é \033[32mR${valor_total:.2f}\033[m')
    escolha_menu = int(input('O que deseja comprar? \033[33m(0 p/ finalizar compra)\033[m: '))
    if escolha_menu == 0:
        break
    while True:
        if escolha_menu == 1:
            print('_'*50)
            print('\033[40m MENU COMIDAS: \033[m')
            print('[1] ARROZ - R$4,99  -- [2] FEIJÃO - R$5,59'
                  '\n[3] PÃO   - R$5,49  -- [4] FRANGO - R$11,99'
                  '\n[5] Carne - R$25,50 -- [6] QUEIJO - R$15,97')

            print()
            selecao_de_comidas = int(input('Selecione o produto: ').strip())
            if selecao_de_comidas == 1:
                lista_de_compras.append(int(input('Quantidade: ')) * 4.99)
            elif selecao_de_comidas == 2:
                lista_de_compras.append(int(input('Quantidade: ')) * 5.59)
            elif selecao_de_comidas == 3:
                lista_de_compras.append(int(input('Quantidade: ')) * 5.49)
            elif selecao_de_comidas == 4:
                lista_de_compras.append(int(input('Quantidade: ')) * 11.99)
            elif selecao_de_comidas == 5:
                lista_de_compras.append(int(input('Quantidade: ')) * 25.50)
            elif selecao_de_comidas == 6:
                lista_de_compras.append(int(input('Quantidade: ')) * 15.97)
            else:
                print('\033[31mEsse número digitado não corresponde a nenhuma produto!\033[m')

        elif escolha_menu == 2:
            print('_'*50)
            print('\033[40m MENU BEBIDAS: \033[m')
            print('[1] LEITE - R$4,69 -- [2] REFRIGERANTE 2L - R$9,50'
                  '\n[3] SUCO  - R$3,59 -- [4] CAFÉ            - R$1,99')

            print()
            selecao_de_bebidas = int(input('Selecione o Produto: ').strip())
            if selecao_de_bebidas == 1:
                lista_de_compras.append(int(input('Quantidade: ')) * 4.69)
            elif selecao_de_bebidas == 2:
                lista_de_compras.append(int(input('Quantidade: ')) * 9.5)
            elif selecao_de_bebidas == 3:
                lista_de_compras.append(int(input('Quantidade: ')) * 3.59)
            elif selecao_de_bebidas == 4:
                lista_de_compras.append(int(input('Quantidade: ')) * 1.99)
            else:
                print('\033[31mEsse número digitado não corresponde a nenhum produto!\033[m')

        elif escolha_menu == 3:
            print('_'*50)
            print('\033[40m MENU ROUPAS: \033[m')
            print('[1] CAMISA - R$29,90 -- [2] CALÇA  - R$45,99'
                  '\n[3] MEIA   - R$ 9,99 -- [4] CASACO - R$69,90')

            selecao_de_roupas = int(input('Selecione o Produto: ').strip())
            if selecao_de_roupas == 1:
                lista_de_compras.append(int(input('Quantidade: ')) * 29.9)
            elif selecao_de_roupas == 2:
                lista_de_compras.append(int(input('Quantidade: ')) * 45.99)
            elif selecao_de_roupas == 3:
                lista_de_compras.append(int(input('Quantidade: ')) * 9.99)
            elif selecao_de_roupas == 4:
                lista_de_compras.append(int(input('Quantidade: ')) * 69.9)
            else:
                print('\033[31mEsse número digitado não corresponde a nenhum produto\033[m')



        r = str(input('Deseja continuar comprando?[S/N]: ')).strip().upper()
        if r == 'N':
            break
print('_'*50)
valor_total = sum(lista_de_compras)
print(f'Valor total: R${valor_total:.2f}')
print('-'*30)
print('\033[7;40mÀ vista DINHEIRO/CHEQUE [1]\033[m\n\033[7;40mÀ vista no cartão       [2]\033[m\n\033[7;40mEm até 2x no cartão '
      '    [3]\033[m\n\033[7;40m3x ou mais no cartão    [4]\033[m')
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
