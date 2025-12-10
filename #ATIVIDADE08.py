#ATIVIDADE08
peso,altura=float(input('Digite o seu peso em kilograma (EX:80): ')),float(input('Digite sua altura em metros (EX:1.8): '))


IMC=peso/(altura*altura)
if IMC <  19.1:
    print('Abaixo do peso')
elif IMC <25.9
    print('Peso normal')
else:
    print('Acima do peso')
    