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
Defs.Pagamento()
print('-'*28)
Defs.volte_sempre()
