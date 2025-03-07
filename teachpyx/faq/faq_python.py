# coding: utf-8

import io
import os
import re


def entier_grande_taille():
    """

    .. faqref::
        :tag: python
        :title: Quel est l'entier le plus grand ?

        La version 3 du langage Python a supprimé la constante ``sys.maxint``
        qui définissait l'entier le plus grand (voir
        `What's New In Python 3.0
        <https://docs.python.org/3.1/whatsnew/3.0.html#integers>`_).
        De ce fait la fonction
        `getrandbit <https://docs.python.org/3/library/random.html#random.getrandbits>`_
        retourne un entier aussi grand que l'on veut.

        ::

            import random,sys
            x = random.getrandbits(2048)
            print(type(x),x)

        Qui affiche ::

            <class 'int'> 2882159224557107513165483098383814837021447484558010147211921
                          304219017212673656549681269862792029...

        Les calculs en nombre réels se font toujours avec
        huit octets de précision.
        Au delà, il faut utiliser la librairie `gmpy2
        <http://gmpy2.readthedocs.org/en/latest/>`_.
        Il est également recommandé d'utiliser cette
        librairie pour les grands nombres entiers
        (entre 20 et 40 chiffres). La librairie est
        plus rapide que l'implémentation
        du langage Python (voir `Overview of gmpy2
        <https://gmpy2.readthedocs.org/en/latest/overview.html>`_).

    .. faqref::
        :tag: python
        :title: Tabulations ou espace ?

        Il est préférable de ne pas utiliser les tabulations et
        de les remplacer par des espaces.
        Lorsqu'on passe d'un Editeur à un autre, les espaces ne bougent pas.
        Les tabulations sont plus ou moins grandes visuellement.
        L'essentiel est de ne pas mélanger.
        Dans `SciTE <http://www.scintilla.org/SciTE.html>`_,
        il faut aller dans le menu Options / Change Indentation Settings...
        Tous les éditeurs ont une option similaire.
    """


def difference_div():
    """
    .. faqref::
        :tag: python
        :title: Quelle est la différence entre / et // - division ?

        Le résultat de la division avec l'opérateur ``/``
        est toujours réel :
        la division de deux entiers ``1/2`` donne ``0.5``.
        Le résultat de la division avec l'opérateur ``//``
        est toujours entier.
        Il correspond au quotient de la division.

        .. runpython::
            :showcode:

            div1 = 1/2
            div2 = 4/2
            div3 = 1//2
            div4 = 1.0//2.0
            print(div1, div2, div3, div4) # affiche (0.5, 2.0, 0, 0)

        Le reste d'une division entière est obtenue avec l'opérateur ``%``.

        .. runpython::
            :showcode:

            print( 5 % 2 )  # affiche 1
    """
    div1 = 1 / 2
    div2 = 4 / 2
    div3 = 1 // 2
    div4 = 1.0 // 2.0
    return div1, div2, div3, div4


def python_path():
    """
    .. faqref::
        :tag: python
        :title: Comment éviter sys.path.append... quand on développe un module ?

        Lorsqu'on développe un module,
        on ne veut pas l'installer. On ne veut pas qu'il soit présent
        dans le répertoire ``site-packages`` de la distribution
        de Python car cela introduit deux versions :
        celle qu'on développe et celle qu'on a installer.
        Avant, je faisais cela pour créer un petit
        programme utilisant mon propre module
        (et on en trouve quelque trace dans mon code) :

        ::

            import sys
            sys.path.append("c:/moncode/monmodule/src")
            import monmodule

        Quand je récupère un programme utilisant ce module,
        il me faudrait ajouter
        ces petites lignes à chaque fois et c'est barbant.
        Pour éviter cela, il est possible de dire à
        l'interpréteur Python d'aller chercher
        ailleurs pour trouver des modules en ajoutant le chemin à la
        `variable d'environnement
        <http://fr.wikipedia.org/wiki/Variable_d'environnement>`_
        `PYTHONPATH <https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH>`_.
        Sous Windows :

        ::

            set PYTHON_PATH=%PYTHON_PATH%;c:\\moncode\\monmodule\\src
    """
    return os.environ.get("PYTHON_PATH", "")


