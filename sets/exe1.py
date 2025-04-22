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
print(animais)

#EX3 - Verifique se o item "cachorro" está no set animais e imprima o resultado (True ou False).
animais = list(animais)
for i in animais:
    if 'cachorro' in animais:
        print('EXISTE')
        break
    else:
        continue

#EX4 - Crie dois sets: a = {1, 2, 3} e b = {3, 4, 5}. Imprima a união deles.
set1 = {1,2,3}
set2 = {2,7,8}
set1 = set1.union(set2)
print(set1)

#EX5 - Imprima a interseção entre os sets a e b.
a = {1,4,5,3}
b = {3,5,4,12,32}
c = a & b # OU c = a.interssesion(b)
print(c)

#EX6 - Esvazie o set a e imprima o set.
a.clear()
print(a)