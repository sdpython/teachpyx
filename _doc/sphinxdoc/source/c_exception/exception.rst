
.. _l-exception:

.. _chap_exception:

==========
Exceptions
==========

.. contents::
    :local:
    :depth: 2

.. index:: exception, division par zéro

Le petit programme suivant déclenche une erreur parce qu'il effectue une
division par zéro.

::

   x = 0
   y = 1.0 / x

Il déclenche une erreur ou ce qu'on appelle une *exception* :

::

   Traceback (most recent call last):
     File "cours.py", line 2, in ?
       y = 1.0 / x
   ZeroDivisionError: float division

Le mécanisme des exceptions permet au programme de "rattraper" les
erreurs, de détecter qu'une erreur s'est produite et d'agir en
conséquence afin que le programme ne s'arrête pas.

Principe des exceptions
=======================

Attraper toutes les erreurs
+++++++++++++++++++++++++++

Une exception est un objet qui indique que le programme ne peut continuer son exécution.
Le type de l'exception donne une indication sur le type de l'erreur rencontrée.
L'exception contient généralement un message plus détaillé.
Toutes les exceptions hérite du type
`Exception <https://docs.python.org/3/library/exceptions.html#Exception>`_.

On décide par exemple qu'on veut rattraper toutes les erreurs du
programme et afficher un message d'erreur. Le programme suivant appelle
la fonction qui retourne l'inverse d'un nombre.

::

   def inverse (x):
       y = 1.0 / x
       return y

   a = inverse(2)
   print(a)
   b = inverse(0)
   print(b)

.. index:: pile d'exécution, pile d'appels

Lorsque ``x == 0``, le programme effectue une division par zéro et
déclenche une erreur. L'interpréteur Python affiche ce qu'on appelle la
*pile d'appels* ou `pile d'exécution <https://fr.wikipedia.org/wiki/Pile_d%27ex%C3%A9cution>`_.
La pile d'appel permet d'obtenir la liste de toutes les fonctions pour remonter
jusqu'à celle où l'erreur s'est produite.

::

   Traceback (most recent call last):
     File "cours.py", line 8, in ?
       b = inverse (0)
     File "cours.py", line 3, in inverse
       y = 1.0 / x
   ZeroDivisionError: float division

Afin de rattraper l'erreur, on insère le code susceptible de produire
une erreur entre les mots clés `try <https://docs.python.org/3/reference/compound_stmts.html#try>`_
et `except <https://docs.python.org/3/reference/compound_stmts.html#except>`_.

.. index:: try, except

.. runpython::
    :showcode:

    def inverse (x):
        y = 1.0 / x
        return y

    try:
        a = inverse(2)
        print(a)
        b = inverse(0)  # déclenche une exception
        print(b)
    except:
        print("le programme a déclenché une erreur")

Le programme essaye d'exécuter les quatre instructions incluses entre
les instructions ``try`` et ``except``. Si une erreur se produit, le programme exécute
alors les lignes qui suivent l'instruction ``except``. L'erreur se produit en fait
à l'intérieur de la fonction mais celle-ci est appelée à l'intérieur
d'un code "protégé" contre les erreurs. Ceci explique les lignes affichées par le programme.
Il est aussi possible d'ajouter une clause qui sert de préfixe à une
liste d'instructions qui ne sera exécutée que si aucune exception n'est
déclenchée.

.. runpython::
    :showcode:

    def inverse (x):
        y = 1.0 / x
        return y

    try:
        print(inverse(2))  # pas d'erreur
        print(inverse(1))  # pas d'erreur non plus
    except:
        print("le programme a déclenché une erreur")
    else:
        print("tout s'est bien passé")

Ce dernier programme attrape l'erreur et affiche un message.
Ce programme ne s'arrête jamais, il ne *plante* jamais.
Pour résumer, la syntaxe suivante permet d'attraper toutes les erreurs
qui se produisent pendant l'exécution d'une partie du programme. Cette
syntaxe permet en quelque sorte de protéger cette partie du programme
contre les erreurs.

::

    try:
        # ... instructions à protéger
    except:
        # ... que faire en cas d'erreur
    else:
        # ... que faire lorsque aucune erreur n'est apparue

