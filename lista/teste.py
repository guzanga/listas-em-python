fruta = ["maçã", "banana", "abacaxi", "uva"]

#exemplo de alteração de variavel na lista
fruta[3] = "melancia"

#append adiciona uma variavel ao final de uma lista
fruta.append("laranja")

#adiciona um elemento a qq lugar da lista
fruta.insert(0, "morango")

#exclui algum elemento de uma lista
del fruta[3]


#apaga o ultimo elemento, se colocar a posição dentro do pareteses ele apaga o da posição
fruta.pop()


#verifica se um elemento exte em uma lista
if "abacaxi" in fruta:
    fruta.remove("abacaxi")
else:
    print("não encontrado")

print(fruta)

#cria uma lista
num = list(range(1,7))
print(num)

#ordena uma lista
#num2.sort(remove = true) organiza em ordem decrecente, isso vale para strings
num2= [1,3,2,5,7,5,3]
num2.sort()
print(num2)

#somar elementos de uma lista
soma = sum(num2)
print(soma)

#para achar o maior ou o menor numero dentro de uma lista, isso vale para achar a maior letra do ou menor do alfabeto
maior = max(num2)
menor = min(num2)
print(maior)
print(menor)
#para pegar a maior palavra de uma lista se utilza o max(fruta, key=len) e para o min, a mesma coisa


#usuario adciona numeros a uma lista
num3 = []
while True:
    num3.append(int(input("digite um numero")))
    res = str(input("digite N para sair"))

    if res in "Nn":
        break
    print("estes são os numeros", num3)