def same_variable(a, b):
    """
    Cette fonction dit si les deux objets sont en fait le même objet (True)
    ou non (False) s'ils sont différents
    (même s'ils contiennent la même information).

    :param a: n'importe quel objet
    :param b: n'importe quel objet
    :return: ``True`` ou ``False``

    .. faqref::
        :tag: python
        :title: Qu'est-ce qu'un type immuable ou immutable ?
        :lid: faq-py-immutable

        Une variable de type *immuable* ne peut être modifiée.
        Cela concerne principalement :

        - ``int``, ``float``, ``str``, ``tuple``

        Si une variable est de type *immuable*,
        lorsqu'on effectue une opération,
        on créé implicitement une copie de l'objet.

        Les dictionnaires et les listes sont
        *modifiables* (ou *mutable*). Pour une variable
        de ce type, lorsqu'on écrit ``a = b``, ``a`` et ``b``
        désigne le même objet même
        si ce sont deux noms différentes.
        C'est le même emplacement mémoire
        accessible paur deux moyens (deux identifiants).

        Par exemple ::

            a  = (2,3)
            b  = a
            a += (4,5)
            print( a == b ) # --> False
            print(a,b)      # --> (2, 3, 4, 5) (2, 3)

            a  = [2,3]
            b  = a
            a += [4,5]
            print( a == b ) # --> True
            print(a,b)      # --> [2, 3, 4, 5] [2, 3, 4, 5]

        Dans le premier cas, le type (``tuple``) est _immutable_,
        l'opérateur ``+=`` cache implicitement une copie.
        Dans le second cas, le type (``list``) est _mutable_,
        l'opérateur ``+=`` évite la copie
        car la variable peut être modifiée. Même si ``b=a``
        est exécutée avant l'instruction suivante,
        elle n'a **pas** pour effet de conserver l'état de ``a`` avant
        l'ajout d'élément.
        Un autre exemple ::

            a  = [1, 2]
            b  = a
            a [0] = -1
            print(a)        # --> [-1, 2]
            print(b)        # --> [-1, 2]

        Pour copier une liste, il faut expliciter la demander ::

            a  = [1, 2]
            b  = list(a)
            a [0] = -1
            print(a)        # --> [-1, 2]
            print(b)        # --> [1, 2]

        La page `Immutable Sequence Types
        <https://docs.python.org/3/library/stdtypes.html?highlight=immutable#immutable-sequence-types>`_
        détaille un peu plus le type qui sont *mutable* et ceux qui
        sont *immutable*. Parmi les types standards :

        * **mutable**
            * `bool <https://docs.python.org/3/library/functions.html#bool>`_
            * `int <https://docs.python.org/3/library/functions.html#int>`_,
              `float <https://docs.python.org/3/library/functions.html#float>`_,
              `complex <https://docs.python.org/3/library/functions.html#complex>`_
            * `str <https://docs.python.org/3/library/functions.html#func-str>`_,
              `bytes <https://docs.python.org/3/library/functions.html#bytes>`_
            * `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_
            * `tuple <https://docs.python.org/3/library/functions.html#func-tuple>`_,
              `frozenset <https://docs.python.org/3/library/functions.html#func-frozenset>`_
        * **immutable**, par défaut tous les autres types dont :
            * `list <https://docs.python.org/3/library/functions.html#func-list>`_
            * `dict <https://docs.python.org/3/library/functions.html#func-dict>`_
            * `set <https://docs.python.org/3/library/functions.html#func-set>`_
            * `bytearray <https://docs.python.org/3/library/functions.html#bytearray>`_

        Une instance de classe est mutable. Il est possible de la rendre
        immutable par quelques astuces :

        * `__slots__ <https://docs.python.org/3/reference/datamodel.html?highlight=_slots__#object.__slots__>`_
        * `How to Create Immutable Classes in Python
          <http://www.blog.pythonlibrary.org/2014/01/17/how-to-create-immutable-classes-in-python/>`_
        * `Ways to make a class immutable in Python
          <https://stackoverflow.com/questions/4996815/ways-to-make-a-class-immutable-in-python>`_
        * surcharger des méthodes `__getattr__
          <https://docs.python.org/3/reference/datamodel.html#object.__getattr__>`_,
          `__getattribute__
          <https://docs.python.org/3/reference/datamodel.html#object.__getattribute__>`_,
          `__setattr__
          <https://docs.python.org/3/reference/datamodel.html#object.__setattr__>`_.


        Enfin, pour les objects qui s'imbriquent les uns dans
        les autres, une liste de listes, une classe
        qui incluent des dictionnaires et des listes,
        on distingue une copie simple d'une copie intégrale (**deepcopy**).
        Dans le cas d'une liste de listes, la copie simple
        recopie uniquement la première liste ::

            import copy
            l1 = [ [0,1], [2,3] ]
            l2 = copy.copy(l1)
            l1 [0][0] = '##'
            print(l1, l2)  # --> [['##', 1], [2, 3]] [['##', 1], [2, 3]]

            l1 [0] = [10,10]
            print(l1,l2)   # --> [[10, 10], [2, 3]] [['##', 1], [2, 3]]

        La copie intégrale recopie également les objets inclus ::

            import copy
            l1 = [ [0,1], [2,3] ]
            l2 = copy.deepcopy(l1)
            l1 [0][0] = '##'
            print(l1,l2)   # --> [['##', 1], [2, 3]] [[0, 1], [2, 3]]

        Les deux fonctions s'appliquent à tout object Python :
        `module copy <https://docs.python.org/3/library/copy.html>`_.
    """
    return id(a) == id(b)


