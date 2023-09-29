# Verificar se o número digitado é primo
n=int(input("insira um número: "))
i=1
c=0
while i<=n:
    if n%i==0:
        c=c+1
        i=i+1 
    else:
        i=i+1
if c==2:
    print("o número é primo")
else:
    print("O número não é primo")

# Relação de pertinência -> n pertence ao conjunto dos primos