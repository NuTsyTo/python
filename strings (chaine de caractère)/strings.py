text1 = "lorem"
text2 = 'ispum'

# Concaténation
text3 = text1 + " " + text2
print(text3)

# Interpolation avec une f-string
text3 = f"{text1} {text2}"
print(text3)

# ATTENTION la concaténation ne fonctionne qu'avec des str,
# Solution : convertir les autres types en STR
mails = 52
text4 = "Vous avez " + str(mails) + " non lus"
print(text4)

# Répétition de texte
text5 = "foo " * 3
print(text5)

# Affichage de valeurs arrondies mais sans arrondir la variable
number1 = 10 / 3
text6 = f"10 / 3 est à peu près {number1:.2f}"
print(text6)

# Les fonctions associées aux strings
text7 = "foo bar baz foo"

#len = calculer la taille d'une chaine de caractère
print(len(text7))

# count = compter le nombre de fois ou le caractère choisi apparait
print(text7.count('foo'))  

# Retrouver l'emplacement d'un mot
# Chaque caractère  à une position, le 0 est le 1er emplacement
position = text7.find('foo')
print(position)

# Pour trouver l'occurence suivante, il faut chercher une position plus loin
print(text7.find('foo', position + 1))

# Si le mot est absent, la fonction renvoie -1
position = text7.find('lorem')
print(position)

# Remplacement de mots
text7 = text7.replace('foo', 'lorem')
print(text7)

# split & join
list1 = text7.split(' ')
print(list1)

text8 = "_".join(list1)
print(text8)

# Documenter une fonction = ajouter un commentaire

def ouiNon(value):
    """Cette fonction renvoie :
    - "oui" si la paramètre passé est True
    - "non" si la paramètre passé est False
    - "" dans les autres cas
    
    value bool valeur qui sera transformée en "oui" ou "non"
    return str
    """

    if value == True:
        return "oui"
    elif value == False:
        return "non"

    return ""

# help(ouiNon)
print(ouiNon.__doc__)