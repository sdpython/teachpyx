
.. _l-regex:

.. _chap_regex:

======================
Expressions régulières
======================

.. contents::
    :local:
    :depth: 2

A quoi ça sert ?
================

Chercher un mot dans un texte est une tâche facile, c'est l'objectif
de la méthode `find <https://docs.python.org/3/library/stdtypes.html?highlight=find#str.find>`_
attachée aux chaînes de caractères, elle suffit encore lorsqu'on cherche
un mot au pluriel ou au singulier mais il faut l'appeler au moins
deux fois pour chercher ces deux formes. Pour des expressions plus
compliquées, il est conseillé d'utiliser les `expressions régulières <https://fr.wikipedia.org/wiki/Expression_rationnelle>`_.
C'est une fonctionnalité qu'on retrouve dans beaucoup de langages.
C'est une forme de grammaire qui permet de rechercher des expressions.

Lorsqu'on remplit un formulaire, on voit souvent le format ``"MM/JJ/AAAA"``
qui précise sous quelle forme on s'attend à ce qu'une date soit écrite.
Les expressions régulières permettent de définir également ce format
et de chercher dans un texte toutes les chaînes de caractères qui
sont conformes à ce format.

La liste qui suit contient des dates de naissance. On cherche à obtenir
toutes les dates de cet exemple sachant que les jours ou les mois
contiennent un ou deux chiffres, les années deux ou quatre.

::

    s = """date 0 : 14/9/2000
    date 1 : 20/04/1971     date 2 : 14/09/1913     date 3 : 2/3/1978
    date 4 : 1/7/1986     date 5 : 7/3/47     date 6 : 15/10/1914
    date 7 : 08/03/1941     date 8 : 8/1/1980     date 9 : 30/6/1976"""

Le premier chiffre du jour est soit 0, 1, 2, ou 3 ; ceci se traduit par ``[0-3]``.
Le second chiffre est compris entre 0 et 9, soit ``[0-9]``.
Le format des jours est traduit par ``[0-3][0-9]``. Mais le premier
jour est facultatif, ce qu'on précise avec le symbole ``?`` : ``[0-3]?[0-9]``.
Les mois suivent le même principe : ``[0-1]?[0-9]``. Pour les années,
ce sont les deux premiers chiffres qui sont facultatifs, le symbole ``?`` s'appliquent sur les
deux premiers chiffres, ce qu'on précise avec des parenthèses : ``([0-2][0-9])?[0-9][0-9]``.
Le format final d'une date devient :

::

    [0-3]?[0-9]/[0-1]?[0-9]/([0-2][0-9])?[0-9][0-9]

Le module `re <https://docs.python.org/3/library/re.html?highlight=re#module-re>`_
gère les expressions régulières, celui-ci traite différemment les parties de l'expression
régulière qui sont entre parenthèses de celles qui ne le sont pas : c'est un moyen
de dire au module `re <https://docs.python.org/3/library/re.html?highlight=re#module-re>`_
que nous nous intéressons à telle partie de l'expression qui est signalée
entre parenthèses. Comme la partie qui nous intéresse - une date -
concerne l'intégralité de l'expression régulière, il faut insérer celle-ci entre parenthèses.

La première étape consiste à construire l'expression régulière,
la seconde à rechercher toutes les fois qu'un morceau de la chaîne ``s``
définie plus haut correspond à l'expression régulière.

.. runpython::
    :showcode:

    s = """date 0 : 14/9/2000
        date 1 : 20/04/1971     date 2 : 14/09/1913     date 3 : 2/3/1978
        date 4 : 1/7/1986     date 5 : 7/3/47     date 6 : 15/10/1914
        date 7 : 08/03/1941     date 8 : 8/1/1980     date 9 : 30/6/1976"""

    import re
    # première étape : construction
    expression = re.compile("([0-3]?[0-9]/[0-1]?[0-9]/([0-2][0-9])?[0-9][0-9])")
    # seconde étape : recherche
    res = expression.findall(s)
    print(res)

