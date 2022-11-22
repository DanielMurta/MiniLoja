lista_de_compras = []
def ListasComprasParcial():
    valor_parcial = sum(lista_de_compras)
    if valor_parcial != 0:
        print(f'O valor parcial da sua compra é \033[32mR${valor_parcial:.2f}\033[m')


def ListaComprasFinal():
    valor_total = sum(lista_de_compras)
    print(f'Valor total: R$\033[32m{valor_total:.2f}\033[m')

def cabecalho_loja():
    print('\033[30;41m \033[m'*30)
    print('\033[30;41m    BEM-VINDO A MINI LOJA     \033[m')
    print('\033[30;41m \033[m'*30)


def menu_loja():
    print('\033[30;47m MENU: \033[m')
    print('\033[4mCOMIDAS [1]\033[m     \033[4mROUPAS     [3]\033[m \n\033[4mBEBIDAS [2]\033[m     '
          '\033[4mBRINQUEDOS [4]\033[m')


def volte_sempre():
    print()
    print('\033[30;42m \033[m'*30)
    print('\033[30;42m        VOLTE SEMPRE!         \033[m')
    print('\033[30;42m \033[m'*30)


def MenuComidas():
    print('_' * 50)
    print('\033[40m MENU COMIDAS: \033[m')
    print('[1] ARROZ - R$4,99  -- [2] FEIJÃO - R$5,59'
          '\n[3] PÃO   - R$5,49  -- [4] FRANGO - R$11,99'
          '\n[5] CARNE - R$25,50 -- [6] QUEIJO - R$15,97')

    print()
    selecao_de_comidas = int(input('Selecione o produto: ').strip())
    if selecao_de_comidas == 1:
        lista_de_compras.append(int(input('[ARROZ (1kg)] Quantidade: ')) * 4.99)
    elif selecao_de_comidas == 2:
        lista_de_compras.append(int(input('[FEIJÃO (1kg)] Quantidade: ')) * 5.59)
    elif selecao_de_comidas == 3:
        lista_de_compras.append(int(input('[PÃO] Quantidade: ')) * 5.49)
    elif selecao_de_comidas == 4:
        lista_de_compras.append(int(input('[FRANGO (kg)] Quantidade: ')) * 11.99)
    elif selecao_de_comidas == 5:
        lista_de_compras.append(int(input('[CARNE (kg)] Quantidade: ')) * 25.50)
    elif selecao_de_comidas == 6:
        lista_de_compras.append(int(input('[QUEIJO (kg)] Quantidade: ')) * 15.97)
    else:
        print('\033[31mEsse número digitado não corresponde a nenhuma produto!\033[m')


def MenuBebidas():
    print('_' * 50)
    print('\033[40m MENU BEBIDAS: \033[m')
    print('[1] LEITE - R$4,69 -- [2] REFRIGERANTE 2L - R$9,50'
          '\n[3] SUCO  - R$3,59 -- [4] CAFÉ            - R$1,99')

    print()
    selecao_de_bebidas = int(input('Selecione o Produto: ').strip())
    if selecao_de_bebidas == 1:
        lista_de_compras.append(int(input('[LEITE (1L)] Quantidade: ')) * 4.69)
    elif selecao_de_bebidas == 2:
        lista_de_compras.append(int(input('[REFRIGERANTE] Quantidade: ')) * 9.5)
    elif selecao_de_bebidas == 3:
        lista_de_compras.append(int(input('[SUCO (1L)] Quantidade: ')) * 3.59)
    elif selecao_de_bebidas == 4:
        lista_de_compras.append(int(input('[CAFÉ (400G)] Quantidade: ')) * 1.99)
    else:
        print('\033[31mEsse número digitado não corresponde a nenhum produto!\033[m')


def MenuRoupas():
    print('_' * 50)
    print('\033[40m MENU ROUPAS: \033[m')
    print('[1] CAMISA - R$29,90 -- [2] CALÇA  - R$45,99'
          '\n[3] MEIA   - R$ 9,99 -- [4] CASACO - R$69,90')

    selecao_de_roupas = int(input('Selecione o Produto: ').strip())
    if selecao_de_roupas == 1:
        lista_de_compras.append(int(input('[CAMISA] Quantidade: ')) * 29.9)
    elif selecao_de_roupas == 2:
        lista_de_compras.append(int(input('[CALÇA] Quantidade: ')) * 45.99)
    elif selecao_de_roupas == 3:
        lista_de_compras.append(int(input('[MEIA] Quantidade: ')) * 9.99)
    elif selecao_de_roupas == 4:
        lista_de_compras.append(int(input('[CASACO] Quantidade: ')) * 69.9)
    else:
        print('\033[31mEsse número digitado não corresponde a nenhum produto\033[m')