def stringio(text):
    """
    Teturns a :class:`io.StringIO` object on a text.

    :param text: any text
    :return: StringIO object

    .. faqref::
        :tag: python
        :title: A quoi sert un ``StringIO`` ?

        La plupart du temps, lorsqu'on récupère des données,
        elles sont sur le disque dur
        de votre ordinateur dans un fichier texte. Lorsqu'on
        souhaite automatiser un processur
        qu'on répète souvent avec ce fichier, on écrit une
        fonction qui prend le nom du fichier en entrée.

        ::

            def processus_quotidien(nom_fichier) :
                # on compte les lignes
                nb = 0
                with open(nom_fichier,"r") as f :
                    for line in f :
                        nb += 1
                return nb

        Et puis un jour, les données ne sont plus dans un fichier
        mais sur Internet.
        Le plus simple dans ce cas est de recopier ces données sur disque
        dur et d'appeler la même fonction.
        Simple. Un autre les données qu'on doit télécharger font plusieurs
        gigaoctets. Tout télécharger prend
        du temps pour finir pour s'apercevoir qu'elles sont corrompues.
        On a perdu plusieurs heures pour rien.
        On aurait bien voulu que la fonction ``processus_quotidien``
        commence à traiter les données
        dès le début du téléchargement.

        Pour cela, on a inventé la notion de **stream** ou **flux**
        qui sert d'interface entre la fonction
        qui traite les données et la source des données.
        Le flux lire les données depuis n'importe quel source
        (fichier, internet, mémoire), la fonction qui les traite
        n'a pas besoin d'en connaître la provenance.

        `StringIO <https://docs.python.org/3/library/io.html#io.StringIO>`_
        est un flux qui considère
        la mémoire comme source de données.

        ::

            def processus_quotidien(data_stream):
                # on compte toujours les lignes
                nb = 0
                for line in data_stream :
                    nb += 1
                return nb

        La fonction ``processus_quotidien``
        fonctionne pour des données en mémoire
        et sur un fichier.

        ::

            fichier = __file__
            f = open(fichier,"r")
            nb = processus_quotidien(f)
            print(nb)

            text = "ligne1\\nligne2"
            st = io.StringIO(text)
            nb = processus_quotidien(st)
            print(nb)
    """
    return io.StringIO(text)