Le résultat une liste de couples dont chaque élément correspond
aux parties comprises entre parenthèses qu'on appelle des
*groupes*. Lorsque les expressions régulières sont utilisées,
on doit d'abord se demander comment définir ce qu'on cherche puis quelles
fonctions utiliser pour obtenir les résultats de cette recherche.
Les deux paragraphes qui suivent y répondent.

Syntaxe
=======

La syntaxe des expressions régulières est décrite sur le site
officiel de *python*. La page
`Regular Expression Syntax <https://docs.python.org/3/library/re.html?highlight=re#regular-expression-syntax>`_
décrit comment se servir des expressions régulières, les deux pages
sont en anglais. Comme toute grammaire, celle des expressions
régulières est susceptible d'évoluer au fur et à mesure des
versions du langage *python*.

Les ensembles de caractères
---------------------------

Lors d'une recherche, on s'intéresse aux caractères et souvent
aux classes de caractères : on cherche un chiffre, une lettre,
un caractère dans un ensemble précis ou un caractère qui n'appartient
pas à un ensemble précis. Certains ensembles sont prédéfinis,
d'autres doivent être définis à l'aide de crochets.

Pour définir un ensemble de caractères, il faut écrire cet ensemble entre crochets :
``[0123456789]`` désigne un chiffre. Comme c'est une séquence de caractères
consécutifs, on peut résumer cette écriture en ``[0-9]``. Pour inclure les symboles
``-``, ``+``, il suffit d'écrire : ``[-0-9+]``. Il faut penser à mettre
le symbole ``-`` au début pour éviter qu'il ne désigne une séquence.

Le caractère  ``^`` inséré au début du groupe signifie que le caractère
cherché ne doit pas être un de ceux qui suivent. Le tableau suivant décrit
les ensembles prédéfinis et leur équivalent en terme d'ensemble de caractères :

.. list-table::
    :widths: 5 10
    :header-rows: 0

    * - ``.``
      - désigne tout caractère non spécial quel qu'il soit
    * - ``\d``
      - désigne tout chiffre, est équivalent à ``[0-9]``
    * - ``\D``
      - désigne tout caractère différent d'un chiffre, est équivalent à ``[^0-9]``
    * - ``\s``
      - désigne tout espace ou caractère approché, est équivalent à
        ``[\; \t\n\r\f\v]``. Ces caractères sont spéciaux, les plus utilisés sont
        ``\t`` qui est une tabulation, ``\n`` qui est une fin de ligne et qui
        ``\r`` qui est un retour à la ligne.
    * - ``\S``
      - désigne tout caractère différent d'un espace, est équivalent à  ``[^ \t\n\r\f\v]``
    * - ``\w``
      - désigne tout lettre ou chiffre, est équivalent à ``[a-zA-Z0-9\_]``
    * - ``\W``
      - désigne tout caractère différent d'une lettre ou d'un chiffre,
        est équivalent à ``[^a-zA-Z0-9\_]``
    * - ``^``
      - désigne le début d'un mot sauf s'il est placé entre crochets
    * - ``$``
      - désigne la fin d'un mot sauf s'il est placé entre crochets

A l'instar des chaînes de caractères, comme le caractère ``\`` est un
caractère spécial, il faut le doubler : ``[\\]``. Avec ce système, le mot
*"taxinomie"* qui accepte deux orthographes s'écrira : ``tax[io]nomie``.

Le caractère ``\`` est déjà un caractère spécial pour les chaînes de caractères
en *python*, il faut donc le quadrupler pour l'insérer dans un expression
régulière. L'expression suivante filtre toutes les images dont
l'extension est *png* et qui sont enregistrées dans un
répertoire ``image``.

.. runpython::
    :showcode:

    import re
    s = "something\\support\\vba\\image/vbatd1_4.png"
    print(re.compile("[\\\\/]image[\\\\/].*[.]png").search(s))  # résultat positif
    print(re.compile("[\\\\/]image[\\\\/].*[.]png").search(s))  # même résultat

