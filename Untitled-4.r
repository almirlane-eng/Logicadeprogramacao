print("calculo de bolsa UNIASSELVI")
n1 = float(input("digite a nota 1:"))
n2 = float(input("digite a nota 2:"))
n3 = float(input("digite a nota 3:"))
n4 = float (input("digite a nota 4:"))

media = (n1 + n2 + n3 + n4 + n5)/5
print(f"\nmédia do enem: {media:.2f}")

if media <= 450
    desconto = 0.20

elif 451 <= media <= 550
    desconto = 0.30

elif 551 <= media <= 600
    desconto = 0.35

elif 601 <= media <= 650
    desconto = 0.40

elif 651 <= media <= 700
    desconto =  0.50

else desconto = 1000

mensalidade_sem_desconto = 1000
mensalidade_com_desconto = mensalidade_sem_desconto * (1 - desconto)
economia_anual = (mensalidade_sem_desconto - mensalidade_com_desconto) * 12


