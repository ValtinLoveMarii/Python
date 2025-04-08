#Aula 28 - Dicionário  

dicio = {"chave":"Valor 1", "chave2":"valor 2"}
# print(dicio)

dicio2 = {
    "nome":"Madara", 
    "Idade":17,    
    "naruto":17,
    "modelo":"sasuke"
}

dicio2.update({"nome":"Tobirama"})
dicio2.update({"city":"konoha"})
dicio2.pop("nome")
print(dicio2)
#-------------------- MÉTODOS
# print(len(dicio2))
# print(dicio2.keys())
# print(dicio2.values())
# print(dicio2.items())

# if 'Idade' in dicio2:
#     print('Tem')
# l = []
# for i in dicio2.values():
#     print(i)
#     l.append(i)
# print(l)