Les multiplicateurs
-------------------

Les multiplicateurs permettent de définir des expressions régulières
comme : un mot entre six et huit lettres qu'on écrira ``[\w]{6,8}``.
Le tableau suivant donne la liste des multiplicateurs principaux :

.. list-table::
    :widths: 5 10
    :header-rows: 0

    * - ``*``
      - présence de l'ensemble de caractères qui précède entre 0 fois et l'infini
    * - ``+``
      - présence de l'ensemble de caractères qui précède entre 1 fois et l'infini
    * - ``?``
      - présence de l'ensemble de caractères qui précède entre 0 et 1 fois
    * - ``{m,n}``
      - présence de l'ensemble de caractères qui précède entre ``m`` et ``n`` fois,
        si ``m=n``, cette expression peut être résumée par ``{n}``.
    * - ``(?!(...))``
      - absence du groupe désigné par les points de suspensions.

L'algorithme des expressions régulières essaye toujours de faire correspondre
le plus grand morceau à l'expression régulière. Par exemple, dans la chaîne
``<h1>mot</h1>``, ``<.*>`` correspond avec ``<h1>``, ``</h1>`` ou encore
``<h1>mot</h1>``. Par conséquent, l'expression régulière correspond à trois
morceaux. Par défaut, il prendra le plus grand. Pour choisir les plus petits,
il faudra écrire les multiplicateurs comme ceci : ``*?``, ``+?``, ``??``.

.. runpython::
    :showcode:

    import re
    s = "<h1>mot</h1>"
    print(re.compile("(<.*>)").match(s).groups())  # ('<h1>mot</h1>',)
    print(re.compile("(<.*?>)").match(s).groups()) # ('<h1>',)

Groupes
-------

Lorsqu'un multiplicateur s'applique sur plus d'un caractère,
il faut définir un groupe à l'aide de parenthèses. Par exemple,
le mot ``yoyo`` s'écrira : ``(yo){2}``. Les parenthèses jouent un
rôle similaire à celui qu'elles jouent dans une expression numérique.
Tout ce qui est compris entre deux parenthèses est considéré
comme un groupe.

Assembler les caractères
------------------------

On peut assembler les groupes de caractères les uns à la suite des
autres. Dans ce cas, il suffit de les juxtaposer comme pour trouver
les mots commençant par ``s`` : ``s[a-z]*``. On peut aussi chercher
une chaîne ou une autre grâce au symbole ``|``. Chercher dans un texte
l'expression *Xavier Dupont* ou *M. Dupont* s'écrira : ``(Xavier)|(M[.]) Dupont``.

Fonctions
---------

La fonction `compile <https://docs.python.org/3/library/re.html?highlight=re#re.compile>`_
du module `re <https://docs.python.org/3/library/re.html?highlight=re#module-re>`_
permet de construire un objet "expression régulière". A partir de cet objet,
on peut vérifier la correspondance entre une expression régulière et une chaîne
de caractères (méthode `match <https://docs.python.org/3/library/re.html?highlight=re#re.match>`_).
On peut chercher une expression régulière
(méthode `search <https://docs.python.org/3/library/re.html?highlight=re#re.search>`_).
On peut aussi remplacer une expression régulière par une chaîne de caractères
(méthode `sub <https://docs.python.org/3/library/re.html?highlight=re#re.sub>`_).