def property_example():
    """

    .. faqref::
        :tag: python
        :title: property

        Une `property
        <https://docs.python.org/3/library/functions.html#property>`_ est
        une écriture qui sert à transformer l'appel d'une méthode de classe
        en un attribut.

        ::

            class ClasseAvecProperty:

                def __init__(self,x,y):
                    self._x, self._y = x,y

                @property
                def x(self):
                    return self._x

                @property
                def y(self):
                    return self._y

                @property
                def norm2(self):
                    return self._y**2 + self._x**2

            c = ClasseAvecProperty(1,2)
            print(c.x)
            print(c.y)

        ``x`` est définit comme une méthode mais elle
        retourne simplement l'attribut
        ``_x``. De cette façon, il est impossible de
        changer ``x`` en écrivant::

            c.x = 5

        Cela déclenche l'erreur::

            Traceback (most recent call last):
              File "faq_python.py", line 455, in <module>
                c.x = 5
            AttributeError: can't set attribute

        On fait cela parce que l'écriture est plus courte et que cela
        évite certaines erreurs.
    """


def enumerate_regex_search(exp, text):
    """
    Cette fonction itère sur les différentes occurences
    d'une expression régulière.

    :param exp: expression régulière
    :param text: text à parser
    :return: itérateur

    .. faqref::
        :tag: python
        :title: Comment itérer sur les résultats d'une expression régulière ?

        On utilise la méthode
        `finditer <https://docs.python.org/3/library/re.html#re.regex.finditer>`_.

        ::

            found = exp.search(text)
            for m in exp.finditer(text):
                # ...
    """
    # found = exp.search(text)
    if isinstance(exp, str):
        exp = re.compile(exp)
    for m in exp.finditer(text):
        yield m


def sortable_class(cl):
    """
    .. faqref::
        :tag: python
        :title: Classe sortable

        Il faut prononcer *sortable* à l'anglaise.
        Comment rendre une classe
        *sortable* ? Pour faire simple, on veut écrire ::

            l = [ o1, o2 ]
            l.sort()

        Où ``o1`` et ``o2`` sont des objets d'une classe
        que vous avez définie ::

            class MaClasse:

                ...

        Pour que cela fonctionne, il suffit juste
        de surcharger l'opérateur ``<`` ou plus exactement
        ``__lt__``. Par exemple ::

            class MaClasse:

                def __lt__(self, autre_instance):
                    if self.jenesaispas < autre.jenesaispas:
                        return True
                    elif self.jenesaispas > autre.jenesaispas:
                        return False:
                    else:
                        if self.jenesaispas2 < autre.jenesaispas2:
                            return True
                        else:
                            return False
    """


class PQPipError(Exception):
    """
    Any exception raised by one of the following function.
    """

    def __init__(self, *args):
        """
        :param args: either a string 3 strings (cmd, out, err)
        """
        if len(args) == 1:
            Exception.__init__(self, args[0])
        else:
            cmd, out, err = args
            mes = f"CMD:\n{cmd}\nOUT:\n{out}\n[piperror]\n{err}"
            Exception.__init__(self, mes)


class Distribution:
    """
    Common interface for old and recent pip packages.
    """

    def __init__(self, dist):
        self.dist = dist

    def __getattr__(self, attr):
        if attr == "key":
            if hasattr(self.__dict__["dist"], "key"):
                return self.__dict__["dist"].key
            return self.__dict__["dist"].canonical_name
        if attr == "dist":
            return self.__dict__["dist"]
        if attr in {
            "_get_metadata",
            "requires",
            "PKG_INFO",
            "project_name",
            "py_version",
            "platform",
            "extras",
        }:
            if hasattr(self.__dict__["dist"], attr):
                return getattr(self.__dict__["dist"], attr)
            try:
                return getattr(self.__dict__["dist"]._dist, attr)
            except AttributeError as e:
                if attr == "project_name":
                    return getattr(self.__dict__["dist"]._dist, "name")  # noqa: B009
                if attr == "py_version":
                    return getattr(self.__dict__["dist"]._dist, "version")  # noqa: B009
                if attr in {"platform", "extras"}:
                    return None
                raise AttributeError(
                    f"Unable to find {attr!r} in {dir(self.__dict__['dist']._dist)} or "
                    f"{dir(self.__dict__['dist'])}."
                ) from e
        try:
            return getattr(self.__dict__["dist"], attr)
        except AttributeError as e:
            raise AttributeError(
                f"Unable to find {attr!r} in {dir(self.__dict__['dist'])}."
            ) from e


