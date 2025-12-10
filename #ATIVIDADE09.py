#ATIVIDADE09
valor_compra=float(input('Digite o valor da compra: '))
if valor_compra>=350:
    if valor_compra>=700:
        print('frete gratis e brinde')
    else:
        print('frete gratis')
else:
    if valor_compra<=50:
        print('O valor do frete e de R$30')
    else:
        print('O valor do frete e de R$20')
        