total = 0
quantidade = 0

print("Digite o valor dos produtos.Digite 0 para finalizar a compra.\n")

while True:
    valor = float(input("Valor do produto:R$"))

    if valor == 0:
        break

    total += valor
    quantidade += 1

    print("\nquantidade de itens:, quantidade")
    print("Valor total da compra: R$",total)

    print("|informas de pagamento")

    if total < 50:
        print("debito")
        print("pix")


    elif 50 <= total <= 100:
        print("-Cartão de crédito (1x)")

    elif 100 < total <= 200:
        print("-Cartão de credito (até 2x)")

    else:
        print("_Cartão de crédito (até 3x)")





