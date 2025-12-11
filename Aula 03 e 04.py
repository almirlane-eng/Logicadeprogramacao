#ATIVIDADE 03
nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo", "Fernanda"]
print("Lista original de nomes:", nomes)

posicao = int(input("Digite a posição (0 a 5) do nome que quer remover: "))
nome_removido = nomes.pop(posicao)  # ou del nomes[posicao]
print(f"Nome removido: {nome_removido}")
print("Lista após remover:", nomes)

fruta = input("Digite o nome de uma fruta: ")
pos_fruta = int(input(f"Digite a posição (0 a {len(nomes)}) onde quer inserir a fruta: "))
nomes.insert(pos_fruta, fruta)
print("Lista final com a fruta:", nomes)