Toute erreur déclenchée alors que le programme exécute les instructions
qui suivent le mot-clé ``try`` déclenche immédiatement l'exécution des lignes
qui suivent le mot-clé ``except``. Dans le cas contraire, le programme
se poursuit avec l'exécution des lignes qui suivent le mot-clé
``else``. Cette dernière partie est facultative, la clause
``else`` peut ou non être présente. Le bout de code prévoit
ce qu'il faut faire dans n'importe quel cas.

Lorsqu'une section de code est protégée contre les exceptions,
son exécution s'arrête à la première erreur d'exécution.
Le reste du code n'est pas exécuté.
Par exemple, dès la première erreur qui correspond au calcul d'une
puissance non entière d'un nombre négatif, l'exécution du programme
suivant est dirigée vers l'instruction qui suit le mot-clé ``except``.

::

    def inverse (x):
        y = 1.0 / x
        return y

    try:
        print((-2.1) ** 3.1)  # première erreur
        print(inverse(2))
        print(inverse(0))     # cette ligne produirait une erreur
                              # mais le programme n'arrive jamais jusqu'ici
    except:
        print("le programme a déclenché une erreur")

Obtenir le type d'erreur, attraper un type d'exception
++++++++++++++++++++++++++++++++++++++++++++++++++++++

Parfois, plusieurs types d'erreurs peuvent être déclenchés à l'intérieur
d'une portion de code protégée. Pour avoir une information sur ce type,
il est possible de récupérer une variable de type
`Exception <https://docs.python.org/3/library/exceptions.html>`_.

.. runpython::
    :showcode:

    def inverse (x):
        y = 1.0 / x
        return y

    try:
        print(inverse(2))
        print(inverse(0))
    except Exception as exc:
        print("exception de type ", exc.__class__)
        # affiche exception de type  exceptions.ZeroDivisionError
        print("message", exc)
        # affiche le message associé à l'exception

Le programme précédent récupère une exception sous
la forme d'une variable appelée . Cette variable est en fait une
instance d'une classe d'erreur, ``__class__`` correspond au nom de cette classe. A
l'aide de la fonction ``isinstance``, il est possible d'exécuter des traitements
différents selon le type d'erreur.

.. runpython::
    :showcode:

    def inverse (x):
        y = 1.0 / x
        return y

    try:
        print((-2.1) ** 3.1)  # première erreur
        print(inverse(2))
        print(inverse(0))     # seconde erreur
    except Exception as exc:
        if isinstance(exc, ZeroDivisionError) :
            print("division par zéro")
        else:
            print("erreur insoupçonnée :", exc.__class__)
            print("message", exc)

L'exemple précédent affiche le message qui suit parce que la première
erreur intervient lors du calcul de ``(-2.1) ** 3.1``.
Une autre syntaxe plus simple permet d'attraper un type d'exception
donné en accolant au mot-clé ``except`` le type de l'exception qu'on désire
attraper. L'exemple précédent est équivalent au suivant mais
syntaxiquement différent.

.. index:: as

.. runpython::
    :showcode:

    def inverse (x):
        y = 1.0 / x
        return y

    try :
        print((-2.1) ** 3.1)
        print(inverse(2))
        print(inverse(0))
    except ZeroDivisionError:
        print("division par zéro")
    except Exception as exc:
        print("erreur insoupçonnée :", exc.__class__)
        print("message ", exc)

Cette syntaxe obéit au schéma qui suit.

.. mathdef::
    :title: Attraper une exception
    :tag: Syntaxe

    ::

       try:
           # ... instructions à protéger
       except type_exception_1:
           # ... que faire en cas d'erreur de type type_exception_1
       except (type_exception_i, type_exception_j):
           # ... que faire en cas d'erreur de type type_exception_i ou type_exception_j
       except type_exception_n:
           # ... que faire en cas d'erreur de type type_exception_n
       except:
           # ... que faire en cas d'erreur d'un type différent de tous
           #     les précédents types
       else:
           # ... que faire lorsque une erreur aucune erreur n'est apparue

Toute erreur déclenchée alors que le programme exécute les instructions qui suivent le mot-clé
``try`` déclenche immédiatement l'exécution des lignes qui suivent un mot-clé ``except``.
Le programme compare le type d'exception aux types ``type_exception_1`` à ``type_exception_n``.
S'il existe une correspondance alors ce sont les instructions de la clause ``except`` associée qui
seront exécutées et uniquement ces instructions. La dernière clause ``except`` est facultative,
elle est utile lorsque aucun type de ceux prévus ne correspond à l'exception
générée. La clause ``else`` est aussi facultative. Si la dernière clause ``except``
n'est pas spécifiée et que l'exception déclenchée ne correspond à aucune de celle
listée plus haut, le programme s'arrête sur cette erreur à moins que celle-ci ne soit attrapée plus tard.

