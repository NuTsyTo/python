# exo 7.18
# dans une boucle while, on tire un nombre entier `r` au hasard entre 1 et 100 inclus
# boucler jusqu'à ce que la valeur 100 soit tirée au hasard

import random

# réponse 7.18
r = random.randint(1, 101)

while True:
    r = random.randint(1, 101)
    print(r,)
    if r == 100:
        break  
