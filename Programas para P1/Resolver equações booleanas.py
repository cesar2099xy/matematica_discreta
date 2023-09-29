# Utilizando uma biblioteca para resolver as expressões e gerar output em tabela verdade
import ttg

#Através dessa biblioteca é possível resolver expressões. Limitei o input em 3 variáveis.
#Função valuation() classifica a última coluna da tabela como tautologia, contradição ou continência


print("Na hora de escrever sua expressão, utilize os seguintes simbolos:\n"
"\nNegação: 'not''\n"
"Disjunção: 'or'\n"
"Conjunção: 'and'\n"
"implicância: '=>'\n"
"biconditional: '='\n"
"exemplo: a and not b => a \n")

exp = input("Utilizando as variáveis a,b e c, insira a equação boleana: ")
a=ttg.Truths(['a','b','c'],[exp])
print(a)
a.valuation()
print(a.valuation())