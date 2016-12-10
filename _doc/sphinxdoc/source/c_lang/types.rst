

====================================
Types et variables du langage python
====================================

Variables
=========

Il est impossible d'�crire un programme sans utiliser de variable. 
Ce terme d�signe le fait d'attribuer un nom ou identificateur � des informations : 
en les nommant, on peut manipuler ces informations beaucoup plus facilement. 
L'autre avantage est de pouvoir �crire des programmes valables pour des valeurs 
qui varient : on peut changer la valeur des variables, le programme s'ex�cutera 
toujours de la m�me mani�re et fera les m�mes types de calculs quelles que soient 
les valeurs manipul�es. Les variables jouent un r�le semblable aux inconnues 
dans une �quation math�matique. 

L'ordinateur ne sait pas faire l'addition de plus de deux nombres mais cela 
suffit � calculer la somme de :math:`n` premiers nombres entiers. 
Pour cela, il est n�cessaire de cr�er une variable interm�diaire qu'on appellera 
par exemple ``somme`` de mani�re � conserver le r�sultat des sommes interm�diaires.

.. runpython::
    :showcode:

    n = 11
    somme = 0                   # initialisation : la somme est nulle 
    for i in range(1, n):       # pour tous les indices de 1 � n exclu
        somme = somme + i       # on ajoute le i �me �l�ment � somme
    print(somme)


.. mathdef::
    :title: variable
    :tag: D�finition

    Une variable est caract�ris�e par :
    
    * **un identificateur :** il peut contenir des lettres, des chiffres, des blancs soulign�s 
      mais il ne peut commencer par un chiffre. Minuscules et majuscules
      sont diff�renci�es. Il est aussi unique.
    * **un type :** c'est une information sur le contenu de la variable
      qui indique � l'interpr�teur *python*, la mani�re de manipuler cette information.

Comme le typage est dynamique en *python*, le type n'est pas pr�cis� explicitement, 
il est implicitement li�e � l'information manipul�e. Par exemple, en �crivant, 
``x = 3.4``, on ne pr�cise pas le type de la variable ``x`` 
mais il est implicite car :math:`x` re�oit une valeur r�elle : 
``x`` est de type r�el ou `float` en *python*. Pour leur premi�re initialisation, 
une variable re�oit dans la plupart des cas une constante :

.. mathdef::
    :title: constante
    :tag: D�finition

    Les constantes sont le contraire des variables, ce sont toutes les valeurs num�riques, 
    cha�nes de caract�res, ..., tout ce qui n'est pas d�sign� par un nom. Les constantes poss�dent un type
    mais pas d'identificateur.
		

Le langage *python* poss�de un certain nombre de types de variables d�j� 
d�finis ou types fondamentaux � partir desquels il sera possible de 
d�finir ses propres types (voir chapitre :ref:`chap_classe`). 
Au contraire de langages tels que le *C*, il n'est pas besoin de d�clarer une 
variable pour signifier qu'elle existe, il suffit de lui affecter une valeur. 
Le type de la variable sera d�fini par le type de la constante qui lui est affect�e. 
Le type d'une variable peut changer, il correspond toujours au type de la derni�re affectation.

::

    x   = 3.5      # cr�ation d'une variable nombre r�el appel�e x initialis�e � 3.5
                   # 3.5 est un r�el, la variable est de type "float"
    sc = "cha�ne"  # cr�ation d'une variable cha�ne de caract�res appel�e str 
                   # initialis�e � "cha�ne", sc est de type "str"

.. index:: commentaire

Pour tous les exemples qui suivront, le symbole ``#`` appara�tra � maintes reprises. 
Il marque le d�but d'un commentaire que la fin de la ligne termine. 
Autrement dit, un commentaire est une information aidant � la compr�hension 
du programme mais n'en faisant pas partie comme dans l'exemple qui suit.

::

    x = 3          # affectation de la valeur enti�re 3 � la variable x
    y = 3.0        # affectation de la valeur r�elle 3.0 � la variable y

.. index:: backslash

Le *python* impose une instruction par ligne. Il n'est pas possible d'utiliser 
deux lignes pour �crire une affectation � moins de conclure chaque ligne qui 
n'est pas la derni�re par le symbole ``\``
L'exemple suivant est impossible.

::

    x = 
        5.5

Il devrait �tre r�dig� comme suit :

::

    x =  \
        5.5

Avec ce symbole, les longues instructions peuvent �tre �crites sur plusieurs 
lignes de mani�re plus lisibles, de sorte qu'elles apparaissent en entier � l'�cran. 
Si le dernier caract�re est une virgule, il est implicite.

Les paragraphes suivant �num�rent les types incontournables en *python*. 
Ils sont class�s le plus souvent en deux cat�gories : types 
*immuables* ou *modifiables*. Tous les types du langage *python* sont �galement 
des objets, c'est pourquoi on retrouve dans ce chapitre certaines 
formes d'�criture similaires � celles pr�sent�es plus tard dans 
le chapitre concernant les classes (:ref:`chap_classe`).


.. index:: immuable, immutable

Types immuables (ou immutable)
==============================

.. mathdef::
    :tag: D�finition
    :title: type immuable (ou immutable)

    Une variable de type immuable ne peut �tre modifi�e. Une op�ration
    sur une variable de ce type entra�ne n�cessairement la cr�ation d'une autre 
    variable du m�me type, m�me si cette derni�re est temporaire.
			
Autrement dit, la simple instruction ``x+=3`` qui consiste � ajouter � la 
variable ``x`` la valeur ``3`` cr�e une seconde variable dont la valeur 
est celle de ``x`` augment�e de ``3`` puis � en recopier le contenu dans celui 
de la variable ``x``. Les nombres sont des types immuables tout comme les 
cha�nes de caract�res et les ``tuple`` qui sont des tableaux d'objets. 
Il n'est pas possible de modifier une variable de ce type, il faut en 
recr�er une autre du m�me type qui int�grera la modification.
			

Type "rien" ou None
+++++++++++++++++++

.. index:: None

*python* propose un type ``None`` pour signifier qu'une variable ne contient rien. 
La variable est de type ``None`` et est �gale � ``None``.

::

    s = None
    print(s)    # affiche None

Certaines fonctions utilisent cette convention lorsqu'il leur est impossible 
de retourner un r�sultat. Ce n'est pas la seule option pour g�rer cette 
impossibilit� : il est possible de g�n�rer une :ref:`exception <chap_exception>`, 
de retourner une valeur par d�faut ou encore de retourner ``None``. 
Il n'y a pas de choix meilleur, il suffit juste de pr�ciser la convention choisie.

Les fonctions sont d�finies au paragraphe :ref:`par_fonction`, 
plus simplement, ce sont des mini-programmes : elles permettent de d�couper 
un programme long en t�ches plus petites. On les distingue des variables 
car leur nom est suivi d'une liste de constantes ou variables comprises 
entre parenth�ses et s�par�es par une virgule.






Nombres r�els et entiers
========================

.. index:: float, int, r�el, entier

Il existe deux types de nombres en *python*, les nombres r�els 
``float`` et les nombres entiers ``int``. L'instruction ``x=3`` cr�e une variable 
de type ``int`` initialis�e � ``3`` tandis que ``y=3.0`` cr�e une variable de type 
``float`` initialis�e � ``3.0``. Le programme suivant permet de v�rifier cela en 
affichant pour les variables ``x`` et ``y``, leurs valeurs et leurs 
types respectifs gr�ce � la fonction ``type``.


.. runpython::
    :showcode:

    x = 3
    y = 3.0
    print("x =", x, type(x))
    print("y =", y, type(y))

La liste des op�rateurs qui s'appliquent aux nombres r�els et 
entiers suit. Les trois premiers r�sultats s'expliquent 
en utilisant la repr�sentation en base deux. ``8 << 1`` s'�crit en base deux 
``100 << 1 = 1000``, ce qui vaut 16 en base d�cimale : 
les bits sont d�cal�s vers la droite ce qui �quivaut � multiplier 
par deux. De m�me, ``7 & 2`` s'�crit ``1011 & 10 = 10``, qui vaut 2 en base d�cimale. 
Les op�rateurs ``<<``, ``>>``, ``|``, ``&`` sont des op�rateurs bit � bit, 
ils se comprennent � partir de la repr�sentation binaire des nombres entiers.

.. index:: <<, >>, |, &, +, -, +=, -=, *, /, *=, /=, **, %

.. list-table::
    :widths: 3 10 5
    :header-rows: 1

    * - op�rateur
      - signification
      - exemple
    * - ``<<`` ``>>``
      - d�calage � gauche, � droite
      - ``x = 8 << 1`` 
    * - ``|``
      - op�rateur logique ``ou`` bit � bit
      - ``x = 8 | 1`` 
    * - ``&``
      - op�rateur logique ``et`` bit � bit
      - ``x = 11 & 2`` 
    * - ``+ -``
      - addition, soustraction 											
      - ``x = y + z``
    * - ``+= -=``
      - addition ou soustraction puis affectation
      - ``x += 3``
    * - ``*	/``
      - multiplication, division
      - ``x = y * z``
    * - ``//``
      - division enti�re, le r�sultat est de type r�el si l'un des nombres est r�el
      - ``x = y // 3``
    * - ``%``
      - reste d'une division enti�re (modulo)
      - ``x = y % 3``
    * - ``*= /=``
      - multiplication ou division puis affectation
      - ``x *= 3``
    * - ``**``
      - puissance (enti�re ou non, racine carr�e = ** 0.5)
      - ``x = y ** 3``

.. index:: arrondi, conversion

Les fonctions ``int`` et ``float`` permettent de convertir un nombre quelconque 
ou une cha�ne de caract�res respectivement en un entier (arrondi) et en un nombre r�el.

.. runpython::
    :showcode:
    
    x = int (3.5)
    y = float (3)
    z = int ("3")
    print("x:", type(x), "   y:", type(y), "   z:", type(z))

Il peut arriver que la conversion en un nombre entier ne soit pas directe. 
Dans l'exemple qui suit, on cherche � convertir une cha�ne de caract�res 
(voir :ref:`string_paragraphe_chaine`) en entier mais cette cha�ne 
repr�sente un r�el. Il faut d'abord la convertir en r�el puis en entier, 
c'est � ce moment que l'arrondi sera effectu�.

::

    i = int ("3.5")          # provoque une erreur
    i = int (float ("3.5"))  # fonctionne


.. index:: priorit� des op�rateurs

Les op�rateurs list�s par le tableau ci-dessus ont des priorit�s 
diff�rentes, tri�s par ordre croissant.
Toutefois, il est conseill� d'avoir recours aux parenth�ses pour 
enlever les doutes : ``3 * 2 ** 4 = 3 * (2 ** 4)``.
La page `Opertor Precedence <https://docs.python.org/3/reference/expressions.html#operator-precedence>`_
est plus compl�te � ce sujet.

.. index:: division enti�re

*python* propose l'op�rateur ``//`` pour les divisions enti�res
et c'est une rare exception parmi les languages
qui ne poss�dent qu'un seul op�rateur ``/`` qui retourne 
un entier pour une division enti�re except� en *python* :

.. runpython::
    :showcode:

    x = 11
    y = 2
    z = x // y      # le r�sultat est 5 et non 5.5 car la division est enti�re
    zz = x / y      # le r�sultat est 5.5 
    
    print(z, zz)
    