def get_installed_distributions(
    local_only=True,
    skip=None,
    include_editables=True,
    editables_only=False,
    user_only=False,
    use_cmd=False,
):
    """
    Directs call to function *get_installed_distributions* from :epkg:`pip`.

    Return a list of installed Distribution objects.

    :param local_only: if True (default), only return installations
        local to the current virtualenv, if in a virtualenv.
    :param skip: argument is an iterable of lower-case project names to
        ignore; defaults to ``pip.compat.stdlib_pkgs`` (if *skip* is None)
    :param editables: if False, don't report editables.
    :param editables_only: if True , only report editables.
    :param user_only: if True , only report installations in the user
        site directory.
    :param use_cmd: if True, use a different process (updated package list)
    :return: list of installed Distribution objects.
    """
    if use_cmd:
        raise NotImplementedError("use_cmd should be False.")
    if skip is None:
        try:
            from pip._internal.utils.compat import stdlib_pkgs

            skip = stdlib_pkgs
        except ImportError:
            pass
    try:
        from pip._internal.metadata import get_default_environment

        return list(
            map(
                Distribution,
                get_default_environment().iter_installed_distributions(
                    local_only=local_only,
                    skip=skip,
                    include_editables=include_editables,
                    editables_only=editables_only,
                    user_only=user_only,
                ),
            )
        )

    except ImportError:
        from pip._internal.utils.misc import get_installed_distributions as getd

        return list(
            map(
                Distribution,
                getd(
                    local_only=local_only,
                    skip=skip,
                    include_editables=include_editables,
                    editables_only=editables_only,
                    user_only=user_only,
                    use_cmd=use_cmd,
                ),
            )
        )


def get_packages_list():
    """
    calls ``pip list`` to retrieve the list of packages
    """
    return get_installed_distributions(local_only=True)


def list_of_installed_packages():
    """
    calls ``pip list`` to retrieve the list of packages

    .. faqref::
        :tag: python
        :title: Obtenir des informations sur les packages installés

        Le module :epkg:`pip` retourne des informations
        sur n'importe quel module installé, sa version,
        sa license ::

            pip show pandas

        On peut également l'obtenir depuis l'interpréteur python ::

            import pip
            pip.main(["show", "pandas"])

        Exemple ::

            Name: pandas
            Version: 0.16.0
            Summary: Powerful data structures for data analysis,
            time series,and statistics
            Home-page: http://pandas.pydata.org
            Author: The PyData Development Team
            Author-email: pydata@googlegroups.com
            License: BSD
            Location: c:\\python35_x64\\lib\\site-packages
            Requires: python-dateutil, pytz, numpy

        On utilise également ``pip freeze`` pour répliquer l'environnement
        dans lequel on a développé un programme.
        `pip freeze <https://pip.pypa.io/en/latest/reference/pip_freeze.html>`_
        produit la liste des modules avec la version utilisée ::

            docutils==0.11
            Jinja2==2.7.2
            MarkupSafe==0.19
            Pygments==1.6
            Sphinx==1.2.2

        Ce qu'on utilise pour répliquer l'environnement
        de la manière suivante ::

            pip freeze > requirements.txt
            pip install -r requirements.txt

        Cette façon de faire fonctionne très bien sous
        Linux mais n'est pas encore
        opérationnelle sous Windows à moins d'installer
        le compilateur
        C++ utilisée pour compiler
        Python.
    """
    return get_packages_list()