Le langage Python propose une liste
d'`exceptions standards <https://docs.python.org/3/library/exceptions.html#base-classes>`_.
Lorsqu'une erreur ne correspond pas à l'une de ces exceptions,
il est possible de créer une exception propre à un certain type d'erreur.
Lorsqu'une fonction ou une méthode déclenche une
exception non standard, généralement, le commentaire qui lui est associé
l'indique. Quelques types d'exception courantes
documentée dans la section
`Concrete exceptions <https://docs.python.org/3/library/exceptions.html#concrete-exceptions>`_.
Certaines surviennent car le programme est mal écrit et l'interpréteur
ne peut le comprendre :

.. index:: IndentationError, SyntaxError

* **IndentationError** :
  L'interpréteur ne peut interpréter une partie du programme à cause
  d'un problème d'indentation. Il n'est pas possible
  d'exécuter un programme mal indenté mais cette erreur peut se produire
  lors de l'utilisation de la fonction
  `compile <https://docs.python.org/3/library/functions.html?highlight=compile#compile>`_.
* **SyntaxError** :
  Le programme a un problème de syntaxe comme une parenthèse en trop ou
  ou en moins.

Les deux suivantes surviennent lorsqu'on se trompe dans l'orthographe d'une
variable, une fonction, un module :

.. index:: AttributeError, NameError, ImportError

* **AttributeError** :
  Une référence à un attribut inexistant ou une affectation a échoué.
* **ImportError** :
  Cette erreur survient lorsqu'on cherche à importer un module qui n'existe pas,
  son nom est mal orthographié ou il n'est pas installé.
* **NameError** :
  On utilise une variable, une fonction, une classe qui n'existe pas.

Les erreurs très fréquentes, erreur d'indices, de types :

.. index:: IndexError, KeyError, TypeError, ValueError

* **IndexError** :
  On utilise un index erroné pour accéder à un élément d'une liste,
  d'un dictionnaire ou de tout autre tableau.
* **KeyError** :
  Une clé est utilisée pour accéder à un élément d'un dictionnaire
  dont elle ne fait pas partie.
* **TypeError** :
  Erreur de type, une fonction est appliquée sur un objet qu'elle n'est
  pas censée manipuler.
* **ValueError** :
  Cette exception survient lorsqu'une valeur est inappropriée pour une certaine
  opération, par exemple, l'obtention du logarithme d'un nombre négatif.

Les erreurs qui surviennent lorsqu'on travaille avec des fichiers :

.. index:: OSError, UnicodeError

* **OSError** :
  Une opération concernant les entrées/sorties (Input/Output) a échoué.
  Cette erreur survient par exemple lorsqu'on cherche à
  lire un fichier qui n'existe pas.
* **UnicodeError** :
  Erreur de conversion d'un `encodage <https://fr.wikipedia.org/wiki/Codage_des_caract%C3%A8res>`_
  de texte à un autre. C'est une erreur qui survient régulièrement quand on travaille
  avec des langues qui ont des accents (non anglophones).

Lancer une exception
++++++++++++++++++++

.. index:: raise

Lorsqu'une fonction détecte une erreur, il lui est possible de
déclencher une exception par l'intermédiaire du mot-clé ``raise``.
La fonction ``inverse``
compare ``x`` à ``0`` et déclenche l'exception ``ValueError`` si ``x`` est nul.
Cette exception est attrapée plus bas.

.. runpython::
    :showcode:

    def inverse (x):
        if x == 0 :
            raise ValueError
        y = 1.0 / x
        return y

    try:
        print(inverse(0))  # erreur
    except ValueError:
        print("erreur de type ValueError")

Il est parfois utile d'associer un message à une exception afin que
l'utilisateur ne soit pas perdu. Le programme qui suit est identique au
précédent à ceci près qu'il associe à l'exception ``ValueError`` qui précise l'erreur
et mentionne la fonction où elle s'est produite. Le message est ensuite
intercepté plus bas.