Pour �viter d'�crire le type ``float``, on peut �galement �crire ``11.0`` 
de fa�on � sp�cifier explicitement que la valeur ``11.0`` est r�elle et non enti�re. 
L'op�rateur ``//`` permet d'effectuer une division enti�re lorsque 
les deux nombres � diviser sont r�els, le r�sultat est un entier mais la 
variable est de type r�el si l'un des nombres est de type r�el. 


Bool�en
+++++++

.. index:: bool, True, False

Les bool�ens sont le r�sultat d'op�rations logiques et ont deux 
valeurs possibles : ``True`` ou ``False``. 
Voici la liste des op�rateurs qui s'appliquent aux bool�ens.

.. list-table::
    :widths: 3 10 5
    :header-rows: 1

    * - op�rateur
      - signification
      - exemple
    * - ``and or
      - et, ou logique
      - ``x = True or False`` (r�sultat = True)
    * - ``not``
      - n�gation logique
      - ``x = not x``

.. runpython::
    :showcode:

    x = 4 < 5
    print(x)         # affiche True
    print(not x)     # affiche False

Voici la liste des op�rateurs de comparaisons qui retournent 
des bool�ens. Ceux-ci s'applique � tout type, aux entiers, 
r�els, cha�nes de caract�res, t-uples... Une comparaison entre un entier 
et une cha�ne de caract�res est syntaxiquement correcte m�me si le r�sultat a peu d'int�r�t.


.. index:: <, >, <=, >=, !=, ==, comparaison


.. list-table::
    :widths: 3 10 5
    :header-rows: 1

    * - op�rateur
      - signification
      - exemple
    * - ``< >
      - inf�rieur, sup�rieur
      - ``x = 5  < 5``
    * - ``<= >=``
      - inf�rieur ou �gal, sup�rieur ou �gal
      - ``x = 5 <= 5``
    * - ``== !=``
      - �gal, diff�rent
      - ``x = 5 == 5``

A l'instar des nombres r�els, il est pr�f�rable d'utiliser les 
parenth�ses pour �viter les probl�mes de priorit�s d'op�rateurs 
dans des expressions comme : ``3 < x and x < 7``. 
Toutefois, pour cet exemple, *python* accepte l'�criture r�sum�e 
qui encha�ne des comparaisons : ``3 < x and x < 7`` est 
�quivalent � ``3 < x < 7``. Il existe deux autres mots-cl�s 
qui retournent un r�sultat de type bool�en :

.. list-table::
    :widths: 3 10 5
    :header-rows: 1

    * - op�rateur
      - signification
      - exemple
    * - ``is``
      - test d'identification
      - ``"3" is str``
    * - ``in``
      - test d'appartenance
      - ``3 in [3, 4, 5]``
      
Ces deux op�rateurs seront utilis�s ult�rieurement, 
``in`` avec les listes, les dictionnaires, les boucles 
(paragraphe :ref:`boucle_for`), ``is`` lors de l'�tude des listes 
(paragraphe :ref:`par_liste_copie` et des :ref:`classes <chap_classe>`). 
Bien souvent, les bool�ens sont utilis�s de mani�re implicite lors 
de tests (paragraphe :ref:`test_test`) ce qui n'emp�che pas de les 
d�clarer explicitement.

::

    x = True
    y = False


.. _string_paragraphe_chaine:

Cha�ne de caract�res
====================

.. index:: cha�ne de caract�res, str, string

Cr�ation d'une cha�ne de caract�res
+++++++++++++++++++++++++++++++++++

.. mathdef::
    :title: cha�ne de caract�res
    :tag: D�finition
    
    Le terme "cha�ne de caract�res" ou *string* en anglais signifie 
    une suite finie de caract�res, autrement dit, du texte.

Ce texte est compris entre deux guillemets ou deux apostrophes, 
ces deux symboles sont interchangeables. L'exemple suivant montre comment 
cr�er une cha�ne de caract�res. Il ne faut pas confondre la partie entre 
guillemets ou apostrophes, qui est une constante, de la variable qui la contient.

.. runpython::
    :showcode:

    t = "string = texte"
    print(type (t), t)
    t = 'string = texte, initialisation avec apostrophes'
    print(type (t), t)

    t = "morceau 1" \
        "morceau 2"    # second morceau ajout� au premier par l'ajout du symbole \, 
                       # il ne doit rien y avoir apr�s le symbole \, 
                       # pas d'espace ni de commentaire
    print(t)

    t = """premi�re ligne		
    seconde ligne"""   # cha�ne de caract�res qui s'�tend sur deux lignes
    print(t)


