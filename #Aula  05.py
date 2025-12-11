#ATIVIDADE 05
lista_numeros = [45, 12, 78, 34, 90, 23, 56, 1, 67]

print("Lista original:", lista_numeros)

# Ordem crescente
crescente = lista_numeros.copy()  # ou sorted(lista_numeros)
crescente.sort()
print("Ordem crescente:", crescente)

# Ordem decrescente
decrescente = lista_numeros.copy()
decrescente.sort(reverse=True)
print("Ordem decrescente:", decrescente)

# Ou de forma mais curta:
print("Crescente (com sorted):", sorted(lista_numeros))
print("Decrescente (com sorted):", sorted(lista_numeros, reverse=True))