.. runpython::
    :showcode:

    def inverse (x):
        if x == 0 :
            raise ValueError("valeur nulle interdite, fonction inverse")
        y = 1.0 / x
        return y

    try:
        print(inverse(0))  # erreur
    except ValueError as exc:
        print("erreur, message :", exc)

Le déclenchement d'une exception suit la syntaxe suivante.

.. mathdef::
    :title: Lever une exception
    :tag: Syntaxe

    ::

        raise exception_type(message)

    Cette instruction lance l'exception ``exception_type`` associée au message
    ``message``. Le message est facultatif, lorsqu'il n'y en a pas, la syntaxe
    se résume à ``raise exception_type``.

Et pour attraper cette exception et le message qui lui est associé, il
faut utiliser la syntaxe décrite au paragraphe précédent.

Héritage et exception
+++++++++++++++++++++

.. index:: héritage

L'instruction ``help(ZeroDivisionError)`` retourne l'aide associée à l'exception ``ZeroDivisionError``.
Celle-ci indique que l'exception ``ZeroDivisionError`` est en fait un cas particulier de
l'exception ``ArithmeticError``,
elle-même un cas particulier de ``StandardError``.

::

    class ZeroDivisionError(ArithmeticError)
        |  Second argument to a division or modulo operation was zero.
        |
        |  Method resolution order:
        |      ZeroDivisionError
        |      ArithmeticError
        |      StandardError
        |      Exception

Toutes les exceptions sont des cas particuliers de l'exception de type ``Exception``.
C'est pourquoi l'instruction ``except Exception:`` attrape toutes les exceptions.
L'instruction ``except ArithmeticError:`` attrape toutes les erreurs de
type ``ArithmeticError``, ce qui inclut les erreurs de type ``ZeroDivisionError``.
Autrement dit, toute exception de type ``ZeroDivisionError``
est attrapée par les instructions suivantes :

::

    except ZeroDivisionError:
    except ArithmeticError:
    except StandardError:
    except Exception:

Plus précisément, chaque exception est une classe qui dérive directement ou indirectement de la
classe ``Exception``. L'instruction ``except ArithmeticError :`` par exemple attrape
toutes les exceptions de type ``ArithmeticError`` et toutes celles
qui en dérivent comme la classe ``ZeroDivisionError``.

Instructions ``try``, ``except`` imbriquées
+++++++++++++++++++++++++++++++++++++++++++

Comme pour les boucles, il est possible d'imbriquer les portions
protégées de code les unes dans les autres. Dans l'exemple qui suit, la
première erreur est l'appel à une fonction non définie, ce qui déclenche
l'exception ``NameError``.

.. runpython::
    :showcode:

    def inverse (x):
        y = 1.0 / x
        return y

    try:
        try:
            print(inverses(0))  # fonction inexistante --> exception NameError
            print(inverse(0))   # division par zéro --> ZeroDivisionError
        except NameError:
            print("appel à une fonction non définie")
    except ZeroDivisionError as exc:
        print("erreur", exc)

En revanche, dans le second exemple, les deux lignes
``print(inverse(0))`` et ``print(inverses(0))`` ont été permutées. La première
exception déclenchée est la division par zéro. La première clause
``except`` n'interceptera pas cette erreur puisqu'elle n'est pas du type recherché.

.. runpython::
    :showcode:

    def inverse (x):
        y = 1.0 / x
        return y

    try:
        try:
            print(inverse(0))   # division par zéro --> ZeroDivisionError
            print(inverses(0))  # fonction inexistante --> exception NameError
        except NameError:
            print("appel à une fonction non définie")
    except ZeroDivisionError as exc:
        print("erreur", exc)

Une autre imbrication possible est l'appel à une fonction qui inclut déjà
une partie de code protégée. L'exemple suivant appelle la fonction
``inverse`` qui intercepte les exceptions de type ``ZeroDivisionError`` pour retourner
une grande valeur lorsque ``x=0``. La seconde exception générée survient
lors de l'appel à la fonction ``inverses`` qui déclenche l'exception ``NameError``,
elle aussi interceptée.

.. runpython::
    :showcode:

    def inverse (x):
        try:
            y = 1.0 / x
        except ZeroDivisionError as exc:
            print("erreur ", exc)
            if x > 0: return 1000000000
            else: return -1000000000
        return y

    try:
        print(inverse(0))   # division par zéro    --> la fonction inverse sait gérer
        print(inverses(0))  # fonction inexistante --> exception NameError
    except NameError:
        print("appel à une fonction non définie")

