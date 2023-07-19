# exo 10.6
# La formule suivante permet de convertir des mètres en miles :
#
#       miles = meters / 1609.344
#
# La formule suivante permet de faire l'inverse :
#
#       meters = miles * 1609.344
#
# Créez une fonction nommée :
#
# - meters_to_miles() permettant de convertir des mètres en miles
# - miles_to_meters() permettant de convertir des miles en mètres
#
# Ensuite convertissez les valeurs :
#
# - 1 Km en miles
# - 10 miles en mètres
#
# Appelez les fonctions et affichez les résultats

# réponse 10.6


def meters_to_miles(meters):
    miles = meters / 1609.344
    return miles

miles = meters_to_miles(1000)
print(miles)


def miles_to_meters(miles):
    meters = miles * 1609.344
    return meters

meters = miles_to_meters(10)
print (meters)