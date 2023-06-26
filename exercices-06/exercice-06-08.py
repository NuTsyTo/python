# exo 6.8
# Calculez la somme des nombres de la liste et affichez le résultat
#
# ATTENTION : ne pas utiliser la fonction sum()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42]

# réponse 6.8
# total = my_list[0] + my_list[1]
# print(total)

total = 0
for somme in range(len(my_list)):
    total = total + my_list[somme]
print("Somme des éléments de la liste:", total)

