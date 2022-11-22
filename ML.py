import Defs

Defs.cabecalho_loja()
while True:
    print('_'*30)
    Defs.menu_loja()
    print()
    Defs.ListasComprasParcial()
    escolha_menu = str(input('O que deseja comprar? \033[36m(0 p/ finalizar compra)\033[m: '))
    if escolha_menu.isdigit():
        escolha_menu = int(escolha_menu)

        if escolha_menu == 0:
            break
        while True:
            if escolha_menu == 1:
                Defs.MenuComidas()

            elif escolha_menu == 2:
                Defs.MenuBebidas()

            elif escolha_menu == 3:
                Defs.MenuRoupas()

            elif escolha_menu == 4:
                print('\033[4;33mSEÇÃO EM CONSTRUÇÃO!\033[m')


            else:
                print('\033[4;31mEsse número não corresponde a nenhuma seção!\033[m')
                print()
            r = str(input('Deseja continuar comprando?[S/N]: ')).strip().upper()
            if r == 'N':
                break
            while r != 'S':
                print('\033[4;31mDigite uma opção válida\033[m! ')
                r = str(input('Deseja continuar comprando?[S/N]: ')).strip().upper()
                if r == 'N':
                    break
            if r == 'N':
                break
    else:
        print('Digite um número')

print('_'*50)
Defs.ListaComprasFinal()
while True:
    if Defs.ListaComprasFinal() == 0:
        break
    else:
        print('-'*28)
        print('\033[7;40m À vista DINHEIRO    [1]\033[m\n\033[7;40m À vista no cartão       [2]\033[m\n\033[7;40m Em até 2x no cartão '
            '    [3]\033[m\n\033[7;40m 3x ou mais no cartão    [4]\033[m')
        print('-'*28)
        CP = int(input('Qual a condição de pagamento? '))
        if CP == 1:
            print()
            #print("Com desconto de 10% o valor será de R${:.2f}".format(valor_total - (valor_total*0.1)))

            break
        elif CP == 2:
            print()
            #print('Com desconto de 5% o valor será de R${:.2f}'.format(valor_total - (valor_total*0.05)))
            break
        elif CP == 3:
            print()
            #print('R${:.2f} parcelado em 2x'.format(valor_total))
            break
        elif CP == 4:
            print()
            while True:
                parcela = int(input('Nº Parcelas: '))
                if parcela <= 2:
                    print('O valor da parcela deve ser acima de 3x.')
                else:
                    break

            print('_'*50)
            print('Sua compra será parcelada em {}x.'.format(parcela))
            #print('O total será R${:.2f} com juros de 20%.'.format(valor_total + valor_total*0.2))
            break
        else:
            print("\033[4;30;41m Opção inválida de pagamento. Tente novamente! \033[m")

Defs.volte_sempre()