.. list-table::
    :widths: 5 10
    :header-rows: 0

    * - ``match(s[, pos[, end]])``
      - Vérifie la correspondance entre l'expression régulière et la chaîne
        ``s``. Il est possible de n'effectuer cette vérification qu'entre
        les caractères dont les positions sont ``pos`` et ``end``. La fonction retourne
        ``None`` s'il n'y a pas de correspondance et sinon un objet de type ``Match``.
    * - ``search(s[, pos[, end]])``
      - Fonction semblable à ``match``, au lieu de vérifier la correspondance entre
        toute la chaîne et l'expression régulière, cherche la première chaîne
        de caractères extraite correspondant à l'expression régulière.
    * - ``split(s, maxsplit = 0])``
      - Recherche toutes les chaînes de caractères extraites qui vérifient
        l'expression régulière puis découpe cette chaîne en fonction des expressions
        trouvées. La méthode ``split`` d'une chaîne de caractère permet de découper
        selon un séparateur. La méthode ``split`` d'une expression régulière permet de
        découper selon plusieurs séparateurs. C'est pratique pour découper une chaîne
        de caractères en colonnes séparées par ``;`` ou une tabulation.
        ``re.compile("[\t;]").split("a;b\tc;g")`` donne ``["a", "b", "c", "g"]``.
    * - ``findall( 	s[, pos[, end]])``
      - Identique à ``split`` mais ne retourne pas les morceaux entre les chaînes
        extraites qui vérifient l'expression régulière.
    * - ``sub(repl, s, count = 0])``
      - Remplace dans la chaîne ``repl`` les éléments ``\1``, ``\2``, ...
        par les parties de ``s`` qui valident l'expression régulière.
    * - ``flags``
      - Mémorise les options de construction de l'expression régulière. C'est un attribut.
    * - ``pattern`` &
      - Chaîne de caractères associée à l'expression régulière. C'est un attribut.

Ces méthodes et attributs qui s'appliquent à un objet de type "expression régulière"
retourné par la fonction `compile <https://docs.python.org/3/library/re.html?highlight=re#re.compile>`_.
Les méthodes `search <https://docs.python.org/3/library/re.html?highlight=re#re.search>`_
et `match <https://docs.python.org/3/library/re.html?highlight=re#re.match>`_
retournent toutes des objets `Match <https://docs.python.org/3/library/re.html?highlight=re#re.Match>`_ :

.. runpython::
    :showcode:

    s = """date 0 : 14/9/2000
    date 1 : 20/04/1971     date 2 : 14/09/1913     date 3 : 2/3/1978
    date 4 : 1/7/1986     date 5 : 7/3/47     date 6 : 15/10/1914
    date 7 : 08/03/1941     date 8 : 8/1/1980     date 9 : 30/6/1976"""

    import re
    expression = re.compile("([0-3]?[0-9]/[0-1]?[0-9]/([0-2][0-9])?[0-9][0-9])[^\d]")
    print(expression.search(s).group(1,2)) # affiche ('14/9/2000', '20')
    c = expression.search(s).span(1)       # affiche (9, 18)
    print(s[c[0]:c[1]])                    # affiche 14/9/2000

.. list-table::
    :widths: 5 10
    :header-rows: 0

    * - ``group([g1, ...])``
      - Retourne la chaîne de caractères validée par les groupes ``g1``...
    * - ``groups([default])``
      - Retourne la liste des chaînes de caractères qui ont été validées par chacun des groupes.
    * - ``span([gr])``
      - Retourne les positions dans la chaîne originale des chaînes extraites validées le groupe ``gr``.

Ces méthodes qui s'appliquent à un objet de type
`Match <https://docs.python.org/3/library/re.html?highlight=re#re.Match>`_
qui est le résultat des méthodes `search <https://docs.python.org/3/library/re.html?highlight=re#re.search>`_
et `match <https://docs.python.org/3/library/re.html?highlight=re#re.match>`_.
Les groupes sont des sous-parties de l'expression régulière, chacune d'entre elles incluses
entre parenthèses. Le énième correspond au groupe qui suit la énième parenthèse ouvrante.
Le premier groupe a pour indice 1.

Exemple plus complet
--------------------

L'exemple suivant présente trois cas d'utilisation des expressions régulières.
On s'intéresse aux titres de chansons
`MP3 <https://fr.wikipedia.org/wiki/MPEG-1/2_Audio_Layer_III>`_
stockées dans un répertoire.
Le module `mutagen <https://pypi.python.org/pypi/mutagen>`_
permet de récupérer certaines informations concernant un fichier *MP3*
dont le titre, l'auteur et la durée.