def get_package_info(name=None, start=0, end=-1):
    """
    Calls ``pip show`` to retrieve information about packages.

    :param name: name of he packages or None to get all of them in a list
    :param start: start at package n (in list return by :func:`get_packages_list`)
    :param end: end at package n, -1 for all
    :return: dictionary or list of dictionaries
    """
    from pip._internal.commands.show import search_packages_info

    if name is None:
        res = []
        packs = get_packages_list()
        if end == -1:
            end = len(packs)
        subp = packs[start:end]
        if len(subp) == 0:
            raise PQPipError(
                "No package, start={0}, end={1}, len(subp)={2}, len(packs)={3}".format(
                    start, end, len(subp), len(packs)
                )
            )
        for cp in subp:
            pack = cp.project_name
            info = get_package_info(pack)
            res.append(info)
        if len(res) == 0 and len(subp) > 0:
            raise PQPipError(
                f"Empty list, unexpected, start={start}, "
                f"end={end}, len(subp)={len(subp)}"
            )
        return res

    res = list(search_packages_info([name]))
    if len(res) != 1:
        raise PQPipError(f"Unexpected number of results {len(res)} for {name}")
    return res[0]


def information_about_package(name):
    """
    Calls ``pip show`` to retrieve information about packages.

    .. faqref::
        :tag: python
        :title: Récupérer la liste des modules installés

        Le module :epkg:`pip` permet d'installer
        de nouveaux modules mais aussi d'obtenir la liste
        des packages installés ::

            pip list

        On peut également l'obtenir depuis l'interpréteur python ::

            import pip
            pip.main(["list"])

    .. faqref::
        :tag: python
        :title: Pourquoi l'installation de pandas (ou numpy)
            ne marche pas sous Windows avec pip ?

        Python est un langage très lent et c'est pourquoi la
        plupart des modules de calculs numériques
        incluent des parties implémentées en langage C++.
        :epkg:`numpy`, :epkg:`pandas`, :epkg:`matplotlib`,
        :epkg:`scipy`, :epkg:`scikit-learn`, ...
        ...

        Sous Linux, le compilateur est intégré au système et
        l'installation de ces modules via
        l'instruction ``pip install <module>`` met implicitement
        le compilateur à contribution.
        Sous Windows, il n'existe pas de compilateur C++ par
        défaut à moins de l'installer.
        Il faut faire attention alors d'utiliser exactement le même que celui utilisé
        pour compiler Python (voir
        `Compiling Python on Windows
        <https://docs.python.org/3/using/windows.html#compiling-python-on-windows>`_).

        C'est pour cela qu'on préfère utiliser des distributions comme
        `Anaconda <https://www.anaconda.com/>`_
        qui propose par défaut
        une version de Python accompagnée des modules les plus utilisés.
        Elle propose également une façon
        simple d'installer des modules précompilés avec l'instruction ::

            conda install <module_compile>
    """
    return get_package_info(name)


def get_month_name(date):
    """
    returns the month name for a give date

    :param date: datatime
    :return: month name

    .. faqref::
        :tag: python
        :title: Récupérer le nom du mois à partir d'une date

        .. runpython::
            :showcode:

            import datetime
            dt = datetime.datetime(2016, 1, 1)
            print(dt.strftime("%B"))
    """
    return date.strftime("%B")


def get_day_name(date):
    """
    returns the day name for a give date

    :param date: datatime
    :return: month name

    .. faqref::
        :tag: python
        :title: Récupérer le nom du jour à partir d'une date

        .. runpython::
            :showcode:

            import datetime
            dt = datetime.datetime(2016, 1, 1)
            print(dt.strftime("%A"))
    """
    return date.strftime("%A")


def class_getitem():
    """
    This function shows how to enable an expression such as
    `A[1]` where `A` is a class type and not an instance.
    This can be done through `__class_getitem__
    <https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__>`_.
    """

    class A:
        def __init__(self):
            pass

        @classmethod
        def get(cls, index):
            if index == 1:
                return A1
            if index == 2:
                return A2
            raise AssertionError(f"Unexpected index={index}")

        @classmethod
        def __class_getitem__(cls, index):
            return cls.get(index)

        def __getitem__(self, index):
            return "i[%d]" % index

    class A1(A):
        def __init__(self):
            A.__init__(self)

    class A2(A):
        def __init__(self):
            A.__init__(self)

    a = A()
    assert a[5] == "i[5]"
    assert a.__class__.__name__ == "A"

    a = A.get(1)()
    assert a.__class__.__name__ == "A1"

    a = A[1]()
    assert a.__class__.__name__ == "A1"

    a = A[2]()
    assert a.__class__.__name__ == "A2"
