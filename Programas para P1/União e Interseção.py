#união e interseção
x = input("Digite os elementos do 1° conjunto: ")
y = input("Digite os elementos do 2° conjunto: ")
c1 = x.split(",")
c2 = y.split(",")
uniao =[]
intersecao = set(c1) & set(c2)
for a in c1:
    uniao.append(a)
for b in c2:
    uniao.append(b)
uniao = set(uniao)
print(f"Interseção: {intersecao}")
print(f"União: {uniao}")
