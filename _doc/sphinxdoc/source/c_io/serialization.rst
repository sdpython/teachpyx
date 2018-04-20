
.. _chap_serialization:

=============
Sérialisation
=============

.. index:: sérialisation

La `sérialisation <https://fr.wikipedia.org/wiki/S%C3%A9rialisation>`_ est
un besoin fréquent depuis l'avènement d'internet. Une appplication
web est souvent un assemblage de services indépendant qui s'échangent des
informations complexes. Un service doit transmettre des données
à un autre. L'opération est simple lorsqu'il s'agit de transmettre
un nombre réel, un entier, une chaîne de caractère. C'est déjà
un peu plus compliqué lorsque les données à transmettre sont
constituées de listes et de dictionnaires. Elle est complexe
lorsque ce sont des instances de classes définies par le programme
lui-même. Or les services s'échangent uniquement des octets
(ou *byte* en anglais). Il faut donc convertir des informations
complexes en une séquence d'octets puis effectuer la conversion
inverse. Ces opérations sont regroupées sous le terme
de *sérialisation*.

.. contents::
    :local:
    :depth: 2

JSON
====

Un des premiers utilisés dans le monde internet est le format
`XML <https://fr.wikipedia.org/wiki/Extensible_Markup_Language>`_.
Le langage `HTML <https://fr.wikipedia.org/wiki/Hypertext_Markup_Language>`_
suit la même logique que le format *XML*.
Il peut représenter un assemblage de liste et de dictionnaires
qui contiennent des nombres et des chaînes de caractères.

::

    <xml>
        <personne>                          <!-- dictionnaire -->
            <nom>Dupré</nom>                <!-- str -->
            <prenom>Xavier</prenom>         <!-- str -->
            <langages>                      <!-- liste -->
                <lang>                      <!-- dictionnaire -->
                    <nom>C++</nom>          <!-- str -->
                    <vitesse>rapide</nom>   <!-- str -->
                    <age>40</age>           <!-- int -->
                </lang>
                <lang>                      <!-- dictionnaire -->
                    <nom>python</nom>       <!-- str -->
                    <vitesse>lente</nom>    <!-- str -->
                    <age>20</age>           <!-- int -->
                </lang>
            </langages>
        </personnes>
    </xml>

La sérialisation passe par une étape intermédiaire qui revient à
convertir tout type de variables en une séquence de listes et
de dictionnaires puis à la convertir sous la forme d'une séquence d'octets.

.. blockdiag::

    blockdiag {
       A [label = "variables"];
       B [label = "dictionnaires, listes"];
       C [label = "séquence d'octets"];
       A -> B -> C;
    }

Le format `XML <https://fr.wikipedia.org/wiki/Extensible_Markup_Language>`_
intervient lors de la seconde étape. Il est assez *verbeux*. La séquence
d'octets ou plutôt de caractères qu'il produit est assez longue même une fois
les espaces enlevés. On lui préfère le format :epkg:`JSON`
qui est très utilisé pour communiquer entre les services via
des `API REST <https://fr.wikipedia.org/wiki/Representational_state_transfer>`_
car il est à la fois concis et lisible.

.. runpython::
    :showcode:

    from json import dump
    from io import StringIO

    data = {'records': [{'nom': 'Xavier', 'prénom': 'Xavier',
                         'langages':[{'nom':'C++', 'age':40},
                                     {'nom':'Python', 'age': 20}]}]}

    buffer = StringIO()
    res = dump(data, buffer)
    seq = buffer.getvalue()
    print(seq)

Le format :epkg:`JSON` est très proche de la syntaxe du langage :epkg:`Python`.
Le résultat apparaît sous la forme d'une chaîne de caractère et est
facile à transmettre à n'importe quelle autre application.
La conversion inverse s'effectue comme suit.

.. runpython::
    :showcode:

    from json import load
    from io import StringIO

    seq = '{"records": [{"nom": "Xavier", "pr\\u00e9nom": "Xavier", ' + \
          '"langages": [{"nom": "C++", "age": 40}, {"nom": "Python", "age": 20}]}]}'

    buffer = StringIO(seq)
    read = load(buffer)
    read

Tous les types ne sont pas sérialisables même si ceux-ci
sont fréquemment utilisés :

.. runpython::
    :showcode:

    from json import dump
    from io import StringIO
    import numpy

    data = {'mat': numpy.array([0, 1])}

    buffer = StringIO()
    try:
        dump(data, buffer)
    except Exception as e:
        print(e)

Les classes définies dans le programme ne sont pas non
plus sérialisables par défaut.

.. runpython::
    :showcode:

    from json import dump, JSONEncoder
    from io import StringIO

    class A:
        def __init__(self, att):
            self.att = att

    class MyEncoder(JSONEncoder):
            def default(self, o):
                return {'classname': o.__class__.__name__, 'data': o.__dict__}

    data = A('e')
    buffer = StringIO()
    try:
        dump(data, buffer, cls=MyEncoder)
    except Exception as e:
        print(e)

On peut néanmoins contourner l'obstacle en indiquant à la fonction
`dump <https://docs.python.org/3/library/json.html#json.dump>`_
comment convertir l'instance en un assemblage de listes et de dictionnaires
avec la classe `JSONEncoder <https://docs.python.org/3/library/json.html#json.JSONEncoder>`_.

