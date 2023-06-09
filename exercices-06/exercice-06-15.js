// exo 6.15
// Trouvez la chaîne de caractères la plus longue dans une liste.
// Affichez son index, sa valeur et sa longueur.
//
// ATTENTION : ne pas utiliser la fonction list.index()
// ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

let my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

// réponse 6.15

let index = null;
let valeur = "";
let longueur = 0;

for (let i = 0; i < my_list.length; i++) {
    // console.log(i);
    // console.log(my_list[i]);
    // console.log(my_list[i].length);
    // console.log();

    if (my_list[i].length > longueur) {
        // mise à jour 
        // ou stockage de la plus grande longueur 
        longueur = my_list[i].length;
        // stcokage des autres infos demandées
        index = i;
        valeur = my_list[i];
    }
}

// console.log(index);
// console.log(valeur);
// console.log(longueur);

// Boucle foreach qui permet de récupérer des valeurs mais pas l'index
// initialisation de l'index
let i = 0;

// reset des données (nécessaire car on à déjà le même algo au dessus)
index = null;
valeur = "";
longueur = 0;



for (let word of my_list){
    // console.log(i, word, word.length);
    // incrémentation de l'index
    if (my_list[i].length > longueur) {
        // mise à jour 
        // ou stockage de la plus grande longueur 
        longueur = my_list[i].length;
        // stcokage des autres infos demandées
        index = i;
        valeur = my_list[i];
    }

    i++;
}

console.log(index);
console.log(valeur);
console.log(longueur);
