# importation du module random pour les nombres aléatoires
import random

# opérateurs composés
b = 0

# incrémentation
b += 1
b += 1 #veut dire en gros d'ajouter 1 à la valeur de base
print(b)

# décrémentation, l'inverse d'invrémentation.
b -= 1
print(b)

# multiplication
c = 3
# c = c * 2
print (c)

# division
d = 10
# d = d / 3
d /=3
print(d)

# division entière, (exactement comme la division mais ça l'arrondie)
d = 10
# d = d // 3
d //= 3
print (d)

# opération d'inclusion
text1 = "lorem ipsum"

result = "e" in text1
print(result)
print("e" in text1)

list1 = ["lorem", "ipsum"]
print("e" in list1)
print("lorem" in list1)

#comparaison avec des nombres aléatoires
e = random.randint(0, 100)
f= random.randint(0, 100)

print(f'{e = }')
print(f'{f = }')

result = e == f
print(result)

result = e < f
print(result)

# Est une expression 
# 1 + 1 -> 2
# (100 + 2) * 3 -> 102 * 3 -> 306
# 1 + 1 > (100 + 2) * 3 -> 2 > 306 -> false
# random.randint(0, 100) -> 100

# Pas une expression
# print(100)