Le premier problème consiste à retrouver les chansons sans titre ou dont
le titre contient seulement son numéro : *track03*, *track - 03*, *audiotrack 03*,
*track 03*, *piste 03*, *piste - 03*, *audiopiste 03*, ...
Ce titre indésirable doit valider l'expression régulière suivante :
``^(((audio)?track( )?( - )?[0-9]{1,2})|(piste [0-9]{1,2}))$``.

Le second problème consiste à retrouver toutes les chansons dont le titre contient le
mot *heart* mais ni *heartland* ni *heartache*. Ce titre doit valider
l'expression régulière : ``((heart)(?!((ache)|(land))))``.

Le troisième problème consiste à compter le nombre de mots d'un titre.
Les mots sont séparés par l'ensemble de caractères ``[- ,;!'.?&:]``.
On utilise la méthode ``split`` pour découper en mots.
Le résultat est illustré par le programme suivant.

.. runpython::
    :showcode:

    import os
    import re
    import mutagen.mp3
    import mutagen.easyid3

    def infoMP3 (file, tags) :
        """retourne des informations sur un fichier MP3 sous forme de
        dictionnaire (durée, titre, artiste, ...)"""
        a = mutagen.mp3.MP3(file)
        b = mutagen.easyid3.EasyID3(file)
        info = { "minutes":a.info.length/60, "nom":file }
        for k in tags :
            try:
                info[k] = str(b[k][0])
            except ValueError:
                continue
        return info

    def all_files (repertoire, tags, ext = re.compile (".mp3$")) :
        """retourne les informations pour chaque fichier d'un répertoire"""
        all = []
        for r, d, f in os.walk (repertoire) :
            for a in f :
                if not ext.search (a):
                    continue
                t = infoMP3(r + "/" + a, tags)
                if len(t) > 0:
                    all.append(t)
        return all

    def heart_notitle_mots (all, avoid,sep,heart) :
        """retourne trois résultats
        - les chansons dont le titre valide l'expression régulière heart
        - les chansons dont le titre valide l'expression régulière avoid
        - le nombre moyen de mots dans le titre d'une chanson"""
        liheart, notitle  = [], []
        nbmot, nbsong     = 0,0
        for a in all :
            if "title" not in a :
                notitle.append (a)
                continue
            ti = a ["title"].lower ()
            if avoid.match (ti) :
                notitle.append (a)
                continue
            if heart.search(ti):
                liheart.append (a)
            nbsong += 1
            nbmot  += len ([ m for m in sep.split (ti) if len (m) > 0 ])
        nbsong = max(nbsong, 1)
        return liheart, notitle, float (nbmot)/nbsong

    tags  = "title album artist genre tracknumber".split ()
    all = all_files (r"D:\musique", tags)

    avoid = re.compile("^(((audio)?track( )?( - )?[0-9]{1,2})|(piste [0-9]{1,2}))$")
    sep   = re.compile("[- ,;!'.?&:]")
    heart = re.compile("((heart)(?!((ache)|(land))))")
    liheart, notitle, moymot = heart_notitle_mots (all, avoid, sep, heart)

    print("nombre de mots moyen par titre ", moymot)
    print("somme des durée contenant heart ", sum([s ["minutes"] for s in liheart]))
    print("chanson sans titre ", len (notitle))
    print("liste des titres ")
    for s in liheart:
        print("   ", s["title"])

Groupes nommés
--------------

Une expression régulière ne sert pas seulement de filtre,
elle permet également d'extraire le texte qui correspond à
chaque groupe, à chaque expression entre parenthèses. L'exemple
suivant montre comment récupérer le jour, le mois, l'année à l'intérieur d'une date.

.. runpython::
    :showcode:

    import re
    date = "05/22/2010"
    exp  = "([0-9]{1,2})/([0-9]{1,2})/(((19)|(20))[0-9]{2})"
    com  = re.compile(exp)
    print(com.search(date).groups())    # ('05', '22', '2010', '20', None, '20')