Définir ses propres exceptions
==============================

Dériver une classe d'exception
++++++++++++++++++++++++++++++

Pour définir sa propre exception, il faut créer une classe qui dérive d'une
classe d'exception existante par exemple, la classe ``Exception``.
L'exemple suivant crée une exception ``AucunChiffre`` qui est lancée par la fonction
``conversion`` lorsque la chaîne de caractères qu'elle doit
convertir ne contient pas que des chiffres.

.. runpython::
    :showcode:
    :process:

    class AucunChiffre(Exception):
        """
        chaîne de caractères contenant aussi autre chose que des chiffres
        """
        pass

    def conversion(s):
        """
        conversion d'une chaîne de caractères en entier
        """
        if not s.isdigit():
            raise AucunChiffre(s)
        return int(s)

    try:
        s = "123a"
        print(s, " = ", conversion (s))
    except AucunChiffre as exc:
        # on affiche ici le commentaire associé à la classe d'exception
        # et le message associé
        print(AucunChiffre.__doc__, " : ", exc)

.. index:: __str__

En redéfinissant l'opérateur ``__str__`` d'une exception,
il est possible d'afficher des messages plus explicites avec
la seule instruction ``print``.

::

    class AucunChiffre(Exception):
        """
        chaîne de caractères contenant aussi autre chose que des chiffres
        """
        def __str__ (self):
            return "{0} {1}".format(self.__doc__, Exception.__str__(self))

Personnalisation d'une classe d'exception
+++++++++++++++++++++++++++++++++++++++++

Il est parfois utile qu'une exception contienne davantage d'informations
qu'un simple message. L'exemple suivant reprend l'exemple du paragraphe précédent.
L'exception ``AucunChiffre`` inclut cette fois-ci un paramètre supplémentaire
contenant le nom de la fonction où l'erreur a été déclenchée.

La classe ``AucunChiffre`` possède dorénavant un constructeur qui doit
recevoir deux paramètres : une valeur et un nom de fonction. L'exception est levée à
l'aide de l'instruction ``raise AucunChiffre(s, "conversion")`` qui regroupe
dans un T-uple les paramètres à envoyer à l'exception.

L'opérateur ``__str__`` a été modifié de façon à ajouter ces deux
informations dans le message associé à l'exception. Ainsi, l'instruction
``print(exc)`` présente à l'avant dernière ligne de cet
exemple affiche un message plus complet.

.. runpython::
    :showcode:
    :process:

    class AucunChiffre(Exception):
        """
        chaîne de caractères contenant aussi autre chose que des chiffres
        """
        def __init__(self, s, f=""):
            Exception.__init__(self, s)
            self.s = s
            self.f = f
        def __str__(self) :
            return "exception AucunChiffre, depuis la fonction {0} avec le paramètre {1}".format(self.f, self.s)

    def conversion (s) :
        """
        conversion d'une chaîne de caractères en entier
        """
        if not s.isdigit():
            raise AucunChiffre(s, "conversion")
        return int(s)

    try:
        s = "123a"
        i = conversion (s)
        print(s, " = ", i)
    except AucunChiffre as exc:
        print(exc)
        print("fonction : ", exc.f)

Etant donné que le programme déclenche une exception dans la section de
code protégée, les deux derniers affichages sont les seuls exécutés
correctement. Ils produisent les deux lignes qui suivent. %

Exemples d'utilisation des exceptions
=====================================

.. index:: itérateur

Les itérateurs
++++++++++++++

Les itérateurs sont des outils qui permettent de parcourir des objets qui
sont des ensembles, comme une liste, un dictionnaire. Ils fonctionnent toujours
de la même manière. L'exemple déjà présenté au chapitre :ref:`chap_iterateur`
et repris en partie ici définit une classe contenant trois coordonnées,
ainsi qu'un itérateur permettant de parcourir ces trois coordonnées.
Arrivée à la troisième itération, l'exception
`StopIteration <https://docs.python.org/3/library/exceptions.html#StopIteration>`_
est déclenchée. Cette exception indique à une boucle ``for`` de s'arrêter.

