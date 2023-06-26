"""# # Exo 1.1
# print("programme démarré")

# # Exo 1.2
# print('programme terminé')

# # Exo 2.1
# answer = 42
# golden_ratio = 1.61
# fullname = "Salut Maxence Degaugue"
# love_python = True
# licence_agreement = None
# print(answer)
# print(golden_ratio)
# print(fullname)
# print(love_python)
# print(licence_agreement)

# # Exo 2.2
# number1 = 2
# number1_float = float(number1)
# print(number1_float)

# # Exo 2.3
# number2 = 2.7182
# number2_int = int(number2)
# print(number2_int)

# Exo 2.4
# number3 = 2.7182
# number3_rounded = round(2.7182/ 1, 2)
# print(number3_rounded)

# number3_int = int(number3_rounded)
# print(number3_int)

# # Exo 2.5
# number4 = 3.1415
# number4_rounded = round(3.1415/ 1, 0)
# print(number4_rounded)

# number4_int = int(number4_rounded)
# print(number4_int)
"""


"""# Exo 3.1
# birthyear = 1988
# year = 2023
# print(year - birthyear)"""

# Exo 3.2
# candies = 15
# chocolates = 17
# friends = 3
# chocolates_rest = (chocolates / friends) 
# candies_rest = (candies / friends)
# print(chocolates_rest)
# print(candies_rest)

# # EXO 3.3
# candies_per_person = (candies // friends)
# print(candies_per_person)
# chocolates_per_person = (chocolates / friends) - (chocolates // friends) 
# print(chocolates_per_person)

""" # EXO 4.1
# import random
# number = random.randint(0, 5)
# print(number)
# if number == 1:
#     print("le nombre est égal à 1")
# else:
#     print("le nombre est différent de 1")

# # EXO 4.2
# import random
# number = random.randint(0, 9)
# print(number)

# if (number % 2) == 0:
#     print("le nombre est pair")
# else:
#     print("le nombre est impair")

# EXO 4.3
# import random
# number = random.randint(0, 9)
# print(number)

# if (number % 3)==0:
#     print("le nombre est divisible par 3")
# else:
#     print("le nombre n'est pas divisible par 3")

# EXO 4.4
# import random
# number = random.randint(0, 9)
# print(number)

# if (number >= 5):
#     print("le nombre est supérieur ou égal à 5")
# else:
#     print("le nombre est inférieur à 5")

#EXO 4.5 
# import random
# number = random.randint(0, 99)
# print(number)

# if (number >=0 and number <= 49):
#     print("le nombre est compris entre 0 et 49 inclus")
# else:
#     print("le nombre n'est pas compris entre 0 et 49 inclus")

#EXO 4.6
# import random
# number = random.randint(0, 99)
# print(number)

# if (number >=0 and number <= 33):
#     print("le nombre est compris entre 0 et 33 inclus")
# elif (number >= 34 and number <= 66):
#     print("le nombre est compris entre 34 et 66 inclus")
# else:
#     print("le nombres est pas compris entre 0 et 66 inclus")

# EXO 4.7
# import random
# a = random.randint(0, 99)
# print(a)

# b= random.randint( 0, 99)
# print(b)

# if (a) > (b):
#     print("le nombre est supérieur au nombre B")
# if (a) < (b):
#     print("le nombre est inférieur au nombre B")
# if (a) == (b):
#     print("les deux nombres A et B sont égaux")

#EXO 4.8
# import random
# mails = random.randint(0, 5)
# print(mails)

# if (mails) == 0:
#     print(" Il n'y a aucun mail")
# if (mails) == 1:
#     print(" IL y a un nouveau mail")
# elif(mails):
#     print(f"Il y a {mails} nouveaux mails") """

""" # EXO 5.1
# def multiplication(a: float, b: float) -> float:
#     return a * b 
# help(multiplication)

# EXO 5.2
# my_text = ""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
# Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
# Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
# Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""

# print(my_text.find('minim'))

#EXO 5.3
# my_text = ""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
# Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
# Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
# Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""
# print(len(my_text))
# my_text1 = my_text [12 : 21]

# print(my_text1)

#EXO 5.4 
# my_text = ""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
# Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
# Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
# Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""

# list1 = my_text.split(" ")
# print(list1[5])

#EXO 5.5
# my_text = ""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
# Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
# Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
# Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""

# print(my_text.count("\n"))"""

""" #EXO 6.1
# my_list = [1, 11.14, "hey", True]
# print(my_list)

#EXO 6.2
# my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']
# print(my_list[3])

# #EXO 6.3
# my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']
# my_list.insert(5, 'toto')
# print(my_list)

#EXO 6.4
# my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']
# del my_list[1]
# print(my_list)

#EXO 6.5
# my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']
# number = 11
# my_list[1] = number
# print(my_list)

#EXO 6.6
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']
print (len(my_list))"""

# EXO 6.7 
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']
my_list2 = ['bar', 'lorem']
my_list[1] = my_list[3]
my_list[3] = my_list2[0]
print(my_list)

#EXO 6.8
my_list = [2.71, 42]

print(my_list)