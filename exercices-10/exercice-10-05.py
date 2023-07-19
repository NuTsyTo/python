# exo 10.5
# Créer une fonction nommée `compare()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoie une valeur de type `int`
# - renvoie 1 si `a` est plus grand que `b`
# - renvoie -1 si `a` est plus petit que `b`
# - renvoie 0 si `a` et `b` sont égaux
# Appelez la fonction et affichez le résultat

# réponse 10.5

def compare(a: float, b: float):
    if a > b:
        return '1'
    elif a < b:
        return '-1'
    else:
        return '0'

resultat = compare(9.15, 3.14)
print(resultat)

r = compare(1.23, 3.14)
print(r)

result = compare(1.23, 1.23)
print(result)
