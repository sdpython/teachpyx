
#########
Questions
#########

.. _blog-class-ou-fonction:

C'est obligé d'utiliser les classes ?
======================================

*Monsieur, c'est obligé d'utiliser les classes ?*
C'est une question qu'on me pose chaque année
lors des projets informatiques
et je réponds chaque année que non, les classes
ne sont pas obligatoires mais qu'elles ont le don
de simplifier l'écriture des programmes.
Le lanage :epkg:`Python` propose une des syntaxes
les plus explicites par rapport à  d'autres langages
car il n'y a pas de paramètres cachés.
Le programme suivant calcule la somme et le produit
de deux entiers stockés dans un dictionnaire.

.. runpython::
    :showcode:

    def deux_entiers_somme(de):
        return de['i1'] + de['i2']

    def deux_entiers_multiplication(de):
        return de['i1'] * de['i2']

    de = {'i1': 3, 'i2': 2}
    s = deux_entiers_somme(de)
    m = deux_entiers_multiplication(de)
    print(s, m)

Les deux fonctions ne sont applicables qu'à  deux entiers.
Il paraît normal de les prÃ©fixer avec *deux_entiers*
pour signifier à celui qui les utiliser que ça ne sert
à rien de les utiliser pour autre chose.
Les classes permettent de regrouper formellement
ces deux fonctions.

.. runpython::
    :showcode:

    class DeuxEntiers:

        def somme(de):
            return de['i1'] + de['i2']

        def multiplication(de):
            return de['i1'] * de['i2']

    de = {'i1': 3, 'i2': 2}
    s = DeuxEntiers.somme(de)           # _ --> .
    m = DeuxEntiers.multiplication(de)  # _ --> .
    print(s, m)

On a juste remplacé le signe ``_`` par ``.`` qui signifie
que la fonction cherchée est dans la classe qui précède ``.``.
Comme les deux entiers en questions sont toujours liés
aux fonctions qui les manipulent, il paraît normal de les
inclure dans la classe.

.. runpython::
    :showcode:

    class DeuxEntiers:

        def __init__(self, de):   # on accroche les données à la classe
            self.de = de

        def somme(self):
            return self.de['i1'] + self.de['i2']

        def multiplication(self):
            return self.de['i1'] * self.de['i2']

    de = DeuxEntiers({'i1': 3, 'i2': 2})
    s = DeuxEntiers.somme(de)
    m = DeuxEntiers.multiplication(de)
    print(s, m)

Comme le concept a beaucoup plu aux informaticiens,
ils ont cherché à simplifier l'appel aux fonctions qu'ils
ont appelé des *méthodes* :

.. runpython::
    :showcode:

    class DeuxEntiers:

        def __init__(self, de):
            self.de = de

        def somme(self):
            return self.de['i1'] + self.de['i2']

        def multiplication(self):
            return self.de['i1'] * self.de['i2']

    de = DeuxEntiers({'i1': 3, 'i2': 2})
    s = de.somme()             # disparition de DeuxEntiers
    m = de.multiplication()    # disparition de DeuxEntiers
    print(s, m)

.. index:: attribut

Ensuite, ils se sont penchés sur la simplification de la représentation
des deux entiers ``{'i1': 3, 'i2': 2}``. Et s'ils Ã©taient considérés comme
des variables de la classe qui ont été renommés en *attributs*.

.. runpython::
    :showcode:

    class DeuxEntiers:

        def __init__(self, i1, i2):
            self.i1 = i1               # plus de dictionnaire
            self.i2 = i2

        def somme(self):
            return self.i1 + self.i2   # plus de dictionnaire

        def multiplication(self):
            return self.i1 * self.i2   # plus de dictionnaire

    de = DeuxEntiers(3, 2)             # plus de dictionnaire
    s = de.somme()
    m = de.multiplication()
    print(s, m)

Les classes permettent de regrouper formellement
les fonctions qui ne s'appliquent toujours aux mÃªmes
données. Plus encore, ce nouveau concept a permis d'en
introduire un autre, l':ref:`par_classe_heritage`, qui
permet de réutiliser certaines fonctions, d'en remplacer
d'autres et d'en ajouter pour une autre situation.

.. runpython::
    :showcode:

    class DeuxEntiers:

        def __init__(self, i1, i2):
            self.i1 = i1
            self.i2 = i2

        def somme(self):
            return self.i1 + self.i2

        def multiplication(self):
            return self.i1 * self.i2

    class DeuxEntiersModifies(DeuxEntiers):  # héritage

        def multiplication(self):
            return abs(self.i1 * self.i2)    # modifié

        def division(self):
            return abs(self.i1 / self.i2)    # ajouté

    de = DeuxEntiersModifies(-3, 2)
    s = de.somme()
    m = de.multiplication()
    d = de.division()
    print(s, m, d)

Cela peut paraît anodin mais la grande majorité des
programmeurs utilisent majoritairement les classes
une fois qu'ils les ont découvertes car elles
permettent d'organiser le code informatique
en bloc logique.
