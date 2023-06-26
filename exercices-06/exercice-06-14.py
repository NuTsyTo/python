# exo 6.14
# Créez une deuxième liste nommée `new_list` ne contenant que les nombres entiers de la liste
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]
print(my_list)
# réponse 6.14
number = 0

for number in my_list:
    # print(number)
    # print (type (number) is int)
    if type (number) is int:
        new_list = number
        print(new_list)
    # elif type (number) is int:
    #     new_list = [number]
    #     print(new_list)