
.. index:: conseil

==========================================
Quelques conseils pour écrire un programme
==========================================

Des petites fonctions
=====================

Pour plusieurs raisons :

* Il est plus facile de corriger un programme qui est constitué
  de petites fonctions plutôt que de quelques grandes.
  Chaque fonction peut être vérifiée séparément.
* Il est plus facile de réutiliser des petites fonctions.
* Il est plus facile de répartir le travail sur plusieurs personnes.

Pas de variables globales
=========================

Il vaut mieux éviter les variables globales qui sont
considérées que comme des paramètres cachés.
Il faut réécrire le programme dès qu'on veut répéter le même
code avec différentes valeurs pour cette variable globale.

::

    vglob = 0

    def un_calcul(a=0):
        global vglob
        return a + vglob

    loops = [un_calcul(a) for a in range(0, 10)]

Comment faire une boucle sur la valeur de ``vglob`` ?
Quelque soit la solution choisie, faire une boucle
sur la variable globale requiert quelques contorsions.
Les variables globales sont à éviter avec les threads.

Séparer les calculs, le chargement des données, l'interface graphique
=====================================================================

Pour plusieurs raisons :

* Il est plus facile de vérifier un calcul s'il est
  dans une fonction indépendante plutôt que caché dans le
  code d'une interface graphique.
* C'est facile de faire un calcul une fois lorsqu'un utilisateur
  appuie sur un bouton, si on veut faire ce calcul cent fois,
  on ne peut pas lui demander d'appuyer cent fois sur le même bouton.
* Les calculs ou le chargement des données peuvent être utilisés
  dans d'autres programmes.

Utiliser des fonctions de tests
===============================

Ces fonctions peuvent être exécutées au début du programme
pour vérifier que certaines parties du programme fonctionnent
toujours même après les avoir modifiées.

L'exemple suivant considère une fonction qui doit retourner une
somme réelle même si les éléments de la liste sont entiers.
On écrit la fonction qui vérifie cela.

::

    def somme_double (liste) :
        return 1.0 * sum(liste)

    def test_somme_double () :
        y = somme_double([ 1 ]) / 2
        if y == 0 : raise Exception ("valeur > 0 attendue")

    if __name__ == "__main__" :
        test_somme_double()

Si plus tard, quelqu'un modifie la fonction ``somme_double``
en enlevant la multiplication parce qu'il considère cela
inutile. La fonction de test provoquera une erreur.
Elle est là pour rappeler que la fonction a été programmée
pour retourner un nombre réel et que quiconque l'utilise
s'attend à ce qu'elle retourne ce type de résultat.

::

    Traceback (most recent call last):
      File "conseil.py", line 10, in <module>
        test_somme_double()
      File "conseil.py", line 7, in test_somme_double
        if y == 0 : raise Exception ("valeur > 0 attendue")
    Exception: valeur > 0 attendue

Trucs et astuces
================

**Moteurs de recherche**

Lorsqu'on ne comprend un message d'erreur,
il est souvent utile de recopier le texte dans un moteur
de recherche (Google, Bing, ...). Il est très rare de ne pas
réussir à trouver d'indices.

**Partager du code**

Il existe aujourd'hui des solutions qui permettent
d'éviter les envois de programme par email. Le plus utilisé
pour les librairies open source est `GitHub <https://github.com/>`_.
