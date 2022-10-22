Preço = float(input('Preço do produto:R$ '))
print('-'*30)
print('À vista DINHEIRO/CHEQUE [1]\nÀ vista no cartão       [2]\nEm até 2x no cartão '
      '    [3]\n3x ou mais no cartão    [4]')
print('-'*30)
CP = int(input('Qual a condição de pagamento? '))
if CP == 1:
    print("Com desconto de 10% o valor será de R${:.2f}".format(Preço - Preço*0.1))
elif CP == 2:
    print('Com desconto de 5% o valor será de R${:.2f}'.format(Preço - Preço*0.05))
elif CP == 3:
    print('R${:.2f} parcelado em 2x'.format(Preço))
elif CP == 4:
    parcela = int(input('Quantas parcelas? :'))
    print('Sua compra será parcelada em {}x.'.format(parcela))
    print('O total será R${:.2f} com juros de 20%.'.format(Preço + Preço*0.2))
else:
    print("Opção inválida de pagamento. Tente novamente!")