::

    class point_espace:

        # ...

        class class_iter:
            def __init__(self, ins):
                self._n   = 0
                self._ins = ins
            def __iter__(self) :
                return self
            def next(self):
                if self._n <= 2:
                    v = self._ins[self._n]
                    self._n += 1
                    return v
                else:
                    raise StopIteration

        def __iter__(self):
            return point_espace.class_iter(self)

Cet exemple montre seulement que les exceptions
n'interviennent pas seulement lors d'erreurs mais font parfois partie
intégrante d'un algorithme.

Exception ou valeur aberrante
+++++++++++++++++++++++++++++

.. index:: valeur aberrante

Sans exception, une solution pour indiquer un cas de mauvaise utilisation
d'une fonction est de retourner une valeur aberrante.
Retourner ``-1`` pour une fonction dont le résultat est nécessairement
positif est une valeur aberrante. Cette convention permet de signifier à
celui qui appelle la fonction que son appel n'a pu être traité correctement.
Dans l'exemple qui suit, la fonction ``racine_carree`` retourne un couple de
résultats, ``True`` ou ``False`` pour savoir si le calcul est possible,
suivi du résultat qui n'a un sens que si ``True`` est retournée en première valeur.

.. runpython::
    :showcode:

    def racine_carree(x) :
       if x < 0: return False, 0
       else: return True, x ** 0.5

    print(racine_carree(-1))  # (False, 0)
    print(racine_carree(1))   # (True, 1.0)

Plutôt que de compliquer le programme avec deux résultats ou une valeur aberrante,
on préfère souvent déclencher une exception, ici, ``ValueError``.
La plupart du temps, cette exception n'est pas déclenchée.
Il est donc superflu de retourner un couple plutôt qu'une seule valeur.

::

    def racine_carree(x) :
        if x < 0:
            raise ValueError("valeur négative")
        return x ** 0.5

    print(racine_carree(-1))  # déclenche une exception
    print(racine_carree(1))

Le piège des exceptions
+++++++++++++++++++++++

.. index:: garbage collector

Ce paragraphe évoque certains problèmes lorsqu'une exception est levée.
L'exemple utilise les fichiers décrits au chapitre :ref:`chap_fichier`.
Lorsqu'une exception est levée à l'intérieur d'une fonction,
l'exécution de celle-ci s'interrompt. Si l'exception est attrapée,
le programme continue sans problème ; les objets momentanément créés seront
détruits par le `garbage collector <https://docs.python.org/3/library/gc.html>`_.
Il faut pourtant faire attention dans le cas par exemple où l'exception
est levée alors qu'un fichier est ouvert : il ne sera pas fermé.

::

    for i in range(0, 5):
        try :
            x, y = i-1, i-2
            print("{}/{}".format(x, y))
            f = open("essai.txt", "a")
            f.write("{}/{}=".format(x, y))
            f.write(str((float (x)/y)) + "\n" )     # exception si y == 0
            f.close()
        except Exception as e:
            print("erreur avec i = ", i, ",", e, f.closed)

Les écritures dans le fichier se font en mode ajout ``"a"``,
le fichier ``"essai.txt"`` contiendra tout ce qui aura été écrit.

.. list-table::
    :widths: 8 8
    :header-rows: 1

    * - affichage
      - fichier
    * - ::

            -1/-2
            0/-1
            1/0
            erreur avec i =  2 , float division by zero False
            2/1
            3/2

      - ::

            -1/-2=0.5
            0/-1=-0.0
            1/0=2/1=2.0
            3/2=1.5

.. index:: context manager

La troisième ligne du fichier est tronquée puisque l'erreur est
intervenue juste avant l'affichage. On voit aussi
que ``f.closed`` est faux. Cela signifie que le fichier n'est pas fermé.
Pour se prémunir contre les exceptions lorsqu'on écrit un fichier,
il faut utiliser le mot clé
`with <https://www.python.org/dev/peps/pep-0343/>`_ :

::

    for i in range(0, 5):
        try :
            x, y = i-1, i-2
            print("{}/{}".format(x, y))
            with open("essai.txt", "a") as f:
                f.write("{}/{}=".format(x, y))
                f.write(str((float (x)/y)) + "\n" )     # exception si y == 0
        except Exception as e:
            print("erreur avec i = ", i, ",", e, f.closed)

Pour en savoir un peu plus :
`Les context managers et le mot clé with en Python <http://sametmax.com/les-context-managers-et-le-mot-cle-with-en-python/>`_.
