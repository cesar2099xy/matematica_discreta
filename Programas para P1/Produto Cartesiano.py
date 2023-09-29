#Produto Cartesiano

a = input("Informe os elementos do 1° conjunto (separado por vírgula)")
b = input("Informe os elementos do 2° conjunto (separado por vírgula)")

produto_cartesiano = []

for x in a:
    for y in b:
        produto_cartesiano.append((x,y))
print(produto_cartesiano)