La troisi�me cha�ne de caract�res cr��e lors de ce programme s'�tend sur deux lignes. 
Il est parfois plus commode d'�crire du texte sur deux lignes plut�t 
que de le laisser cach� par les limites de fen�tres d'affichage. 
*python* offre la possibilit� de couper le texte en deux cha�nes de 
caract�res recoll�es � l'aide du symbole ``\`` � condition que 
ce symbole soit le dernier de la ligne sur laquelle il appara�t. De m�me, 
lorsque le texte contient plusieurs lignes, il suffit de les encadrer entre deux 
symboles ``"""`` ou ``'''`` pour que l'interpr�teur *python* consid�re l'ensemble 
comme une cha�ne de caract�res et non comme une s�rie d'instructions. 

Par d�faut, le *python* ne permet pas l'insertion de caract�res tels que 
les accents dans les cha�nes de caract�res, le paragraphe 
:ref:`par_intro_accent_code` explique comment r�soudre ce probl�me. 
De m�me, pour ins�rer un guillemet dans une cha�ne de caract�res 
encadr�e elle-m�me par des guillemets, il faut le faire pr�c�der 
du symbole ``\``. La s�quence ``\`` est appel�e un extra-caract�re
(voir table :ref:`extra_caractere`).

.. list-table::
    :widths: 3 10
    :header-rows: 1

    * - ``"``
      - guillemet
    * - ``'``
      - apostrophe
    * - ``\n``
      - passage � la ligne
    * - ``\\``
      - insertion du symbole ``\``
    * - ``\%``
      - pourcentage, ce symbole est aussi un caract�re sp�cial
    * - ``\t``
      - tabulation
    * - ``\r``
      - retour � la ligne, peu usit�, il a surtout son importance lorsqu'on passe
        d'un syst�me *Windows* � *Linux* car *Windows* l'ajoute
        automatiquement � tous ses fichiers textes

Liste des extra-caract�res les plus couramment utilis�s � 
l'int�rieur d'une cha�ne de caract�res 
(voir  page `Lexical analysis <https://docs.python.org/3/reference/lexical_analysis.html>`_).
		
Il peut �tre fastidieux d'avoir � doubler tous les symboles ``\`` d'un nom de fichier. 
Il est plus simple dans ce cas de pr�fixer la cha�ne de caract�res par ``r`` 
de fa�on � �viter que l'utilisation du symbole ``\`` ne d�signe un caract�re 
sp�cial. Les deux lignes suivantes sont �quivalentes : 

::

    s = "C:\\Users\\Dupre\\exemple.txt"
    s = r"C:\Users\Dupre\exemple.txt"

Sans la lettre ``"r"``, tous les ``\`` doivent �tre doubl�s, dans le cas 
contraire, *python* peut avoir des effets ind�sirables selon le 
caract�re qui suit ce symbole.


.. _fonction_str:

Manipulation d'une cha�ne de caract�res
+++++++++++++++++++++++++++++++++++++++


Une cha�ne de caract�res est semblable � un tableau et certains 
op�rateurs qui s'appliquent aux tableaux s'appliquent �galement aux 
cha�nes de caract�res. Ceux-ci sont regroup�s dans la table 
:ref:`operation_string`. La fonction ``str`` permet de convertir un nombre, 
un tableau, un objet (voir chapitre :ref:`chap_classe`) en cha�ne de caract�res 
afin de pouvoir l'afficher. La fonction ``len`` retourne la longueur 
de la cha�ne de caract�res.

.. runpython::
    :showcode:

    x = 5.567
    s = str (x)
    print(type(s), s)   # <type 'str'> 5.567
    print(len(s))       # affiche 5

.. list-table::
    :widths: 3 10 5
    :header-rows: 1

    * - op�rateur
      - signification
      - exemple
    * - ``+``
      - concat�nation de cha�nes de caract�res
      - ``t = "abc" + "def"``
    * - ``+=``
      - concat�nation puis affectation
      - ``t += "abc"
    * - ``in``, ``not in``
      - une cha�ne en contient-elle une autre ?
      - ``"ed" in "med"
    * - ``*``
      - r�p�tition d'une cha�ne de caract�res
      - ``t = "abc" * 4
    * - ``[n]``
      - obtention du eni�me caract�re, le premier
        caract�re a pour indice 0
      - ``t = "abc"; print(t[0])  # donne a``
    * - ``[i:j]``
      - obtention des caract�res compris entre les indices ``i`` et 
        ``j-1`` inclus, le premier caract�re a pour indice 0
      - ``t = "abc"; print(t [0:2]) # donne ab``
    
Il existe d'autres fonctions qui permettent de manipuler les cha�nes de caract�res.

::

    res = s.fonction (...)

O� ``s`` est une cha�ne de caract�res, ``fonction`` 
est le nom de l'op�ration que l'on veut appliquer � ``s``, ``res`` 
est le r�sultat de cette manipulation. 

La table :ref:`string_method` pr�sente une liste non exhaustive 
des fonctions disponibles dont un exemple d'utilisation suit. 
Cette syntaxe ``variable.fonction(arguments)`` est celle des classes.

.. list-table::
    :widths: 10 20
    :header-rows: 0
   
    * - ``count( sub[, start[, end]])``
      - Retourne le nombre d'occurences de la cha�ne de caract�res ``sub``,
        les param�tres par d�faut ``start`` et ``end`` permettent de r�duire la
        recherche entre les caract�res d'indice ``start`` et ``end`` exclu. Par d�faut,
        ``start`` est nul tandis que ``end`` correspond � la fin de la cha�ne de caract�res.
    * - ``find( sub[, start[, end]])``
      - Recherche une cha�ne de caract�res ``sub``,
        les param�tres par d�faut ``start`` et ``end`` ont la m�me signification
        que ceux de la fonction ``count``. Cette fonction retourne -1 si 
        la recherche n'a pas abouti.
    * - ``isalpha()``
      - Retourne ``True`` si tous les caract�res sont des lettres, ``False`` sinon.
    * - ``isdigit()
      -  Retourne ``True`` si tous les caract�res sont des chiffres, ``False`` sinon.
    * - ``replace( old, new[, count])``
      - Retourne une copie de la cha�ne de caract�res en rempla�ant toutes les
        occurrences de la cha�ne ``old`` par ``new``. Si le param�tre optionnel 
        ``count`` est renseign�, alors seules les ``count`` premi�res occurrences
        seront remplac�es.
    * - ``split( [sep [,maxsplit]])``
      - D�coupe la cha�ne de caract�res en se servant de la cha�ne ``sep`` comme
        d�limiteur. Si le param�tre ``maxsplit`` est renseign�, au plus ``maxsplit}
        coupures seront effectu�es.
    * - ``upper()``
      - Remplace les minuscules par des majuscules.
    * - ``lower()``
      - Remplace les majuscules par des minuscules.
    * - ``join ( li )``
      - ``li`` est une liste,
        cette fonction agglutine tous les �l�ments d'une liste s�par�s par ``sep``
        dans l'expression ``sep.join ( ["un", "deux"])``. 

.. runpython::
    :showcode:
    
    st = "langage python"
    st = st.upper()               # mise en lettres majuscules
    i  = st.find("PYTHON")        # on cherche "PYTHON" dans st
    print(i)                      # affiche 8
    print(st.count("PYTHON"))     # affiche 1
    print(st.count("PYTHON", 9))  # affiche 0

.. _exemple_string_join:

L'exemple suivant permet de retourner une cha�ne de caract�res contenant 
plusieurs �l�ments s�par�s par ``";"``. La cha�ne ``"un;deux;trois"`` 
doit devenir ``"trois;deux;un"``. On utilise pour cela les fonctionnalit�s 
``split`` et ``join``.
L'exemple utilise �galement la fonctionnalit� ``reverse`` des listes qui 
seront d�crites plus loin dans ce chapitre. Il faut simplement retenir 
qu'une liste est un tableau. ``reverse`` retourne le tableau.

.. runpython::
    :showcode:

    s    = "un;deux;trois"
    mots = s.split (";")        # mots est �gal � ['un', 'deux', 'trois']
    mots.reverse ()             # retourne la liste, mots devient �gal � 
                                #                 ['trois', 'deux', 'un']
    s2 = ";".join (mots)        # concat�nation des �l�ments de mots s�par�s par ";"
    print(s2)                   # affiche trois;deux;un

.. _label_formattage_string:

Formatage d'une cha�ne de caract�res
++++++++++++++++++++++++++++++++++++

*python* offre une mani�re plus concise de former une cha�ne 
de caract�res � l'aide de plusieurs types d'informations en 
�vitant la conversion explicite de ces informations (fonction ``str``) 
et leur concat�nation. Il est particuli�rement int�ressant pour les 
nombres r�els qu'il est possible d'�crire en imposant un nombre 
de d�cimales fixe. Le format est le suivant :

::

    ".... %c1  ....  %c2 " % (v1,v2)

``c1`` est un code choisi parmi ceux de la table 
::ref`format_print`. Il indique le format dans lequel la variable 
``v1`` devra �tre transcrite. Il en est de m�me pour le code 
``c2`` associ� � la variable ``v2``. Les codes ins�r�s dans la cha�ne 
de caract�res seront remplac�s par les variables cit�es entre 
parenth�ses apr�s le symbole ``%`` suivant la fin de la cha�ne de 
caract�res. Il doit y avoir autant de codes que de variables, 
qui peuvent aussi �tre des constantes. 

Voici concr�tement l'utilisation de cette syntaxe :

.. runpython::
    :showcode:
    
    x = 5.5
    d = 7
    s = "caract�res"
    res = "un nombre r�el %f et un entier %d, une cha�ne de %s, \n" \
          "un r�el d'abord converti en cha�ne de caract�res %s" % (x,d,s, str(x+4))
    print(res)
    res = "un nombre r�el " + str (x) + " et un entier " + str (d) + \
          ", une cha�ne de " + s + \
          ",\n un r�el d'abord converti en cha�ne de caract�res " + str(x+4)
    print(res)

La seconde affectation de la variable ``res`` propose une solution �quivalente 
� la premi�re en utilisant l'op�rateur de concat�nation ``+``. 
Les deux solutions sont �quivalentes, tout d�pend des pr�f�rences de celui qui �crit le programme.

    un nombre r�el 5.500000 et un entier 7, une cha�ne de caract�res, 
    un r�el d'abord converti en cha�ne de caract�res 9.5
    un nombre r�el 5.5 et un entier 7, une cha�ne de caract�res,
    un r�el d'abord converti en cha�ne de caract�res 9.5

La premi�re option permet n�anmoins un formatage plus pr�cis des nombres r�els 
en imposant par exemple un nombre d�fini de d�cimal. Le format est le suivant :

\begin{xsyntax}{cha�ne de caract�res, formatage des nombres}
\begin{verbatimno}

"%n.df" % x
\end{verbatimno}
\negvspace
o� ``n`` est le nombre de chiffres total et ``d`` est le nombre de d�cimales, ``f`` d�signe un format r�el indiqu� par la pr�sence du symbole ``\%}
\indexsyntaxenoc{formatage des nombres}
\end{xsyntax}
            
%\vspaceneg           
%Exemple :       
\vspace{-0.4cm``     
\begin{verbatimx}
x = 0.123456789
print(x)             # affiche 0.123456789
print("%1.2f" % x)   # affiche 0.12
print("%06.2f" % x)  # affiche 000.12
\end{verbatimx}
\vspaceneg 
%
Il existe d'autres formats regroup�s dans la table \ref{format_print``. L'aide reste encore le meilleur r�flexe car le langage *python* est susceptible d'�voluer et d'ajouter de nouveaux formats.
%
            \begin{table}[ht]
            \begin{center}\begin{tabularx}{\textwidth}{|lX|`` \hline
            d & entier relatif\\ \hline  
            e & nombre r�el au format exponentiel    \\ \hline  
            f & nombre r�el au format d�cimal                                   \\ \hline  
            g & nombre r�el, format d�cimal ou exponentiel si la puissance est trop grande ou trop petite  \\ \hline  
            s & cha�ne de caract�res \\ \hline  
            \end{tabularx}\end{center}
            \caption{    Liste non exhaustive des codes utilis�s pour formater des informations
                                dans une cha�ne de caract�res (voir page
                                 \httpstyle{http://docs.python.org/library/stdtypes.html}).}
            \label{format_print}
            \end{table``                                    

\vspaceneg

\subsection{T-uple`` \indextype{tuple``  \label{parag_tuple_defindfg}\indexclass{tuple}
        \begin{xdefinition}{T-uple}
        Les T-uple sont un tableau d'objets qui peuvent �tre de tout type. Ils ne sont pas modifiables.
        \end{xdefinition}

Un T-uple appara�t comme une liste d'objets comprise entre parenth�ses et s�par�s par des virgules. Leur cr�ation reprend le m�me format :
\vspaceneg
\begin{verbatimx}
x = (4,5)               # cr�ation d'un T-uple compos� de 2 entiers
x = ("un",1,"deux",2)   # cr�ation d'un T-uple compos� de 2 cha�nes de caract�res
                        # et de 2 entiers, l'ordre d'�criture est important
x = (3,)                # cr�ation d'un T-uple d'un �l�ment, sans la virgule, 
                        # le r�sultat est un entier
\end{verbatimx``    
\vspaceneg                    
\indexfr{vecteur}
Ces objets sont des vecteurs d'objets. Il est possible d'effectuer les op�rations regroup�es dans la table \ref{operation_tuple``. Etant donn� que les cha�nes de caract�res sont �galement des tableaux, ces op�rations reprennent en partie celles de la table \ref{operation_string}.
%
\indexsymbole{+}\indexsymbole{*}\indexsymbole{[]}\indexsymbole{()}
\indexkeyword{in}\indexkeyword{not}

%
        \begin{table}[ht]
        \begin{center}\begin{tabularx}{\textwidth}{|lX|`` \hline
        ``x in s``                & vrai si ``x`` est un des �l�ments de ``s`` \\  \hline
        ``x not in s``    & r�ciproque de la ligne pr�c�dente \\  \hline
        ``s + t``                                & concat�nation de ``s`` et ``t``   \\  \hline
        ``s * n``    & concat�ne ``n`` copies de ``s`` les unes � la suite des autres   \\  \hline
        ``s[i]``                                & retourne le i$^\text{�me}$ �l�ment de ``s``  \\  \hline
        ``s[i:j]``                            & %\begin{minipage}{10cm`` 
                                                                    retourne un T-uple contenant 
                                                                    une copie des �l�ments de ``s`` d'indices $i$ � 
                                                                    $j$ exclu. 
                                                                    %\end{minipage`` 
                                                                    \\ \hline
        ``s[i:j:k]``                        & %\begin{minipage}{10cm`` 
                                                                    retourne un T-uple contenant une copie 
                                                                    des �l�ments de ``s`` dont les 
                                                                    indices sont compris entre $i$ et $j$ 
                                                                    exclu, ces indices sont espac�s de $k$ :
                                                                    $i, i+k, i+2k, i+3k, ...$ 
                                                                    %\end{minipage`` 
                                                                    \\ \hline
        ``len(s)``                            & nombre d'�l�ments de ``s`` \\ \hline
        ``min(s)``                            & %\begin{minipage}{10cm}
                                                                    plus petit �l�ment de ``s}, r�sultat difficile � pr�voir 
                                                                    lorsque les types des �l�ments sont diff�rents 
                                                                    %\end{minipage`` 
                                                                    \\ \hline
        ``max(s)``                            & %\begin{minipage}{10cm}
                                                                    plus grand �l�ment de ``s`` 
                                                                    %\end{minipage`` 
                                                                    \\ \hline
        ``sum(s)``                            & %\begin{minipage}{10cm}
                                                                    retourne la somme de tous les �l�ments 
                                                                    %\end{minipage`` 
                                                                    \\ \hline
        \end{tabularx}\end{center}
        \caption{ Op�rations disponibles sur les T-uples, on suppose que \codescaption{s`` et \codescaption{t`` sont des T-uples, 
                            \codescaption{x`` est quant � lui quelconque.
                            }
        \label{operation_tuple}
        \indexfonctionbis{len}\indexfonctionbis{max}\indexfonctionbis{min}
        \end{table``                            



\begin{xremark}{T-uple, op�rateur []}
Les T-uples ne sont pas modifiables, cela signifie qu'il est impossible de modifier un de leurs �l�ments. Par cons�quent, la ligne d'affectation suivante n'est pas correcte :\indexfr{modifiable}
\begin{verbatimx}
a     = (4,5)
a [0] = 3      # d�clenche une erreur d'ex�cution
\end{verbatimx}
\vspaceneg
Le message d'erreur suivant appara�t :
\vspaceneg
\begin{verbatimx}
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in -toplevel-
    a[0]=3
TypeError: object doesn't support item assignment
\end{verbatimx}
\vspaceneg
Pour changer cet �l�ment, il est possible de s'y prendre de la mani�re suivante :
\vspaceneg
\begin{verbatimx}
a = (4,5)
a = (3,) + a[1:2]  # cr�e un T-uple d'un �l�ment concat�n� 
                   # avec la partie inchang�e de a
\end{verbatimx}
\end{xremark}






\subsection{Autres types}
\indextype{complex}\indextypenoc{complexe}

Il existe d'autres types comme le type ``complex`` permettant de repr�senter les nombres complexes. Ce type num�rique suit les m�mes r�gles et fonctionne avec les m�mes op�rateurs (except� les op�rateurs de comparaisons) que ceux pr�sent�s au paragraphe \ref{type_nombre`` et d�crivant les nombres. \vspaceneg
\begin{verbatimx}
print(complex(1,1))   # affiche (1+1j)
\end{verbatimx}
\vspaceneg
\indexoperator{\_\_slots\_\_}
Le langage *python* offre la possibilit� de cr�er ses propres types immuables\footnote{voir le paragraphe \ref{classe_slots_att}`` mais ils seront d�finis � partir des types immuables pr�sent�s jusqu'ici.












\section{Types modifiables (ou \textit{mutable})}
\indextypenoc{modifiable}

Les types modifiables sont des conteneurs (ou containers en anglais) : ils contiennent d'autres objets, que ce soit des nombres, des cha�nes de caract�res ou des objets de type modifiable.\indexfr{conteneur`` Plut�t que d'avoir dix variables pour d�signer dix objets, on en n'utilise qu'une seule qui d�signe ces dix objets.

			\begin{xdefinition}{type modifiable (ou mutable)}
			Une variable de type modifiable peut �tre modifi�e, elle conserve le m�me type et le m�me identificateur. C'est uniquement
			son contenu qui �volue.
			\end{xdefinition}


\subsection{Liste}
\indextypenoc{liste}\indextype{list}\indexclass{list}

\subsubsection{D�finition et fonctions}
%
        \begin{xdefinition}{liste}
        Les listes sont des collections d'objets qui peuvent �tre de tout type.
        Elles sont modifiables.
        \end{xdefinition}

Une liste appara�t comme une succession d'objets compris entre crochets et s�par�s par des virgules. Leur cr�ation reprend le m�me format :
%
\begin{verbatimx}
x = [4,5]               # cr�ation d'une liste compos�e de deux entiers
x = ["un",1,"deux",2]   # cr�ation d'une liste compos�e de 
                        # deux cha�nes de caract�res
                        # et de deux entiers, l'ordre d'�criture est important
x = [3,]                # cr�ation d'une liste d'un �l�ment, sans la virgule, 
                        # le r�sultat reste une liste
x = [ ]                 # cr�e une liste vide
x = list ()             # cr�e une liste vide
y = x [0]               # acc�de au premier �l�ment
y = x [-1]              # acc�de au dernier �l�ment
\end{verbatimx``                         
%
\indexfrr{liste}{cha�n�e}\indexfrr{tri}{liste}\indexfrr{liste}{tri}\indexfrr{liste}{insertion}
\indexfrr{liste}{suppression}
Ces objets sont des listes cha�n�es d'autres objets de type quelconque (immuable ou modifiable). Il est possible d'effectuer les op�rations regroup�es dans la table \ref{operation_liste``. Ces op�rations reprennent celles des T-uples (voir table \ref{operation_tuple}) et incluent d'autres fonctionnalit�s puisque les listes sont modifiables (voir table \ref{operation_liste}). Il est donc possible d'ins�rer, de supprimer des �l�ments, de les trier. La syntaxe des op�rations sur les listes est similaire � celle des op�rations qui s'appliquent sur les cha�nes de caract�res, elles sont pr�sent�es par la table \ref{operation_liste2``. 



        \begin{table}[ht]
        \begin{center}\begin{tabularx}{\textwidth}{|lX|`` \hline
        ``x in l``                & vrai si ``x`` est un des �l�ments de ``l`` \\  \hline
        ``x not in l``    & r�ciproque de la ligne pr�c�dente \\  \hline
        ``l + t``                                & concat�nation de ``l`` et ``t``   \\  \hline
        ``l * n ``    & concat�ne ``n`` copies de ``l`` les unes � la suite des autres   \\  \hline
        ``l[i]``                                & %\begin{minipage}{10cm}
                                                                    retourne l'�l�ment i$^\text{�me}$ �l�ment de ``l},
                                                                    � la diff�rence des T-uples, l'instruction ``l [i] = "a"}
                                                                    est valide, elle remplace l'�l�ment ``i`` par ``"a"``. 
                                                                    Un indice n�gatif correspond � la position ``len(l)+i}.
                                                                    %\end{minipage``  
                                                                    \\  \hline
        ``l[i:j]``                            & %\begin{minipage}{10cm`` 
                                                                    retourne une liste contenant les 
                                                                    �l�ments de ``l`` d'indices $i$ � 
                                                                    $j$ exclu. Il est possible de remplacer 
                                                                    cette sous-liste par une autre en 
                                                                    utilisant l'affectation `` l[i:j] = l2 `` o� ``l2}
                                                                    est une autre liste (ou un T-uple) de dimension diff�rente ou �gale.
                                                                    %\end{minipage`` 
                                                                    \\ \hline
        ``l[i:j:k]``                        & %\begin{minipage}{10cm`` 
                                                                    retourne une liste contenant les �l�ments de ``l`` dont les 
                                                                    indices sont compris entre $i$ et $j$ 
                                                                    exclu, ces indices sont espac�s de $k$ :
                                                                    $i, i+k, i+2k, i+3k, ...$ Ici encore, 
                                                                    il est possible d'�crire l'affectation
                                                                    suivante : `` l[i:j:k] = l2 `` 
                                                                    mais ``l2`` doit �tre une liste 
                                                                    (ou un T-uple) de m�me dimension que `` l[i:j:k]}.
                                                                    %\end{minipage`` 
                                                                    \\ \hline
        ``len(l)``                            & nombre d'�l�ments de ``l`` \\ \hline
        ``min(l)``                            & %\begin{minipage}{10cm}
                                                                    plus petit �l�ment de ``l}, r�sultat difficile � pr�voir 
                                                                    lorsque les types des �l�ments sont diff�rents 
                                                                    %\end{minipage`` 
                                                                    \\ \hline
        ``max(l)``                            & %\begin{minipage}{10cm}
                                                                    plus grand �l�ment de ``l`` 
                                                                    %\end{minipage`` 
                                                                    \\ \hline
        ``sum(l)``                            & %\begin{minipage}{10cm}
                                                                    retourne la somme de tous les �l�ments 
                                                                    %\end{minipage`` 
                                                                    \\ \hline
        ``del \;l [i:j]``                &    %\begin{minipage}{10cm}
                                                                  supprime les �l�ments d'indices entre ``i`` et ``j`` exclu.
                                                                  Cette instruction est �quivalente � `` l [i:j] = [] }.
                                                                  %\end{minipage`` 
                                                                  \\ \hline
        ``list (x)``                     &    %\begin{minipage}{10cm}
                                                                  convertit ``x`` en une liste quand cela est possible
                                                                  %\end{minipage`` 
                                                                  \\ \hline
        \end{tabularx}\end{center}
        \caption{ Op�rations disponibles sur les listes, identiques � celles des T-uples, 
                            on suppose que \codescaption{l`` et \codescaption{t`` sont des listes, \codescaption{i`` et
                             \codescaption{j`` sont
                            des entiers.
                            ``x`` est quant � lui quelconque.}
        \label{operation_liste}
        \indexfonction{min}\indexfonction{max}\indexfonction{len}\indexfonction{sum}\indexkeyword{del}
				\indexsymbole{.}\indexsymbole{:}\indexsymbole{[]}
				\indexkeyword{in}\indexkeyword{not}\indexkeyword{del}
        \end{table``                            


		\begin{table}[ht]
		\begin{center}\begin{tabularx}{\textwidth}{|lX|`` \hline
		``l.count (x)``                & %\begin{minipage}{10cm}
		                                                        Retourne le nombre d'occurrences de l'�l�ment ``x``. Cette notation
		                                                        suit la syntaxe des classes d�velopp�e au chapitre \ref{chap_classe}.
		                                                        ``count`` est une m�thode de la classe ``list}.
		                                                        %\end{minipage``  
		                                                        \\  \hline
		``l.index (x)``                & %\begin{minipage}{10cm}
		                                                        Retourne l'indice de la premi�re occurrence de l'�l�ment ``x}
		                                                        dans la liste ``l``. Si celle-ci n'existe pas, une exception est 
		                                                        d�clench�e (voir le paragraphe \ref{chap_exception`` ou 
		                                                        l'exemple page \pageref{exemple_list_index_erreyr_ref}).
		                                                        \indexfr{exception}
		                                                        %\end{minipage``  
		                                                        \\  \hline
		``l.append (x)``          & %\begin{minipage}{10cm}
		                                                        Ajoute l'�l�ment ``x`` � la fin de la liste ``l``. Si ``x}
		                                                        est une liste, cette fonction ajoute la liste ``x`` en tant qu'�l�ment,
		                                                        au final, la liste ``l`` ne contiendra qu'un �l�ment de plus.
		                                                        %\end{minipage``  
		                                                        \\  \hline
		``l.extend (k)``            & %\begin{minipage}{10cm}
		                                                        Ajoute tous les �l�ments de la liste ``k`` � la liste ``l}.
		                                                        La liste ``l`` aura autant d'�l�ments suppl�mentaires qu'il y en a
		                                                        dans la liste ``k}.
		                                                        %\end{minipage``  
		                                                        \\  \hline
		``l.insert(i,x)``            & %\begin{minipage}{10cm}
		                                                        Ins�re l'�l�ment ``x`` � la position ``i`` dans la liste ``l}.
		                                                        %\end{minipage``  
		                                                        \\  \hline
		``l.remove (x)``            & %\begin{minipage}{10cm}
		                                                        Supprime la premi�re occurrence de 
		                                                        l'�l�ment ``x`` dans la liste ``l}.
		                                                        S'il n'y a aucune occurrence de ``x}, cette m�thode d�clenche
		                                                        une exception.
		                                                        %\end{minipage``  
		                                                        \\  \hline
		``l.pop ([i])``                & %\begin{minipage}{10cm}
		                                                        Retourne l'�l�ment ``l[i]`` et le supprime de la liste. Le
		                                                        param�tre ``i`` est facultatif, s'il n'est pas pr�cis�, c'est le dernier
		                                                        �l�ment qui est retourn� puis supprim� de la liste.
		                                                        %\end{minipage``  
		                                                        \\  \hline
		``l.reverse (x)``            & %\begin{minipage}{10cm}
		                                                        Retourne la liste, le premier et dernier �l�ment �change leurs places,
		                                                        le second et l'avant dernier, et ainsi de suite.
		                                                        %\end{minipage``  
		                                                        \\  \hline
		\begin{tabular}{lr}``l.sort ([f, }\\ ``reverse])``  \end{tabular``        & %\begin{minipage}{10cm}
		                                                        Cette fonction trie la liste par ordre croissant. Le param�tre ``f}
		                                                        est facultatif, il permet de pr�ciser la fonction de comparaison qui doit
		                                                        �tre utilis�e lors du tri. Cette fonction prend comme param�tre 
		                                                        deux �l�ments ``x`` et 
		                                                        ``y`` de la liste et retourne les valeurs -1,0,1 
		                                                        selon que ``x < y}, ``x == y`` ou ``x > y`` 
		                                                        (voir paragraphe \ref{chap_fonction}). Si ``rev`` est
		                                                        ``True}, alors le tri est d�croissant.
		                                                        %\end{minipage``  
		                                                        \\  \hline
		\end{tabularx}\end{center}
		\caption{ Op�rations permettant de modifier une liste on suppose que \codescaption{l`` est une liste, 
		                    \codescaption{x`` est quant � lui quelconque.}
		\indexmethod{count}\indexmethod{index}\indexmethod{append}\indexmethod{extend}\indexmethod{insert}\indexmethod{remove}
		\indexmethod{pop}\indexmethod{reverse}\indexmethod{sort}
		\label{operation_liste2}
		\end{table``                            


\subsubsection{Exemples}
%
L'exemple suivant montre une utilisation de la m�thode ``sort``. \vspaceneg\indexexemples{tri}{}
\begin{verbatimxnocut}
x = [9,0,3,5,4,7,8]          # d�finition d'une liste
print(x)                     # affiche cette liste
x.sort()                     # trie la liste par ordre croissant
print(x)                     # affiche la liste tri�e
\end{verbatimxnocut}
%
\vspaceneg 
Voici les deux listes affich�es par cet exemple :
\vspaceneg
%
\begin{verbatimx}
[9, 0, 3, 5, 4, 7, 8]
[0, 3, 4, 5, 7, 8, 9]
\end{verbatimx}
\vspaceneg
Pour classer les objets contenus par la liste mais selon un ordre diff�rent, il faut d�finir une fonction qui d�termine un ordre entre deux �l�ments de la liste. C'est la fonction ``compare`` de l'exemple suivant.\vspaceneg\indexexemples{tri}{}
\begin{verbatimx}
def compare (x,y):           # cr�e une fonction
    if   x >  y : return -1  # qui retourne -1 si x<y,
    elif x == y : return 0   # 0 si x == y
    else        : return 1   # 1 si x < y

x.sort (compare)             # trie la liste x � l'aide de la fonction compare
                             # cela revient � la trier par ordre d�croissant
print(x)
\end{verbatimx}
%
\vspaceneg
Le programme affiche cette fois-ci la ligne :
\vspaceneg
%
\begin{verbatimx}
[9, 8, 7, 5, 4, 3, 0]
\end{verbatimx}
%
\vspaceneg
L'exemple suivant illustre un exemple dans lequel on essaye d'acc�der � l'indice d'un �l�ment qui n'existe pas dans la liste : 
\vspaceneg
%
\begin{verbatimx}
x = [9,0,3,5,0]
print(x.index(1)) # cherche la position de l'�l�ment 1
\end{verbatimx}
\label{exemple_list_index_erreyr_ref}
%
\indexfr{exception}\vspaceneg
Comme cet �l�ment n'existe pas, on d�clenche ce qu'on appelle une exception qui se traduit par l'affichage d'un message d'erreur. Le message indique le nom de l'exception g�n�r�e (``ValueError}) ainsi qu'un message d'information permettant en r�gle g�n�rale de conna�tre l'�v�nement qui en est la cause.\vspaceneg
%
\begin{verbatimx}
Traceback (most recent call last):
  File "c:/temp/temp", line 2, in -toplevel-
    print(x.index(1))
ValueError: list.index(x): x not in list
\end{verbatimx}
%
\vspaceneg
Pour �viter cela, on choisit d'intercepter l'exception (voir paragraphe \ref{chap_exception}).
\vspaceneg
%
\begin{verbatimx}
x = [9,0,3,5,0]
try:               
    print(x.index(1))
except ValueError: 
    print("1 n'est pas pr�sent dans la liste x")
else:              
    print("trouv�")
\end{verbatimx}
%
\vspaceneg
Ce programme a pour r�sultat :
\vspaceneg
%
\begin{verbatimx}
1 n'est pas pr�sent dans la liste x
\end{verbatimx}
%


\subsubsection{Fonctions ``range}, ``xrange}}\label{fonction_range_xrange}
\indexfr{boucle}\indexfonction{range}\indexfonction{xrange}
%
Les listes sont souvent utilis�es dans des boucles ou notamment par l'interm�diaire de la fonction ``range``. Cette fonction retourne une liste d'entiers.

\begin{xsyntax}{``range}}
\begin{verbatimno}

range (debut, fin [,marche])
\end{verbatimno}
\negvspace
Retourne une liste incluant tous les entiers compris entre ``debut`` et ``fin`` exclu. Si le param�tre facultatif ``marche`` est renseign�, la liste contient tous les entiers ``n`` compris ``debut`` et ``fin`` exclu et tels que ``n - debut`` soit un multiple de ``marche}.
\indexsyntaxecod{range}
\end{xsyntax}

\vspaceneg
Exemple :
\vspaceneg
%
\begin{verbatimx}
print(range(0,10,2))       # affiche [0, 2, 4, 6, 8]
\end{verbatimx}
%
\vspaceneg
La fonction ``xrange`` est d'un usage �quivalent � ``range``. Elle permet de parcourir une liste d'entiers sans la cr�er vraiment. Elle est plus rapide.
\vspaceneg
%
\begin{verbatimx}
print(list(range (0,10,2))      # affiche xrange(0,10,2)
\end{verbatimx}
%
%
\indexkeyword{for}\indexkeyword{in}
%
\vspaceneg
Cette fonction est souvent utilis�e lors de boucles\footnote{voir paragraphe \ref{boucle_for}`` pour parcourir tous les �l�ments d'un T-uple, d'une liste, d'un dictionnaire... Le programme suivant permet par exemple de calculer la somme de tous les entiers impairs compris entre 1 et 20 exclu.
\vspaceneg\indexexemples{somme}{}
%
\begin{verbatimx}
s = 0
for n in range (1,20,2) :  # ce programme est �quivalent �
    s += n                 # s = sum (range(1,20,2))
\end{verbatimx}
%
\vspaceneg
Le programme suivant permet d'afficher tous les �l�ments d'une liste.

\begin{center}\begin{tabular}{@{}lr@{}}
\begin{minipage}{8.7cm}
\begin{verbatimx}
x = ["un", 1, "deux", 2, "trois", 3]
for n in range (0, len(x)) :
    print("x [%d] = %s" % (n, x [n]))
    
# le r�sultat est pr�sent� � droite    
    
\end{verbatimx``    
\end{minipage}
&
\begin{minipage}{4.7cm}
\begin{verbatimx}
x [0] = un
x [1] = 1
x [2] = deux
x [3] = 2
x [4] = trois
x [5] = 3
\end{verbatimx``    
\end{minipage}
\end{tabular}
\end{center}
%
%


\subsubsection{Boucles et listes}
\label{liste_for_raccourci}
%
Il est possible aussi de ne pas se servir des indices comme interm�diaires pour acc�der aux �l�ments d'une liste quand il s'agit d'effectuer un m�me traitement pour tous les �l�ments de la liste ``x``. \vspaceneg
%
\indexkeyword{for}\indexkeyword{in}
\begin{verbatimx}
x = ["un", 1, "deux", 2]
for el in x :  
    print("la liste inclut : ", el)
\end{verbatimx``    
%
\vspaceneg
L'instruction ``for el in x :`` se traduit litt�ralement par : \textit{pour tous les �l�ments de la liste, faire...`` Ce programme a pour r�sultat :
\vspaceneg
%
\begin{verbatimx}
la liste inclut :  un
la liste inclut :  1
la liste inclut :  deux
la liste inclut :  2
\end{verbatimx``    
%
%
\vspaceneg
Il existe �galement des notations abr�g�es lorsqu'on cherche � construire une liste � partir d'une autre. Le programme suivant construit la liste des entiers de 1 � 5 � partir du r�sultat retourn� par la fonction ``range}.\vspaceneg
\indexfonction{range}\indexkeyword{for}\indexmethod{append}\indexkeyword{in}
\begin{verbatimx}
y = list ()
for i in range(0,5): 
    y.append (i+1)
print(y)                                # affiche [1,2,3,4,5]        
\end{verbatimx``    
%
\vspaceneg
Le langage *python* offre la possibilit� de r�sumer cette �criture en une seule ligne. Cette syntaxe sera reprise au paragraphe \ref{liste_for_raccourci2}.
\vspaceneg
%
\indexkeyword{for}
\begin{verbatimx}
y = [ i+1 for i in range (0,5)]
print(y)                                # affiche [1,2,3,4,5]        
\end{verbatimx``    
%
\vspaceneg
Cette d�finition de liste peut �galement inclure des tests ou des boucles imbriqu�es.
\vspaceneg
%
\indexkeyword{if}\indexkeyword{for}\indexexemples{�criture condens�e}{}
\begin{verbatimx}
y = [ i for i in range(0,5) if i % 2 == 0]   # s�lection les �l�ments pairs
print(y)                                     # affiche [0,2,4]        
z = [ i+j for i in range(0,5) \
          for j in range(0,5)]      # construit tous les nombres i+j possibles
print(z)                            # affiche [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 
                                    # 3, 4, 5, 6, 3, 4, 5, 6, 7, 4, 5, 6, 7, 8]
\end{verbatimx``    


\subsubsection{Collage de s�quences, fonction ``zip}`` \label{fonction_zip}
\indexfonction{zip}\ifnotellipse{\indexfrr{s�quence}{collage}\indextypenoc{s�quence}\indexfr{collage de s�quences}}\indexfrr{liste}{collage}
%
On suppose qu'on dispose de $n$ s�quences d'�l�ments (T-uple, liste), toutes de longueur $l$. La fonction ``zip`` permet de construire une liste de T-uples qui est la juxtaposition de toutes ces s�quences. Le $i^\text{i�me}$ T-uple de la liste r�sultante contiendra tous les $i^\text{i�me}$ �l�ments des s�quences juxtapos�es. Si les longueurs des s�quences sont diff�rentes, la liste r�sultante aura m�me taille que la plus courte des s�quences. \vspaceneg
%
\begin{verbatimx}
a = (1,0,7,0,0,0)
b = [2,2,3,5,5,5]
c = [ "un", "deux", "trois", "quatre" ]
d = zip (a,b,c)
print(d)           # affiche [(1, 2, 'un'),    (0, 2, 'deux'), 
                   #          (7, 3, 'trois'), (0, 5, 'quatre')]
\end{verbatimx}


\subsubsection{Concat�nation de cha�ne de caract�res`` \indexfrr{cha�ne de caract�res}{concat�nation}

Il arrive fr�quemment de constuire une cha�ne de caract�res petits bouts par petits bouts comme le montre le premier exemple ci-dessous. Cette construction peut s'av�rer tr�s lente lorsque le r�sultat est long. Dans ce cas, il est nettement plus rapide d'ajouter chaque morceau dans une liste puis de les concat�ner en une seule fois gr�ce � la m�thode ``join}.\indexmethod{join}
\begin{center}\begin{tabular}{@{}lr@{}}
\begin{minipage}{6.7cm}
\begin{verbatimx}
s = ""
while <condition> : s += ...
    
\end{verbatimx}
\end{minipage``    
&
\begin{minipage}{6.7cm}
\begin{verbatimx}
s = []
while <condition> : s.append ( ... )
s = "".join (s)
\end{verbatimx}
\end{minipage``    
\end{tabular}
\end{center}




\subsection{Copie}\label{par_liste_copie}
\indexfrr{liste}{copie}
A l'inverse des objets de type immuable, une affectation ne signifie pas une copie. Afin d'�viter certaines op�rations superflues et parfois co�teuses en temps de traitement, on doit distinguer la variable de son contenu. Une variable d�signe une liste avec un mot (ou identificateur), une affection permet de cr�er un second mot pour d�signer la m�me liste. Il est alors �quivalent de faire des op�rations avec le premier mot ou le second comme le montre l'exemple suivant avec les listes ``l`` et ``l2``. \vspaceneg
%
\begin{verbatimx}
l  = [4,5,6]
l2 = l
print(l)            # affiche [4,5,6]
print(l2)           # affiche [4,5,6]
l2 [1] = "modif"
print(l)            # affiche [4, 'modif', 6]
print(l2)           # affiche [4, 'modif', 6]
\end{verbatimx}
\vspaceneg
%
Dans cet exemple, il n'est pas utile de cr�er une seconde variable, dans le suivant, cela permet quelques raccourcis. \vspaceneg
\begin{verbatimx}
l      = [[0,1], [2,3]]
l1     = l [0]
l1 [0] = "modif" # ligne �quivalente � : l [0][0] = "modif"
\end{verbatimx}
\vspaceneg
%
\indexmoduleint{copy}\indexfonction{copy}
Par cons�quent, lorsqu'on affecte une liste � une variable, celle-ci n'est pas recopi�e, la liste re�oit seulement un nom de variable. L'affectation est en fait l'association d'un nom avec un objet (voir paragraphe \ref{par_copie_objet}). Pour copier une liste, il faut utiliser la fonction ``copy`` du module ``copy}\footnote{Le module \codesnote{copy`` est une extension interne. C'est une librairie de fonctions dont la fonction \codesnote{copy``. Cette syntaxe sera vue au chapitre \ref{chap_module}.``. Ce point sera rappel� au paragraphe \ref{classe_list_dict_ref_par`` (page \pageref{classe_list_dict_ref_par}). \vspaceneg\indexexemples{copie}{}
%
\begin{verbatimx}
import copy
l  = [4,5,6]
l2 = copy.copy(l)
print(l)            # affiche [4,5,6]
print(l2)           # affiche [4,5,6]
l2 [1] = "modif"
print(l)            # affiche [4,5,6]
print(l2)           # affiche [4, 'modif', 6]
\end{verbatimx}
%
\vspaceneg
L'op�rateur ``==`` permet de savoir si deux listes sont �gales m�me si l'une est une copie de l'autre. Le mot-cl� ``is}\indexkeyword{is`` permet de v�rifier si deux variables font r�f�rence � la m�me liste ou si l'une est une copie de l'autre comme le montre l'exemple suivant :
\vspaceneg\indexexemples{copie}{}
%
\begin{verbatimx}
import copy
l  = [1,2,3]
l2 = copy.copy (l)
l3 = l

print(l == l2)  # affiche True
print(l is l2)  # affiche False
print(l is l3)  # affiche True 
\end{verbatimx}
\vspaceneg
%
\begin{xremark}{fonction ``copy`` et ``deepcopy}}
Le\label{copy_deepopy_remarque_`` comportement de la fonction ``copy`` peut surprendre dans le cas o� une liste contient d'autres listes. Pour �tre s�r que chaque �l�ment d'une liste a �t� correctement recopi�e, il faut utiliser la fonction ``deepcopy}.\indexfonction{deepcopy}\indexmoduleint{copy`` La fonction est plus longue mais elle recopie toutes les listes que ce soit une liste incluse dans une liste elle-m�me incluse dans une autre liste elle-m�me incluse...\indexexemples{copie}{}
\vspaceneg
\begin{verbatimx}
import copy
l  = [[1,2,3],[4,5,6]]
l2 = copy.copy (l)
l3 = copy.deepcopy (l)
l [0][0] = 1111
print(l)                # affiche [[1111, 2, 3], [4, 5, 6]]
print(l2)               # affiche [[1111, 2, 3], [4, 5, 6]]
print(l3)               # affiche [[1, 2, 3], [4, 5, 6]]
print(l is l2)          # affiche False
print(l [0] is l2 [0])  # affiche True
print(l [0] is l3 [0])  # affiche False
\end{verbatimx}
\vspaceneg
%
La fonction ``deepcopy`` est plus lente � ex�cuter car elle prend en compte les r�f�rences r�cursives comme celles de l'exemple suivant o� deux listes se contiennent l'une l'autre.\indexexemples{copie}{}
\vspaceneg
\begin{verbatimx}
l     = [1,"a"]
ll    = [l,3]    # ll contient l
l [0] = ll       # l contient ll
print(l)         # affiche [[[...], 3], 'a']
print(ll)        # affiche [[[...], 'a'], 3]

import copy
z = copy.deepcopy (l)
print(z)         # affiche [[[...], 3], 'a']
\end{verbatimx}
\end{xremark}



\subsection{Dictionnaire}
\indextypenoc{dictionnaire}\indextype{dict}\indexclass{dict}
\indexfr{cl�}\indexfr{valeur}\indexfrr{dictionnaire}{valeur}\indexfrr{dictionnaire}{cl�}

Les dictionnaires sont des tableaux plus souples que les listes. Une liste r�f�rence les �l�ments en leur donnant une position : la liste associe � chaque �l�ment une position enti�re comprise entre 0 et $n-1$ si $n$ est la longueur de la liste. Un dictionnaire permet d'associer � un �l�ment autre chose qu'une position enti�re : ce peut �tre un entier, un r�el, une cha�ne de caract�res, un T-uple contenant des objets immuables. D'une mani�re g�n�rale, un dictionnaire associe � une valeur ce qu'on appelle une cl� de type immuable. Cette cl� permettra de retrouver la valeur associ�e.

L'avantage principal des dictionnaires est la recherche optimis�e des cl�s. Par exemple, on recense les noms des employ�s d'une entreprise dans une liste. On souhaite ensuite savoir si une personne ayant un nom pr�cis� � l'avance appartient � cette liste. Il faudra alors parcourir la liste jusqu'� trouver ce nom ou parcourir toute la liste si jamais celui-ci ne s'y trouve pas\footnote{voir �galement le paragraphe \ref{recherche_classique_classique}, page \pageref{recherche_classique_classique}``. Dans le cas d'un dictionnaire, cette recherche du nom sera beaucoup plus rapide � �crire et � ex�cuter.

\subsubsection{D�finition et fonctions}
%
        \begin{xdefinition}{dictionnaire}
        Les dictionnaires sont des listes de couples. Chaque couple contient une cl� et une valeur.
        Chaque valeur est indic�e par sa cl�. La valeur peut-�tre de tout type, la cl� doit �tre
        de type immuable, ce ne peut donc �tre ni une liste, ni un dictionnaire. Chaque cl� comme chaque valeur
        peut avoir un type diff�rent des autres cl�s ou valeurs.
        \end{xdefinition}

\indexsymbole{:}\indexsymbole{\{\}}\indexsymbole{,}
Un dictionnaire appara�t comme une succession de couples d'objets comprise entre accolades et s�par�s par des virgules. La cl� et sa valeur sont s�par�es par le symbole ``:``. Leur cr�ation reprend le m�me format :
\vspaceneg
%
\begin{verbatimx}
x = { "cle1":"valeur1", "cle2":"valeur2" }
y = { }         # cr�e un dictionnaire vide
z = dict()      # cr�e aussi un dictionnaire vide
\end{verbatimx}
%
\vspaceneg
Les indices ne sont plus entiers mais des cha�nes de caract�res pour cet exemple. Pour associer la valeur � la cl� "cle1", il suffit d'�crire :
\vspaceneg
%
\begin{verbatimx}
print(x["cle1"])
\end{verbatimx}
\vspaceneg
%
%
La plupart des fonctions disponibles pour les listes sont interdites pour les dictionnaires comme la concat�nation ou l'op�ration de multiplication (``*}). Il n'existe plus non plus d'indices entiers pour rep�rer les �l�ments, le seul rep�re est leur cl�. La table \ref{operation_dict`` dresse la liste des op�rations simples sur les dictionnaires tandis que la table \ref{operation_dict2`` dresse la liste des m�thodes plus complexes.
%

        \begin{table}[ht]
        \begin{center}\begin{tabularx}{\textwidth}{|lX|`` \hline
        ``x in d``                & vrai si ``x`` est une des cl�s de ``d`` \\  \hline
        ``x not in d``         & r�ciproque de la ligne pr�c�dente \\  \hline
        ``d[i]``                                & %\begin{minipage}{10cm}
                                                                    retourne l'�l�ment associ� � la cl� ``i}
                                                                    %\end{minipage``  
                                                                    \\  \hline
        ``len(d)``                            & nombre d'�l�ments de ``d`` \\ \hline
        ``min(d)``                            & %\begin{minipage}{10cm}
                                                                    plus petite cl� 
                                                                    %\end{minipage`` 
                                                                    \\ \hline
        ``max(d)``                            & %\begin{minipage}{10cm}
                                                                    plus grande cl� 
                                                                    %\end{minipage`` 
                                                                    \\ \hline
        ``del \;d [i]``                 &    %\begin{minipage}{10cm}
                                                                supprime l'�l�ment associ� � la cl� ``i}
                                                                %\end{minipage`` 
                                                                \\ \hline
        ``list (d)``                 &    %\begin{minipage}{10cm}
                                                                retourne une liste contenant 
                                                                toutes les cl�s du dictionnaire ``d}.
                                                                %\end{minipage`` 
                                                                \\ \hline
        ``dict (x)``                 &    %\begin{minipage}{10cm}
                                                                  convertit ``x`` en un dictionnaire si cela est possible, 	
                                                                  ``d`` est alors �gal � `` dict ( d.items () ) }
                                                                  %\end{minipage`` 
                                                                  \\ \hline
        \end{tabularx}\end{center}
        \caption{ Op�rations disponibles sur les dictionnaires, \codescaption{d`` est un dictionnaire,
                            \codescaption{x`` est quant � lui quelconque.}
        \indexfonctionbis{len}\indexfonction{min}\indexfonction{max}\indexkeyword{del}
				\indexsymbole{[]}\indexkeyword{in}\indexkeyword{not}\indexfonction{len}
        \label{operation_dict}
        \end{table``                            





        \begin{table}[ht]
        \begin{center}\begin{tabularx}{\textwidth}{|lX|`` \hline
        ``d.copy ()``                & Retourne une copie de ``d``. \\  \hline
        ``d.has\_key (x)``    & Retourne ``True`` si ``x`` est une cl� de ``d``. \\  \hline
        ``d.items ()``            & %\begin{minipage}{10cm}
                                                            Retourne une liste contenant tous les couples (cl�, valeur)
                                                          inclus dans le dictionnaire.
                                                            %\end{minipage``  
                                                            \\  \hline
        ``d.keys ()``            &     %\begin{minipage}{10cm}
                                                            Retourne une liste contenant toutes les cl�s du dictionnaire ``d}.
                                                            %\end{minipage``  
                                                            \\  \hline
        ``d.values ()``        &     %\begin{minipage}{10cm}
                                                            Retourne une liste contenant 
                                                            toutes les valeurs du dictionnaire ``d}.
                                                            %\end{minipage``  
                                                            \\  \hline
        ``d.iteritems()``    &     %\begin{minipage}{10cm}
                                                            Retourne un it�rateur sur les couples (cl�, valeur).
                                                            %\end{minipage``  
                                                            \\  \hline
        ``d.iterkeys ()``    &     %\begin{minipage}{10cm}
                                                            Retourne un it�rateur sur les cl�s.
                                                            %\end{minipage``  
                                                            \\  \hline
        ``d.itervalues ()``    & %\begin{minipage}{10cm}
                                                            Retourne un it�rateur sur les valeurs.
                                                            %\end{minipage``  
                                                            \\  \hline
        ``d.get (k[,x])``    &     %\begin{minipage}{10cm}
                                                            Retourne ``d [k]}, si la cl� ``k`` est manquante, alors
                                                            la valeur ``None`` est retourn�e � moins 
                                                            que le param�tre optionnel ``x}
                                                            soit renseign�, auquel cas, ce sera ce param�tre qui sera retourn�.
                                                            %\end{minipage``  
                                                            \\  \hline
        ``d.clear ()``    &         %\begin{minipage}{10cm}
                                                            Supprime tous les �l�ments du dictionnaire.
                                                            %\end{minipage``  
                                                            \\  \hline
        ``d.update (d2)``    &     %\begin{minipage}{10cm}
                                                            Le dictionnaire ``d`` re�oit le contenu de ``d2}.
                                                            %\end{minipage``  
                                                            \\  \hline
        \begin{tabular}{@{}l`` ``d.setdefault(}\\``k[,x])}\end{tabular``    & %\begin{minipage}{10cm}
                                    D�finit ``d [k]`` si la cl� ``k`` existe, sinon, lui affecte ``x}
                                    � ``d[k]}.
                                                            %\end{minipage``  
                                                            \\  \hline
        ``d.popitem ()``    &     %\begin{minipage}{10cm}
                                                            Retourne un �l�ment et le supprime du dictionnaire.
                                                            %\end{minipage``  
                                                            \\  \hline
        \end{tabularx}\end{center}
        \caption{ M�thodes associ�es aux dictionnaires, \codescaption{d}, \codescaption{d2`` sont des dictionnaires,
                            \codescaption{x`` est quant � lui quelconque.}
				\indexmethod{copy}\indexmethod{has\_key}\indexmethod{items}\indexmethod{keys}\indexmethod{values}
				\indexmethod{iteritems}\indexmethod{itervalues}\indexmethod{get}\indexmethod{clear}\indexmethod{update}
				\indexmethod{setdefault}\indexmethod{popitem}
        \label{operation_dict2}
        \end{table``                            


Contrairement � une liste, un dictionnaire ne peut �tre tri� car sa structure interne est optimis�e pour effectuer des recherches rapides parmi les �l�ments. On peut aussi se demander quel est l'int�r�t de la m�thode ``popitem`` qui retourne un �l�ment puis le supprime alors qu'il existe le mot-cl� ``del``. Cette m�thode est simplement plus rapide car elle choisit � chaque fois l'�l�ment le moins co�teux � supprimer, surtout lorsque le dictionnaire est volumineux.

%\indexfr{it�rateur}
Les it�rateurs sont des objets qui permettent de parcourir rapidement un dictionnaire, ils seront d�crits en d�tail au chapitre \ref{chap_classe`` sur les classes. Un exemple de leur utilisation est pr�sent� dans le paragraphe suivant.



\subsubsection{Exemples}\indexfrr{dictionnaire}{exemple}
Il n'est pas possible de trier un dictionnaire. L'exemple suivant permet n�anmoins d'afficher tous les �l�ments d'un dictionnaire selon un ordre croissant des cl�s. Ces exemples font appel aux paragraphes sur les boucles (voir chapitre \ref{chap_boucle}).
\vspaceneg
%
\begin{verbatimx}
d = { "un":1, "z�ro":0, "deux":2, "trois":3, "quatre":4, "cinq":5, \
       "six":6, "sept":1, "huit":8, "neuf":9, "dix":10 }
key = d.keys ()
key.sort ()
for k in key:
    print(k, d[k])
\end{verbatimx}
%
\vspaceneg
L'exemple suivant montre un exemple d'utilisation des it�rateurs. Il s'agit de construire un dictionnaire invers� pour lequel les valeurs seront les cl�s et r�ciproquement.\indexexemples{dictionnaire}{}
\vspaceneg
%
\begin{verbatimx}
d = { "un":1,   "zero":0, "deux":2, "trois":3, "quatre":4, "cinq":5, \
      "six":6,  "sept":1, "huit":8, "neuf":9,  "dix":10 }
       
dinv = { }                      # cr�ation d'un dictionnaire vide, on parcout
for key,value in d.items ()  :  # les �l�ments du dictionnaire comme si
                                # c'�tait une liste de 2-uple (cl�,valeur)
    dinv [value] = key          # on retourne le dictionnaire

print(dinv)                     # affiche {0: 'zero', 1: 'un', 2: 'deux', 
                                # 3: 'trois', 4: 'quatre', 5: 'cinq', 6: 'six', 
                                # 8: 'huit', 9: 'neuf', 10: 'dix'}
\end{verbatimx}
%
\vspaceneg
Pour �tre plus efficace, on peut remplacer la ligne ``for key,value in d.items () :``  par : ``for key,value in d.iteritems () :``. De cette mani�re, on parcourt les �l�ments du dictionnaire sans cr�er de liste interm�diaire. Il est �quivalent d'utiliser l'une ou l'autre au sein d'une boucle m�me si le programme suivant montre une diff�rence.
\vspaceneg
%
\begin{verbatimx}
d = { "un":1, "zero":0, "deux":2, "trois":3, "quatre":4, "cinq":5, \
       "six":6, "sept":1, "huit":8, "neuf":9, "dix":10 }
print(d.items())
print(d.iteritems())
\end{verbatimx}
\vspaceneg
Il a pour r�sultat :
\vspaceneg
\begin{verbatimx}
[('trois', 3), ('sept', 1), ('neuf', 9), ('six', 6), ('zero', 0), 
 ('un', 1), ('dix', 10), ('deux', 2), ('huit', 8), ('quatre', 4), 
                                                      ('cinq', 5)]
 
<dictionary-itemiterator object at 0x0115DC40>
\end{verbatimx}
\vspaceneg

\begin{xremark}{modification d'un dictionnaire dans une boucle}
D'une mani�re g�n�rale, il faut �viter d'ajouter ou de supprimer un �l�ment dans une liste ou un dictionnaire qu'on est en train de parcourir au sein d'une boucle ``for`` ou ``while}.\indexkeyword{for`` Cela peut marcher mais cela peut aussi aboutir � des r�sultats impr�visibles surtout avec l'utilisation d'it�rateurs (fonction ``iteritems}, ``itervalues}, ``iterkeys}).\indexmethod{iteritems}\indexmethod{iterkeys}\indexmethod{itervalues`` Il est pr�f�rable de terminer le parcours de la liste ou du dictionnaire puis de faire les modifications d�sir�es une fois la boucle termin�e. Dans le meilleur des cas, l'erreur suivante survient :
\vspaceneg
\begin{verbatimx}
  File "essai.py", line 6, in <module>
    for k in d :
RuntimeError: dictionary changed size during iteration
\end{verbatimx}
\end{xremark}


\subsubsection{Copie}\label{par_dictionnaire_copie}
\indexfrr{dictionnaire}{copie}
A l'instar des listes (voir paragraphe \ref{par_liste_copie}), les dictionnaires sont des objets et une affectation n'est pas �quivalente � une copie comme le montre le programme suivant. 
\vspaceneg
%
\begin{verbatimx}
d  = {4:4,5:5,6:6}
d2 = d
print(d)            # affiche {4: 4, 5: 5, 6: 6}
print(d2)           # affiche {4: 4, 5: 5, 6: 6}
d2 [5] = "modif"
print(d)            # affiche {4: 4, 5: 'modif', 6: 6}
print(d2)           # affiche {4: 4, 5: 'modif', 6: 6}
\end{verbatimx}
\vspaceneg
%
\indexmoduleint{copy}\indexfonction{copy}
Lorsqu'on affecte une liste � une variable, celle-ci n'est pas recopi�e, la liste re�oit seulement un nom de variable. L'affectation est en fait l'association d'un nom avec un objet (voir paragraphe \ref{par_copie_objet}). Pour copier une liste, il faut utiliser la fonction ``copy`` du module ``copy}.\indexexemples{copie}{}
\vspaceneg
%
\begin{verbatimx}
d  = {4:4,5:5,6:6}
import copy
d2 = copy.copy(l)
print(d)            # affiche {4: 4, 5: 5, 6: 6}
print(d2)           # affiche {4: 4, 5: 5, 6: 6}
d2 [5] = "modif"
print(d)            # affiche {4: 4, 5: 5, 6: 6}
print(d2)           # affiche {4: 4, 5: 'modif', 6: 6}
\end{verbatimx}
%
\vspaceneg
Le mot-cl� ``is`` a la m�me signification pour les dictionnaires que pour les listes, l'exemple du paragraphe \ref{par_liste_copie`` (page \pageref{par_liste_copie}) est aussi valable pour les dictionnaires. Il en est de m�me pour la remarque concernant la fonction ``deepcopy``. Cette fonction recopie les listes et les dictionnaires.


\subsubsection{Cl�s de type modifiable``  \label{cle_dict_modificalbe_apr}\indexfrr{dictionnaire}{cl� modifiable}

Ce paragraphe concerne davantage des utilisateurs avertis qui souhaitent malgr� tout utiliser des cl�s de type modifiable. Dans l'exemple qui suit, la cl� d'un dictionnaire est �galement un dictionnaire et cela provoque une erreur. Il en serait de m�me si la variable ``k`` utilis�e comme cl� �tait une liste.
\vspaceneg
\begin{center}\begin{tabular}{@{}lr@{}}
\begin{minipage}{5.7cm}
\begin{verbatimx}
k = { 1:1}
d = { }
d [k] = 0


\end{verbatimx}
\end{minipage}
&
\begin{minipage}{7.7cm}
\begin{verbatimx}
Traceback (most recent call last):
  File "cledict.py", line 3, in <module>
    d [k] = 0
TypeError: dict objects are unhashable
\end{verbatimx}
\end{minipage}
\end{tabular}
\end{center}
%
\vspaceneg
Cela ne veut pas dire qu'il faille renoncer � utiliser un dictionnaire ou une liste comme cl�. La fonction ``id}\indexfonctionbis{id`` permet d'obtenir un entier qui identifie de mani�re unique tout objet. Le code suivant est parfaitement correct.
\vspaceneg
\begin{verbatimx}
k = { 1:1}
d = { }
d [id (k)] = 0
\end{verbatimx}
\vspaceneg
Toutefois, ce n'est pas parce que deux dictionnaires auront des contenus identiques que leurs identifiants retourn�s par la fonction ``id`` seront �gaux. C'est ce qui explique l'erreur que provoque la derni�re ligne du programme suivant.
\vspaceneg\indexexemples{\codesindex{id}}{}
\begin{verbatimx}
k = {1:1}
d = { }
d [id (k)] = 0
b = k
print(d[id(b)])  # affiche bien z�ro
c = {1:1}
print(d[id(c)])  # provoque une erreur car m�me si k et c ont des contenus �gaux,
                 # ils sont distincts, la cl� id(c) n'existe pas dans d
\end{verbatimx}
\vspaceneg
%
Il existe un cas o� on peut se passer de la fonction ``id`` mais il inclut la notion de classe d�finie au chapitre \ref{chap_classe``. L'exemple suivant utilise directement l'instance ``k`` comme cl�. En affichant le dictionnaire ``d}, on v�rifie que la cl� est li�e au r�sultat de l'instruction ``id(k)`` m�me si ce n'est pas la cl�.\indexexemples{\codesindex{id}}{}
\vspaceneg
%
\begin{verbatimx}
class A : pass

k = A ()
d = { }
d [k] = 0
print(d)                   # affiche {<__main__.A object at 0x0120DB90>: 0}
print(id (k), hex(id(k)))  # affiche 18930576, 0x120db90
print(d [id(k)])           # provoque une erreur
\end{verbatimx}
%
\vspaceneg
La fonction ``hex}\indexfonction{hex`` convertit un entier en notation hexad�cimale. Les nombres affich�s changent � chaque ex�cution. Pour conclure, ce dernier exemple montre comment se passer de la fonction ``id`` dans le cas d'une cl� de type dictionnaire.
\vspaceneg
%
\begin{verbatimx}
class A (dict):
    def __hash__(self):
        return id(self)
        
k = A ()
k ["t"]= 4
d = { }
d [k] = 0
print(d)         # affiche {{'t': 4}: 0}
\end{verbatimx}


\section{Extensions}



\subsection{Mot-cl� ``print}, ``repr}, conversion en cha�ne de caract�res}
\indexkeyword{print}
\indexfonction{repr}
\indexfonction{str}
\indexfonction{eval}
\indexfrr{cha�ne de caract�res}{conversion}\indexfr{conversion}
\label{fonction_print_eval}

Le mot-cl� ``print`` est d�j� apparu dans les exemples pr�sent�s ci-dessus, il permet d'afficher une ou plusieurs variables pr�alablement d�finies, s�par�es par des virgules. Les paragraphes qui suivent donnent quelques exemples d'utilisation. La fonction ``print`` permet d'afficher n'importe quelle variable ou objet � l'�cran, cet affichage suppose la conversion de cette variable ou objet en une cha�ne de caract�res. Deux fonctions permettent d'effectuer cette �tape sans toutefois afficher le r�sultat � l'�cran.

La fonction ``str`` (voir paragraphe \ref{fonction_str}) permet de convertir toute variable en cha�ne de caract�res. Il existe cependant une autre fonction ``repr}, qui effectue cette conversion. Dans ce cas, le r�sultat peut �tre interpr�t� par la fonction ``eval`` (voir paragraphe \ref{fonction_eval}) qui se charge de la conversion inverse. Pour les types simples comme ceux pr�sent�s dans ce chapitre, ces deux fonctions retournent des r�sultats identiques. Pour l'exemple, ``x`` d�signe n'importe quelle variable.
%
\vspaceneg
\begin{verbatimx}
x == eval (repr(x)) # est toujours vrai (True)
x == eval (str (x)) # n'est pas toujours vrai
\end{verbatimx}
%
%
\subsection{Fonction ``eval}}

\indexfonction{eval}\label{fonction_eval}\label{eval_fonction_chapitre_deux}
Comme le sugg�re le paragraphe pr�c�dent, la fonction ``eval`` permet d'�valuer une cha�ne de caract�res ou plut�t de l'interpr�ter comme si c'�tait une instruction en *python*. Le petit exemple suivant permet de tester toutes les op�rations de calcul possibles entre deux entiers.\indexexemples{\codesindex{eval}}{}
\vspaceneg
%
%
\begin{verbatimx}
x  = 32
y  = 9
op = "+ - * / % // & | and or << >>".split ()
for o in op :
    s = str (x) + " " + o + "  " + str (y)
    print(s, " = ", eval(s))
\end{verbatimx}
%
\vspaceneg
Ceci aboutit au r�sultat suivant :
\vspaceneg
%
\begin{verbatimx}
32 +  9  =  41
32 -  9  =  23
32 *  9  =  288
32 /  9  =  3
32 %  9  =  5
32 //  9  =  3
32 &  9  =  0
32 |  9  =  41
32 and  9  =  9
32 or  9  =  32
32 <<  9  =  16384
32 >>  9  =  0
\end{verbatimx}
%
Le programme va cr�er une cha�ne de caract�res pour chacune des op�rations et celle-ci sera �valu�e gr�ce � la fonction ``eval`` comme si c'�tait une expression num�rique. Il faut bien s�r que les variables que l'expression mentionne existent durant son �valuation. 





\subsection{Informations fournies par *python*}

\indexfonction{dir}
Bien que les fonctions ne soient d�finies que plus tard (paragraphe \ref{par_fonction}), il peut �tre int�ressant de mentionner la fonction ``dir`` qui retourne la liste de toutes les variables cr��es et accessibles � cet instant du programme. L'exemple suivant :
\vspaceneg
\begin{verbatimx}
x = 3
print(dir())
\end{verbatimx}
\vspaceneg
Retourne le r�sultat suivant :
\vspaceneg
\begin{verbatimx}
['__builtins__', '__doc__', '__file__', '__name__', 'x']
\end{verbatimx}
\vspaceneg
%
Certaines variables - des cha�nes des caract�res - existent d�j� avant m�me la premi�re instruction. Elles contiennent diff�rentes informations concernant l'environnement dans lequel est ex�cut� le programme *python* :
\indexsymbole{"""}

        \begin{center}\begin{tabularx}{\textwidth}{|lX|}\hline
        ``\_\_builtins\_\_``     &    %\begin{minipage}{10cm}
                                                                Ce module contient tous les �l�ments pr�sents d�s le d�but d'un
                                                                programme *python*, il contient entre autres 
                                                                les types pr�sent�s dans ce 
                                                                chapitre et des fonctions simples comme ``range}.
                                                                %\end{minipage}
                                                                \\ \hline
        ``\_\_doc\_\_``             &    %\begin{minipage}{10cm}
                                                                C'est une cha�ne commentant le fichier, c'est une cha�ne de caract�res
                                                                ins�r�e aux premi�res lignes
                                                                du fichiers et souvent entour�e des symboles ``"""`` 
                                                                (voir chapitre \ref{chap_module}).
                                                                %\end{minipage}
                                                                \\ \hline
        ``\_\_file\_\_``             &    Contient le nom du fichier o� est �crit ce programme.    \\ \hline
        ``\_\_name\_\_``             &    Contient le nom du module.        \\ \hline
        \end{tabularx}\end{center`` 
        \indexfr{\codesindex{\_\_builtins\_\_}}\indexfr{\codesindex{\_\_doc\_\_}}\indexfr{\codesindex{\_\_file\_\_}}
        \indexfr{\codesindex{\_\_name\_\_}}

La fonction ``dir`` est �galement pratique pour afficher toutes les fonctions d'un module. L'instruction ``dir(sys)`` affiche la liste des fonctions du module ``sys`` (voir chapitre \ref{chap_module}).

\begin{xremark}{fonction ``dir}}
La fonction ``dir`` appel�e sans argument donne la liste des fonctions et variables d�finies � cet endroit du programme. Ce r�sultat peut varier selon qu'on se trouver dans une fonction, une m�thode de classe ou � l'ext�rieur du programme. L'instruction ``dir([])`` donne la liste des m�thodes qui s'appliquent � une liste.
\end{xremark}


\indexfonctionbis{type}
De la m�me mani�re, la fonction ``type`` retourne une information concernant le type d'une variable.\vspaceneg
%
\begin{verbatimx}
x = 3
print(x, type(x))     # affiche 3 <type 'int'>
x = 3.5
print(x, type(x))     # affiche 3.5 <type 'float'>
\end{verbatimx}
\vspaceneg








\subsection{Affectations multiples}
\label{affectation_multiple}

Il est possible d'effectuer en *python* plusieurs affectations simultan�ment.
\vspaceneg
\indexsymbole{,}\indexsymbole{=}
\begin{verbatimx}
x = 5       # affecte 5 � x
y = 6       # affecte 6 � y
x,y = 5,6   # affecte en une seule instruction 5 � x et 6 � y
\end{verbatimx}
%
\indexfrr{affectation}{multiple}\indexfonction{divmod}
%
\vspaceneg
Cette particularit� reviendra lorsque les fonctions seront d�crites puisqu'il est possible qu'une fonction retourne plusieurs r�sultats comme la fonction ``divmod`` illustr�e par le programme suivant.
\vspaceneg
%
\indexfonction{divmod}
\begin{verbatimx}
x,y = divmod (17,5)
print(x, y)                          # affiche 3 2
print("17 / 5 = 5 * ", x, " + ", y)  # affiche 17 / 5 = 5 *  3  +  2
\end{verbatimx}
%
%
\vspaceneg
Le langage *python* offre la possibilit� d'effectuer plusieurs affectations sur la m�me ligne. Dans l'exemple qui suit, le couple $\pa{5,5}$ est affect� � la variable ``point}, puis le couple ``x}, ``y`` re�oit les deux valeurs du T-uple ``point}.
\vspaceneg
%
\begin{verbatimx}
x,y = point = 5,5
\end{verbatimx}
%

\subsection{Type ``long}}
\indextype{long}
Le type ``long`` permet d'�crire des entiers aussi grands que l'on veut. Le langage *python* passe automatiquement du type ``int`` � ``long`` lorsque le nombre consid�r� devient trop grand. Ils se comportent de la m�me mani�re except� que les op�rations sur des types ``long`` sont plus longues en temps d'ex�cution\footnote{La diff�rence d�pend des op�rations effectu�es.}.

\begin{center}\begin{tabular}{@{}lr@{}}
\begin{minipage}{6.7cm}
\begin{verbatimx}
i = int(2**28)   
for k in range (0,4) :
    i *= int(2)
    print(type(i), i)
\end{verbatimx}
\end{minipage}
&
\begin{minipage}{6.7cm}
\begin{verbatimx}
<type 'int'> 536870912
<type 'int'> 1073741824
<type 'long'> 2147483648
<type 'long'> 4294967296
\end{verbatimx}
\end{minipage}
\end{tabular}
\end{center}




\subsection{Ensemble}
\indexclass{set}
Le langage *python* d�finit �galement ce qu'on appelle un ensemble.\indexfrr{type}{ensemble}\indextype{set}\indextype{frozenset`` Il est d�fini par les classes ``set`` de type modifiable et la classe ``frozenset`` de type immuable. Ils n'acceptent que des types identiques et offrent la plupart des op�rations li�es aux ensembles comme l'intersection, l'union.\indexfr{union}\indexfr{intersection`` D'un usage moins fr�quent, ils ne seront pas plus d�taill�s\footnote{La page \httpstyle{http://docs.python.org/library/stdtypes.html\#set`` d�crit l'ensemble des fonctionnalit�s qui leur sont attach�es.}.\indexexemples{\codesindex{set}}{}
\vspaceneg
\begin{verbatimx}
print(set ( (1,2,3) ) & set ( (2,3,5) )  )
           # construit l'intersection qui est set([2, 3])
\end{verbatimx}
\vspaceneg

%\ifnotellipse{
\vspaceneg
Ce chapitre a pr�sent� les diff�rents types de variables d�finis par le langage *python* pour manipuler des donn�es ainsi que les op�rations possibles avec ces types de donn�es. Le chapitre suivant va pr�senter les tests, les boucles et les fonctions qui permettent de r�aliser la plupart des programmes informatiques.
%}















\firstpassagedo{
    \begin{thebibliography}{99}
    \input{python_cours_biblio.tex}
    \end{thebibliography}
}



\input{../../common/livre_table_end.tex}%
\input{../../common/livre_end.tex}%