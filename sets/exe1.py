#AULA 29 - SETS

#EX1 - Crie um set chamado animais e adicione animais digitados pelo o usuário.
animais = {}
for i in range(3):
    animais = set(animais)
    animal = str(input('Digite um animal: '))
    animais.add(animal)

#EX2 - Remova o item "gato" do set animais.
animais = set(animais)
animais.discard('gato')
# print(animais)

# #EX3 - Verifique se o item "cachorro" está no set animais e imprima o resultado (True ou False).
animais = list(animais)
for i in animais:
    if 'cachorro' in animais:
        # print('EXISTE')
        break
    else:
        continue

# #EX4 - Crie dois sets: a = {1, 2, 3} e b = {3, 4, 5}. Imprima a união deles.
set1 = {1,2,3}
set2 = {2,7,8}
set1 = set1.union(set2)
# print(set1)

# #EX5 - Imprima a interseção entre os sets a e b.
a = {1,4,5,3}
b = {3,5,4,12,32}
c = a & b # OU c = a.interssesion(b)
# print(c)

# #EX6 - Esvazie o set a e imprima o set.
a.clear()
print(a)

# EX7  - Crie dois sets: pares = {2, 4, 6, 8, 10} e ímpares = {1, 3, 5, 7, 9}. Verifique se eles têm algum número em comum.
pares = {2, 4, 6, 8, 10}
impares = {1, 3, 5, 7, 9}

novo = pares.intersection(impares)
print(novo)

# EX8 - Crie um set com os números de 1 a 10. Remova todos os números pares usando um loop.
setinho = []
for i in range(3):
    n = int(input('Numero: '))
    setinho.append(n)
for x in setinho[:]:
    if x%2 == 0:
        setinho.remove(x)
    else:
        print('IMPAR')
setinho = set(setinho)
print(setinho)

# EX10 - Dado o set valores = {10, 20, 30, 40, 50}, remova o valor 30 apenas se ele existir no set.
valores = {10, 20, 30, 40, 50}
if 30 in valores:
    valores.remove(30)
print(valores)

# EX11 - Verifique se dois sets são disjuntos (não possuem elementos em comum) usando o método isdisjoint().
a = {1,2,3,5}
b = {2,3,5,12}
z = a.isdisjoint(b)
print(z)
if z == False:
    print('Existe algum valor igual!')
else:
    print('Não existe igualdade entre eles!')

#EX12 - Crie dois sets e verifique se um é subconjunto do outro usando issubset()
a = {1,3,4,5,6}
b = {5,6}
z = b.issubset(a)
print(z)

#EX13 - Dado o set nomes = {"Ana", "Lucas", "Carlos", "João"}, imprima o número de elementos no set.
nomes = {'mariana','marina', 'apollo', 'vivi'}
print(len(nomes))

#EX14 - Faça a união de três sets distintos e imprima o resultado ordenado (dica: use sorted()).
set1 = {1,5,120,1,678}
set2 = {12,78,2,933,411}
set3 = {4,5,12,6,799,12}
z = set1.union(set2, set3)
z = list(z)
z.sort()
print(z)

#EX15 - Dado um set com vários números, encontre o maior e o menor número.
maior = 0
menor = 99999999999999999999
set1 = {1,7,12,13123,909,125}
set1 = list(set1)
for x in set1[:]:
    if x > maior:
        maior = x
    if x < menor:
        menor = x
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
print(set(set1))