Il n'est pas toujours évident de connaître le numéro du groupe qui
contient l'information à extraire. C'est pourquoi il paraît plus
simple de les nommer afin de les récupérer sous la forme d'un
dictionnaire et non plus sous forme de tableau. La syntaxe
``(?P<nom_du_groupe>expression)`` permet de nommer un groupe.
Elle est appliquée à l'exemple précédent.

.. runpython::
    :showcode:

    import re
    exp  = "(?P<jj>[0-9]{1,2})/(?P<mm>[0-9]{1,2})/(?P<aa>((19)|(20))[0-9]{2})"
    com  = re.compile(exp)
    print(com.search(date).groupdict()) # {'mm': '22', 'aa': '2010', 'jj': '05'}

Le programme suivant est un exemple d'utilisation des expressions régulières
dont l'objectif est de détecter les fonctions définies dans un programme
mais jamais utilisées. Les expressions servent à détecter les définitions
de fonctions (d'après le mot-clé ``def``) puis à détecter les appels.
On recoupe ensuite les informations en cherchant les fonctions définies mais
jamais appelées.

Il n'est pas toujours évident de construire une expression régulière qui
correspondent précisément à tous les cas qu'on veut détecter. Une stratégie
possible est de construire une expression régulière plus permissive
puis d'éliminer les cas indésirables à l'aide d'une seconde expression
régulière, c'est le cas ici pour détecter les appels.

.. runpython::
    :showcode:
    :process:

    """ce programme détermine toutes les fonctions définies dans
    un programme et jamais appelées"""
    import glob
    import os
    import re

    def trouve_toute_fonction (s, exp, gr, expm = "^$") :
        """ à partir d'une chaîne de caractères correspondant
        à un programme Python, cette fonction retourne
        une liste de 3-uples, chacun contient :
            - le nom de la fonction
            - (debut,fin) de l'expression dans la chaîne
            - la ligne où elle a été trouvée

        Paramètres:
           - s    : chaîne de caractères
           - exp  : chaîne de caractères correspond à l'expression
           - gr   : numéro de groupe correspondant au nom de la fonction
           - expm : expression négative
        """
        exp = re.compile(exp)
        res = []
        pos = 0
        r = exp.search (s, pos)   # première recherche
        while r is not None :
            temp = (r.groups()[gr], r.span(gr), r.group(gr))
            x    = re.compile(expm.replace("function", temp[0]))
            if not x.match(temp[2]) :
                # l'expression négative n'est pas trouvé, on peut ajouter ce résultat
                res.append(temp)
            r = exp.search(s, r.end(gr))     # recherche suivante
        return res

    def get_function_list_definition (s) :
        """trouve toutes les définitions de fonctions"""
        return trouve_toute_fonction (s, \
                  "\ndef[ ]+([a-zA-Z_][a-zA-Z_0-9]*)[ ]*[(].*[)][ ]*[:]", 0)

    def get_function_list_call (s) :
        """trouve tous les appels de fonctions"""
        return trouve_toute_fonction (s, \
                  "\n.*[=(,[{ .]([a-zA-Z_][a-zA-Z_0-9]*)(?![ ]?:)[ ]*[(].*[)]?", 0, \
                  "^\\n[ ]*(class|def)[ ]+function.*$")

    def detection_fonction_pas_appelee (file) :
        """retourne les couples de fonctions jamais appelées suivies
        du numéro de la ligne où elles sont définies"""

        f       = open (file, "r")
        li      = f.readlines ()
        f.close ()
        sfile   = "".join (li)

        funcdef = get_function_list_definition (sfile)
        funccal = get_function_list_call (sfile)
        f2 = [ p [0] for p in funccal ]
        res = []
        for f in funcdef :
            if f [0] not in f2 :
                ligne = sfile [:f [1][0]].count ("\n")
                res.append ( (f [0], ligne+2))
        return res

    def fonction_inutile () :  # ligne 63
        pass

    file = __file__
    print(detection_fonction_pas_appelee(file))
