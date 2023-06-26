import random

# if True:
#     print("ce message s'affichera toujours")

# if False:
#     print("ce message ne s'affichera jamais")

# number1 = random.randint(0, 10)
# number2 = random.randint(0, 10)
# print(f'{number1 = }')
# print(f'{number2 = }')

# if number1 < number2:
#     print("Number1 est plus petit que number2")
# else: 
#     print("la varaible Number1 est plus grande ou égale à number2")

# if number1 < number2:
#     print("Number1 est plus petit que number2")
# elif number1 > number2:
#     print("la varaible Number1 est plus grande que number2")
# else:
#     print("les deux variables Number1 et number2 sont égales")
# elif == else if

# block if4
# réécriture du block if3 avec des if imbriqués
# if number1 < number2:
#     print("Number1 est plus petit que number2")
# else:
#     if number1 > number2:
#     print("la varaible Number1 est plus grande que number2")






# Opérateurs booléens

# négation
# print(not True)
# print(not False)

# Table de vérité de l'opération de négation
# A     not A
# True False
# False True

# OU logique
# print(True or True)
# print(True or False)
# print(False or True)
# print( False or False)

#Table de vérité de l'opération OU logique
# A    B        A or B
#True  True     True
#True  False    True
#False True     True
#False False    False

# pour retrouver la table, remplacer :
# -A par "j'ai du cash"
# -B par "j'ai ma CB"
# -"A or B" par "puis-je faire mes courses ?"

# ET logique
# print(True and True)
# print(True and False)
# print(False and True)
# print( False and False)

#Table de vérité de l'opération ET logique
# A    B        A and B
#True  True     True
#True  False    False
#False True     False
#False False    False

#pour retrouver la table, remplacer:
# - A par "j'ai coupé l'électricité"
# - B par "j'ai coupé l'eau"
# - "A et B" par "je peux partir 3 mois en vacances"

#Table de vérité de l'opération NAND logique
# A    B        A and B       not (A and B)
#True  True     True          False
#True  False    False         True
#False True     False         True
#False False    False         True

# utilisation de l'opérateur AND pour voir si une variable est dans un interval de valeurs


# syntaxe alternative spécifique à Python
# Équivalent de : age >= 12 and age <= 25
# print(12 <= age <= 25)

# OU EXCLUSIF
# print(True ^ True)
# print(True ^ False)
# print(False ^ True)
# print(False ^ False)

# Table de vérité de l'opérateur XOR
# A    B        A XOR B
#True  True     False
#True  False    True
#False True     True
#False False    False

# Exo course (opérateur OU logique)
# Afficher : 
    # - "je peux aller faire les courses", si on a au moins un moyen de paiement
    # - "je ne peux pas aller faire les courses", si je n'ai aucun moyen de paiement


# import random
# has_cash = bool(random.randint(0, 1))
# has_cb = bool(random.randint(0, 1))

# print(f'{has_cash = }')
# print(f'{has_cb = }')

# if has_cash or has_cb:
#     print(" je peux aller faire mes courses")
# else :
#     print("je ne peux pas aller faire mes courses")

# Exo courses (opérateur ET logique)
# remplicer le même cahier des charges mais avec l'opérateur ET
# if (has_cash and not has_cb) or (has_cb and not has_cash) or (has_cash and has_cb):
#     print(" je peux aller faire mes courses")
# else:
#     print("je ne peux pas aller faire les courses")

    # CORECTION
    # CORECTION DITE NAIVE 
# if has_cash == False and has_cb == False:
#     print("je ne peux pas aller faire les courses")
# else: 
#    print("je peux aller faire les courses")

#     # CORECTION PLUS RAPIDE
# if not has_cash and not has_cb:
#     print("je ne peux pas aller faire les courses")
# else:
#     print("je peux aller faire les courses")

# combinaison d'opérateur AND et OR (ET et OU), IL FAUT (OBLIGATOIREMENT) DES () pour avoir un ordre de priorité.
# user_level = 1
# user_xp = 0
# user_social = 0

# if user_level >= 3 and user_xp >= 100 or user_social >= 100:
#     print("le joueur peut acheter du matériel")
# else: 
#     print("le joueur ne peut pas acheter de matériel")

# EXO CARTE DE RÉDUCTION
# determinez la carte de réduction auquelle le voyageur a droit:
# - entre 0 et 11 ans (inclus), le voyageur a droit à la gratuité
# - entre 12 et 25 ans (inclus), le voyageur a droit à une réduction de 50%
# - entre 26 et 64 ans (inclus), le voyageur a droit à une réduction de 10%
# - au delà de 65 ans (inclus), le voyageur a droit à une réduction de 50%
age = random.randint(0, 99)
print(age)

if age >= 0 and age <= 11:
    print("le voyageur a droit à la gratuité")

elif age >= 12 and age <= 25:
    print("le voyageur a droit à 50%")

elif age >= 26 and age <= 64:
    print("le voyageur a droit à 10%")
else: #age >= 65
    print("le voyageur a droit à 50%")