.. runpython::
    :showcode:

    from json import dump, JSONEncoder
    from io import StringIO

    class A:
        def __init__(self, att):
            self.att = att

    class MyEncoder(JSONEncoder):
            def default(self, o):
                return {'classname': o.__class__.__name__, 'data': o.__dict__}

    data = A('e')
    buffer = StringIO()
    res = dump(data, buffer, cls=MyEncoder)
    res = buffer.getvalue()
    res

Et la relecture s'effectue comme suit :

.. runpython::
    :showcode:

    from json import load, JSONDecoder
    from io import StringIO

    class MyDecoder(JSONDecoder):
            def decode(self, o):
                dec = JSONDecoder.decode(self, o)
                if isinstance(dec, dict) and dec.get('classname') == 'A':
                    return A(dec['data']['att'])
                else:
                    return dec

    res = '{"classname": "A", "data": {"att": "e"}}'
    buffer = StringIO(res)
    obj = load(buffer, cls=MyDecoder)
    obj

Il existe des alternatives plus rapides au module
`json <https://docs.python.org/3/library/json.html>`_
come le module :epkg:`ultrajson`.

Binaire
=======

Le format *binaire* n'est pas un format à proprement parler.
Le problème principale lié à l'utilisation d'un format comme
:epkg:`JSON` est le temps passé à convertir les informations
numériques en texte et réciproquement. Il est plus efficace
de conserver cette information dans un format plus proche de
celui de la mémoire. Cette remarque est aussi vrai pour tous
les autre types. Lorsque la sérialisation est nécessaire au
sein d'une même application, il est nettement préférable de
choisir ce type de format même s'il est illisible pour un autre
langage voire même pour un autre programme. Le code ressemble
beaucoup à ce qui a été écrit pour le format :epkg:`JSON`.

.. runpython::
    :showcode:

    from pickle import dump
    from io import BytesIO

    data = {'records': [{'nom': 'Xavier', 'prénom': 'Xavier',
                         'langages':[{'nom':'C++', 'age':40},
                                     {'nom':'Python', 'age': 20}]}]}

    buffer = BytesIO()
    res = dump(data, buffer)
    seq = buffer.getvalue()
    print(seq)

La relecture s'effectue tout aussi simplement.

.. runpython::
    :showcode:

    from pickle import load, dump
    from io import BytesIO

    data = {'records': [{'nom': 'Xavier', 'prénom': 'Xavier',
                         'langages':[{'nom':'C++', 'age':40},
                                     {'nom':'Python', 'age': 20}]}]}

    # écriture
    buffer = BytesIO()
    res = dump(data, buffer)
    seq = buffer.getvalue()

    # lecture
    buffer = BytesIO(seq)
    read = load(buffer)
    print(read)

Certaines configurations impossible, un peu comme pour
le format :epkg:`JSON`, de modifier les éléments sérialisés
et restaurés. Cela se fait grâce aux fonctions
`__getstate__ <https://docs.python.org/3/library/pickle.html#object.__getstate__>`_ et
`__setstate__ <https://docs.python.org/3/library/pickle.html#object.__setstate__>`_.
Dans l'exemple suivant, la classe copie un attribut deux fois.
Pour réduire la taille de l'objet une fois sérialisé, on en stocke qu'un seul.

.. runpython::
    :showcode:

    from io import BytesIO
    from pickle import dump, load

    class B:
        def __init__(self, att):
            self.att1 = att
            self.att2 = att

        def __getstate__(self):
            # On indique les attributs à converser.
            return dict(att=self.att1)

        def __setstate__(self, state):
            # On restaure l'objet à partir de ce qui a été sérialisé.
            setattr(self, 'att1', state["att"])
            setattr(self, 'att2', state["att"])

        data = B('r')
        buffer = BytesIO()
        res = dump(data, buffer)
        seq = buffer.getvalue()

        buffer = BytesIO(seq)
        read = load(buffer)
        print(read.att1, read.att2)

Optimisation
============

.. index:: protobuf

La communication entre services devient parfois cruciale
pour assurer un service temps réel. Le premier enjeu est
d'écrire ou de lire rapidement. Le second est de pouvoir
accéder à une information sans avoir à déchiffrer l'ensemble
des données sérialisées. Pour ces deux objectifs, la solution
la plus aboutie est la librarie :epkg:`protobuf`. L'efficacité
est gagnée en imposant un format strict et figé aux données.
La première étape consiste à définir un schéma de donnée,
qui est convertit ensuite en un programme qui permette de
sérialiser, désérialiser et accéder à une information précise
dans le language de votre choix.

.. blockdiag::

    blockdiag {
       A [label = "schéma"];
       B [label = "code python"];
       A -> B [label = "compilation"];
    }

La suite est dans le notebook :

.. toctree::
    :maxdepth:

    ../notebooks/serialisation_protobuf

Sérialiser autre chose que des données
======================================

D'une manière générale, il vaut mieux éviter de sérialiser
les fonctions, itérateurs ou générateurs. Il est souvent impossible
des les sérialiser proprement sans ajouter du code spécifiquement
développés pour cela. Le notebook suivant étudie certains cas
où cela est néanmoins possible sans trop de développement.

.. toctree::
    :maxdepth:

    ../notebooks/serialisation_examples
