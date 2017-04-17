
.. _l-files:

.. _chap_fichier:

==========
Fichiers
==========

.. contents::
    :local:
    :depth: 2

.. index:: fichier

Lorsqu'un programme termine son exécution, toutes les informations stockées
dans des variables sont perdues. Un moyen de les conserver est de les
enregistrer dans un fichier sur disque dur. A l'intérieur de celui-ci,
ces informations peuvent apparaître sous un format texte qui est lisible
par n'importe quel éditeur de texte, dans un format compressé, ou sous
un autre format connu par le concepteur du programme. On appelle ce dernier
type un `format binaire <https://fr.wikipedia.org/wiki/Fichier_binaire>`_,
il est adéquat lorsque les données à conserver
sont très nombreuses ou lorsqu'on désire que celles-ci ne puissent
pas être lues par une autre application que le programme lui-même. En
d'autres termes, le format binaire est illisible excepté pour celui qui l'a conçu.

Ce chapitre abordera pour commencer les formats texte, binaire et
compressé (*zip*) directement manipulable depuis *python*.
Les manipulations de fichiers suivront pour terminer sur les
expressions régulières qui sont très utilisées pour effectuer
des recherches textuelles. A l'issue de ce chapitre, on peut envisager
la recherche à l'intérieur de tous les documents textes présents sur
l'ordinateur, de dates particulières, de tous les numéros de téléphones
commençant par 06... En utilisant des modules tels que
`reportlab <https://pypi.python.org/pypi/reportlab>`_
ou encore `openpyxl <https://pypi.python.org/pypi/openpyxl>`_,
il serait possible d'étendre cette fonctionnalité aux fichiers de type
`pdf <https://fr.wikipedia.org/wiki/Portable_Document_Format>`_
et aux fichiers `Excel <https://fr.wikipedia.org/wiki/Microsoft_Excel>`_.

Format texte
============

.. index:: format texte

Les `fichiers texte <https://fr.wikipedia.org/wiki/Fichier_texte>`_ sont les plus
simples : ce sont des suites de caractères. Le format
`HTML <https://fr.wikipedia.org/wiki/Hypertext_Markup_Language>`_ et
`XML <https://fr.wikipedia.org/wiki/Extensible_Markup_Language>`_ font partie de
cette catégorie. Ils servent autant à conserver des informations qu'à en
échanger comme par exemple transmettre une matrice à
`Excel <https://fr.wikipedia.org/wiki/Microsoft_Excel>`_.

Ce format, même s'il est simple, implique une certaine organisation dans la
façon de conserver les données afin de pouvoir les récupérer. Le cas le
plus fréquent est l'enregistrement d'une matrice : on choisira d'écrire les
nombres les uns à la suite des autres en choisissant un séparateur de
colonnes et un séparateur de lignes. Ce point sera abordé à la fin de cette section.
Les fichiers texte que les programmes informatiques manipulent sont souvent structurées.

Ecriture
--------

La première étape est l'écriture. Les informations sont toujours écrites
sous forme de chaînes de caractères et toujours ajoutées à la fin du
fichier qui s'allonge jusqu'à ce que toutes les informations y
soient écrites. L'écriture s'effectue toujours selon le même schéma.

1. création ou ouverture du fichier,
2. écriture,
3. fermeture.

Lors de l'ouverture, le fichier dans lequel seront écrites les
informations est créé s'il n'existe pas ou nettoyé s'il existe déjà.
La fermeture permet à d'autres programmes de lire ce que vous
avez placé dans ce fichier. Sans cette dernière étape, il sera
impossible d'y accéder à nouveau pour le lire ou y écrire à nouveau.
A l'intérieur d'un programme informatique, écrire dans un
fichier suit toujours le même schéma :

::

    f = open ("nom-fichier", "w")    # ouverture

    f.write ( s )    # écriture de la chaîne de caractères  s
    f.write ( s2 )   # écriture de la chaîne de caractères  s2
    ...

    f.close ()  # fermeture

.. index:: ressource

Les étapes d'ouverture et de fermeture sont toujours présentes en ce qui
concerne les fichiers. Il s'agit d'indiquer au système d'exploitation que
le programme souhaite accéder à un fichier et interdire à tout autre programme
l'accès à ce fichier. Un autre programme qui souhaiterait créer un fichier du
même nom ne le pourrait pas tant que l'étape de fermeture n'est pas exécutée.
En revanche, il pourrait tout à fait le lire car la lecture ne perturbe pas l'écriture.

Il faut donc toujours fermer le fichier à la fin pour indiquer que le fichier
est accessible pour un autre usage. Un fichier est une
`ressource <https://fr.wikipedia.org/wiki/Ressource_(informatique)>`_.
Et comme ce schéma se répète toujours, le langage *Python* a prévu une syntaxe
avec le mot-clé `with <https://docs.python.org/3/reference/compound_stmts.html#the-with-statement>`_.

::

    with open ("nom-fichier", "w") as f:    # ouverture

        f.write ( s )    # écriture de la chaîne de caractères  s
        f.write ( s2 )   # écriture de la chaîne de caractères  s2
        ...

L'instruction ``f.close()`` est implicite et automatiquement exécutée
dès que le programme sort de la section *with*.
Lorsque que le programme se termine, même s'il reste des fichiers "ouverts"
pour lesquels la méthode ``close`` n'a pas été appelée, ils seront automatiquement fermés.

Certains caractères sont fort utiles lors de l'écriture de fichiers texte
afin d'organiser les données. Le symbole ``;`` est très utilisé comme
séparateur de colonnes pour une matrice, on utilise également le
passage à la ligne ou la tabulation. Comme ce ne sont pas des
caractères "visibles", ils ont des codes :

* ``\n`` : passage à la ligne
* ``\t`` : tabulation, indique un passage à la colonne suivante dans
  le format `tsv <https://fr.wikipedia.org/wiki/Tabulation-separated_values>`_
  (Tabulation-separated values).

Il existe peu de manières différentes de conserver une matrice dans un
fichier, le programme ressemble dans presque tous les cas à celui qui suit :

::

    mat =  ... # matrice de type liste de listes
    f = open ("mat.txt", "w")
    for i in range (0,len (mat)) :                # la fonction join est aussi
        for j in range (0, len (mat [i])) :       # fréquemment utilisée
            f.write ( str (mat [i][j]) + "\t")    # pour assembler les chaînes
        f.write ("\n")                            # un une seule et réduire le
    f.close ()                                    # nombre d'appels à f.write

Ou encore :

::

    mat =  ... # matrice de type liste de listes
    with open ("mat.txt", "w") as f:
        for i in range (0,len (mat)) :
            for j in range (0, len (mat [i])) :
                f.write ( str (mat [i][j]) + "\t")
            f.write ("\n")

La fonction `open <https://docs.python.org/3/library/functions.html?highlight=open#open>`_
accepte deux paramètres, le premier est le nom du fichier,
le second définit le mode d'ouverture : ``"w"`` pour écrire (**w**rite),
"a" pour écrire et ajouter (**a**ppend),
"r" pour lire (**r**ead). Ceci signifie que la fonction ``open``
sert à ouvrir un fichier quelque soit l'utilisation qu'on en fait.

A la première écriture dans un fichier (premier appel à la fonction ``write``,
la taille du fichier créée est souvent nulle. L'écriture dans un fichier
n'est pas immédiate, le langage *python* attend d'avoir reçu beaucoup
d'informations avant de les écrire physiquement sur le disque dur.
Les informations sont placées dans un tampon ou `buffer <https://en.wikipedia.org/wiki/Data_buffer>`_.
Lorsque le tampon est plein, il est écrit sur disque dur. Pour éviter ce délai,
il faut soit fermer puis réouvrir le fichier soit appeler la méthode
`flush <https://docs.python.org/3.6/library/io.html#io.IOBase.flush>`_
qui ne prend aucun paramètre. Ce mécanisme vise à réduire le nombre
d'accès au disque dur car selon les technologies,
il n'est pas nécessairement beaucoup plus long d'y écrire un caractère
plutôt que 1000 en une fois.

Ecriture en mode "ajout"
------------------------

Lorsqu'on écrit des informations dans un fichier, deux cas se présentent.
Le premier consiste à ne pas tenir compte du précédent contenu de ce fichier
lors de son ouverture pour écriture et à l'écraser. C'est le cas traité par
le précédent paragraphe. Le second cas consiste à ajouter toute nouvelle
information à celles déjà présentes lors de l'ouverture du fichier. Ce second
cas est presque identique au suivant hormis la première ligne qui change :

::

    with open ("nom-fichier", "a") as f:    # ouverture en mode ajout, mode "a"
        ...

Pour comprendre la différence entre ces deux modes d'ouverture,
voici deux programmes. Celui de gauche n'utilise pas le mode ajout tandis
que celui de droite l'utilise lors de la seconde ouverture.

*Premier programme*

::

    with open ("essai.txt", "w") as f:
        f.write (" premiere fois ")
        f.close ()

    with f = open ("essai.txt", "w") as f:
        f.write (" seconde fois ")
        f.close ()

*Second programme*

::

    with open ("essai.txt", "w") as f:
        f.write (" premiere fois ")
        f.close ()

    with f = open ("essai.txt", "a") as f:  ###
        f.write (" seconde fois ")
        f.close ()

Le premier programme crée un fichier ``"essai.txt"`` qui ne contient que les
informations écrites lors de la seconde phase d'écriture, soit
``seconde fois``. Le second utilise le mode ajout lors de la seconde
ouverture. Le fichier ``"essai.txt"``, même s'il existait avant l'exécution
de ce programme, est effacé puis rempli avec l'information ``premiere fois``.
Lors de la seconde ouverture, en mode ajout, une seconde chaîne de caractères
est ajoutée. le fichier ``"essai.txt"``, après l'exécution du programme
contient donc le message : ``premiere fois seconde fois``.

Un des moyens pour comprendre ou suivre l'évolution d'un programme est d'écrire
des informations dans un fichier ouvert en mode ajout qui est ouvert et
fermé sans cesse. Ce sont des fichiers de *traces* ou de
`log <https://fr.wikipedia.org/wiki/Historique_(informatique)>`_.
Ils sont souvent utilisés pour vérifier des calculs complexes. Ils permettent
par exemple de comparer deux versions différentes d'un programme pour
trouver à quel endroit ils commencent à diverger.

Lecture
-------

La lecture d'un fichier permet de retrouver les informations stockées
grâce à une étape préalable d'écriture. Elle se déroule selon le même principe, à savoir :

1. ouverture du fichier en mode lecture,
2. lecture,
3. fermeture.

Une différence apparaît cependant lors de la lecture d'un fichier :
celle-ci s'effectue ligne par ligne alors que l'écriture ne suit
pas forcément un découpage en ligne. Les instructions à écrire
pour lire un fichier diffèrent rarement du schéma qui suit où seule
la ligne indiquée par ``(*)`` change en fonction ce qu'il
faut faire avec les informations lues.

::

    with f = open ("essai.txt", "r") as f:  # ouverture du fichier en mode lecture
        for ligne in f :             # pour toutes les lignes du fichier
            print ligne              # on affiche la ligne (*)
        # f.close ()                 # on ferme le fichier, ce qui est implicite avec with

Pour des fichiers qui ne sont pas trop gros (< 100000 lignes),
il est possible d'utiliser la méthode
`readlines <https://docs.python.org/3/library/io.html?highlight=readlines#io.IOBase.readlines>`_
qui récupère toutes les
lignes d'un fichier texte en une seule fois. Le programme suivant donne
le même résultat que le précédent.

::

    with open ("essai.txt", "r") as f: # ouverture du fichier en mode lecture
        l = f.readlines ()             # lecture de toutes les lignes, placées dans une liste

    for s in l:
        print(s)                       # on affiche les lignes à l'écran (*)

Lorsque le programme précédent lit une ligne dans un fichier,
le résultat lu inclut le ou les caractères (``\n``, ``\r`` - sous Windows seulement)
qui marquent la fin
d'une ligne. C'est pour cela que la lecture est parfois suivie d'une
étape de nettoyage.

::

    with open ("essai.txt", "r") as f: # ouverture du fichier en mode lecture
        l = f.readlines ()             # lecture de toutes les lignes, placées dans une liste

    # contiendra la liste des lignes nettoyées
    l_net = [ s.strip ("\n\r") for s in l ]

Les informations peuvent être structurées de façon plus élaborée dans un fichier texte,
c'est le cas des formats `HTML <https://fr.wikipedia.org/wiki/Hypertext_Markup_Language>`_ et
`XML <https://fr.wikipedia.org/wiki/Extensible_Markup_Language>`_.
Pour ce type de format plus complexe, il est déconseillé de concevoir soi-même
un programme capable de les lire, il existe presque toujours un module qui permette
de le faire. C'est le cas du module
`html.parser <https://docs.python.org/3/library/html.parser.html>`_
ou `xml <https://docs.python.org/3/library/xml.html?highlight=xml#module-xml>`_.
De plus, les modules sont régulièrement mis à jour et suivent l'évolution des
formats qu'ils décryptent.

Un fichier texte est le moyen le plus simple d'échanger des matrices ou des données avec un
tableur et il n'est pas besoin de modules dans ce cas. Lorsqu'on enregistre
une feuille de calcul sous format texte, le fichier obtenu est organisé en colonnes :
sur une même ligne, les informations sont disposées en colonne délimitées par
un séparateur qui est souvent une tabulation (``\t``) ou un point virgule
comme dans l'exemple suivant :

::

    nom  ; prénom ; livre
    Hugo  ; Victor  ; Les misérables
    Kessel ; Joseph  ; Le lion
    Woolf ; Virginia  ; Mrs Dalloway
    Calvino ; Italo  ; Le baron perché

Pour lire ce fichier, il est nécessaire de scinder chaque ligne en
une liste de chaînes de caractères, on utilise pour cela la méthode
`split <https://docs.python.org/3/library/stdtypes.html?highlight=split#str.split>`_
des chaînes de caractères.

::

    mat = []                            # création d'une liste vide,
    with open ("essai.txt", "r") as f:  # ouverture du fichier en mode lecture
        for li in f :                   # pour toutes les lignes du fichier
            s = li.strip ("\n\r")       # on enlève les caractères de fin de ligne
            l = s.split (";")           # on découpe en colonnes
            mat.append (l)              # on ajoute la ligne à la matrice

Ce format de fichier texte est appelé
`CSV <https://fr.wikipedia.org/wiki/Comma-separated_values>`_ (Comma Separated Value),
il peut être relu depuis un programme *python* comme le montre l'exemple précédent,
par *Excel* en précisant que le format du fichier est le format *CSV* et par
toutes les applications ou langages traitant de données. Pour les valeurs numériques,
il ne faut pas oublier de convertir en caractères lors de l'écriture et
de convertir en nombres lors de la lecture.

Les nombres réels s'écrivent en anglais avec un point pour séparer la partie
entière de la partie décimale. En français, il s'agit d'une virgule. Il est
possible que, lors de la conversion d'une matrice, il faille remplacer
les points par des virgules et réciproquement pour éviter les problèmes de conversion.

Encoding et les accents
-----------------------

.. index:: encoding

Par défaut, un fichier n'accepte pas d'enregistrer des accents, uniquement
les acaractères `ascii <https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange>`_.
C'est pourquoi il faut presque tout le temps utiliser le paramètre *encoding*
de la fonction `open <https://docs.python.org/3/library/functions.html?highlight=open#open>`_
que ce soit pour écrire ou lire.

::

    with open("fichier.txt", "r", encoding="utf-8") as f:
        texte = f.read()

L'encoding *utf-8* est une façon de représenter les caractères, les caractères ascii sur
un octet, les autres sur deux ou trois octets. Cet encoding est le plus fréquent sur internet.

Fichiers zip
============

Les fichiers `zip <https://fr.wikipedia.org/wiki/ZIP_(format_de_fichier)>`_
sont très répandus de nos jours et constituent un standard de compression
facile d'accès quelque soit l'ordinateur et son système d'exploitation.
Le langage *python* propose quelques fonctions pour compresser et décompresser
ces fichiers par l'intermédiaire du module
`zipfile <https://docs.python.org/3/library/zipfile.html>`_.
Le format de compression *zip* est un des plus répandus bien qu'il ne soit pas
le plus performant. D'autres formats proposent de meilleurs taux de compression
sur les fichiers textes existent comme `7-zip <http://www.7-zip.org/>`_.
Ce format n'est pas seulement utilisé pour compresser mais aussi comme
un moyen de regrouper plusieurs fichiers en un seul.

Lecture
-------

L'exemple suivant permet par exemple d'obtenir la liste des fichiers
inclus dans un fichier *zip* :

::

    import zipfile
    with zipfile.ZipFile ("exemplezip.zip", "r") as fz:
        for info in fz.infolist () :
            print(info.filename, info.date_time, info.file_size)

Les fichiers compressés ne sont pas forcément des fichiers textes mais
de tout format. Le programme suivant extrait un fichier parmi ceux qui
ont été compressés puis affiche son contenu (on suppose que le fichier
lu est au format texte donc lisible).

::

    import zipfile
    with zipfile.ZipFile ("exemplezip.zip", "r") as fz:
        data = fz.read ("informatique/testzip.py")
    print(data)

On retrouve dans ce cas les étapes d'ouverture et de fermeture même si
la première est implicitement inclus dans le constructeur de la classe
`ZipFile <https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile>`_.

Ecriture
--------

Pour créer un fichier *zip*, le procédé ressemble à la création de
n'importe quel fichier. La seule différence provient du fait qu'il
est possible de stocker le fichier à compresser sous un autre nom à
l'intérieur du fichier *zip*, ce qui explique les deux premiers arguments
de la méthode `write <https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.write>`_.
Le troisième paramètre indique si le fichier doit être compressé
`ZIP_DEFLATED <https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_DEFLATED>`_
ou non `ZIP_STORED <https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_STORED>`_.

::

    import zipfile
    with zipfile.ZipFile ("test.zip", "w") as f:
        file.write ("fichier.txt", "nom_fichier_dans_zip.txt", zipfile.ZIP_DEFLATED)

Une utilisation possible de ce procédé serait l'envoi automatique
d'un mail contenant un fichier *zip* en pièce jointe. Une requête comme
*python* précédant le nom de votre serveur de mail permettra, via un moteur
de recherche, de trouver des exemples sur Internet.

Selon les serveurs de mails, le programme permettant d'envoyer automatiquement
un mail en *python* peut varier. L'exemple suivant permet d'envoyer un email
automatiquement via un serveur de mails, il montre aussi comment attacher des
pièces jointes. Il faut bien sûr être autorisé à se connecter. De plus, il est
possible que l'exécution de ce programme ne soit pas toujours couronnée de succès
si le mail est envoyé plusieurs fois à répétition, ce comportement est en effet
proche de celui d'un spammeur.

::

    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
    from email.utils import formatdate
    from email import encoders
    import os

    def envoyer_mail (aqui, sujet, contenu, files = []):
        de = "email de l'auteur"
        msg = MIMEMultipart()
        msg['From'] = de
        msg['To'] = aqui
        msg['Date'] = formatdate (localtime = True)
        msg['Subject'] = sujet

        msg.attach(MIMEText(contenu))
        for file in files:
            part = MIMEBase('application', 'octet-stream')
            with open(file,'rb') as f:
                content = f.read()
            part.set_payload(content)
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',  \
                            'attachment; filename="%s"' % os.path.basename(file))
            msg.attach(part)

        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login("login", "mot_de_passe")

        smtp.sendmail(de, aqui, msg.as_string())
        smtp.close()

    envoyer_mail("destinataire", "sujet","contenu", ["mail.py"])

Manipulation de fichiers
========================

Il arrive fréquemment de copier, recopier, déplacer, effacer des fichiers.
Lorsqu'il s'agit de quelques fichiers, le faire manuellement ne pose pas
de problème. Lorsqu'il s'agit de traiter plusieurs centaines de fichiers,
il est préférable d'écrire un programme qui s'occupe de le faire
automatiquement. Cela peut être la création automatique d'un fichier
*zip* incluant tous les fichiers modifiés durant la journée ou la
réorganisation de fichiers musicaux au format *mp3* à l'aide de modules
complémentaires tel que `mutagen <https://pypi.python.org/pypi/mutagen>`_.

Pour ceux qui ne sont pas familiers des systèmes d'exploitation,
il faut noter que *Windows* ne fait pas de différences entre les majuscules et les
minuscules à l'intérieur d'un nom de fichier. Les systèmes *Linux* et *Mac OSX*
font cette différence. Ceci explique que certains programmes aient des comportements
différents selon le système d'exploitation sur lequel ils sont exécutés ou encore
que certains liens Internet vers des fichiers ne débouchent sur rien car
ils ont été saisis avec des différences au niveau des minuscules majuscules.

Gestion des noms de chemins
---------------------------

Le module `os.path <https://docs.python.org/3/library/os.path.html>`_
propose plusieurs fonctions très utiles qui permettent entre autres de tester
l'existence d'un fichier, d'un répertoire, de récupérer diverses informations
comme sa date de création, sa taille... La liste qui suit est loin d'être exhaustive
mais elle donne une idée de ce qu'il est possible de faire.

.. list-table::
    :widths: 5 10
    :header-rows: 0

    * - `abspath(path) <https://docs.python.org/3/library/os.path.html#os.path.abspath>`_
      - Retourne le chemin absolu d'un fichier ou d'un répertoire.
    * - `commonprefix(list) <https://docs.python.org/3/library/os.path.html#os.path.commonprefix>`_
      - Retourne le plus grand préfixe commun à un ensemble de chemins.
    * - `dirname(path) <https://docs.python.org/3/library/os.path.html#os.path.dirname>`_
      - Retourne le nom du répertoire.
    * - `exists(path) <https://docs.python.org/3/library/os.path.html#os.path.exists>`_
      - Dit si un chemin est valide ou non.
    * - `getatime(path) <https://docs.python.org/3/library/os.path.html#os.path.getatime>`_
      - date de la dernière modification
    * - `getmtime(path) <https://docs.python.org/3/library/os.path.html#os.path.getmtime>`_
      - date de la dernière modification
    * - `getctime(path) <https://docs.python.org/3/library/os.path.html#os.path.getctime>`_
      - date de la création
    * - `getsize(file) <https://docs.python.org/3/library/os.path.html#os.path.getsize>`_
      - Retourne la taille d'un fichier.
    * - `isabs(path) <https://docs.python.org/3/library/os.path.html#os.path.isabs>`_
      - Retourne ``True`` si le chemin est un chemin absolu.
    * - `isfile(path) <https://docs.python.org/3/library/os.path.html#os.path.isfile>`_
      - Retourne ``True`` si le chemin fait référence à un fichier.
    * - `isdir(path) <https://docs.python.org/3/library/os.path.html#os.path.isdir>`_
      - Retourne ``True`` si le chemin fait référence à un répertoire.
    * - `join(p1, p2, ...) <https://docs.python.org/3/library/os.path.html#os.path.join>`_
      - Construit un nom de chemin étant donné une liste de répertoires.
    * - `split(path) <https://docs.python.org/3/library/os.path.html#os.path.split>`_
      - Découpe un chemin, isole le nom du fichier ou le dernier répertoire
        des autres répertoires.
    * - `splitext(path) <https://docs.python.org/3/library/os.path.html#os.path.splitext>`_
      - Découpe un chemin en nom + extension.

Copie, suppression
------------------

.. list-table::
    :widths: 5 10
    :header-rows: 0

    * - `copy (f1,f2) <https://docs.python.org/3/library/shutil.html?highlight=shutil#shutil.copy>`_
      - Copie le fichier ``f1`` vers ``f2``.
    * - `chdir (p) <https://docs.python.org/3/library/os.html?highlight=chdir#os.chdir>`_
      - Change le répertoire courant, cette fonction peut être importante lorsqu'on
        utilise la fonction
        `system <https://docs.python.org/3/library/os.html?highlight=chdir#os.system>`_ du module
        `os <https://docs.python.org/3/library/os.html?highlight=chdir#os.chdir>`_  pour lancer une
        instruction en ligne de commande ou lorsqu'on écrit un fichier sans préciser le nom du répertoire,
        le fichier sera écrit dans ce répertoire courant qui est par défaut le répertoire où est situé
        le programme *python*. C'est à partir du
        répertoire courant que sont définis les chemins relatifs.
    * - `getcwd () <https://docs.python.org/3/library/os.html?highlight=chdir#os.getcwd>`_
      - Retourne le répertoire courant, voir la fonction ``chdir``.
    * - `mkdir (p) <https://docs.python.org/3/library/os.html?highlight=chdir#os.mkdir>`_
      - Crée le répertoire ``p``. \\ \hline
    * - `makedirs (p) <https://docs.python.org/3/library/os.html?highlight=chdir#os.makedirs>`_
      - Crée le répertoire ``p`` et tous les répertoires des niveaux supérieurs
        s'ils n'existent pas. Dans le cas du répertoire
        ``d:/base/repfinal``, crée d'abord ``d:/base`` s'il n'existe pas,
        puis ``d:/base/repfinal``.
    * - `remove (f) <https://docs.python.org/3/library/os.html?highlight=chdir#os.remove>`_
      - Supprime un fichier.
    * - `rename (f1,f2) <https://docs.python.org/3/library/os.html?highlight=chdir#os.rename>`_
      - Renomme un fichier
    * - `rmdir (p) <https://docs.python.org/3/library/os.html?highlight=chdir#os.rmdir>`_
      - Supprime un répertoire

Liste de fichiers
-----------------

La fonction
`listdir <https://docs.python.org/3/library/os.html?highlight=chdir#os.listdir>`_
permet de retourner les listes des éléments inclus dans un répertoire
(fichiers et sous-répertoires).
Le module `glob <https://docs.python.org/3/library/glob.html?highlight=glob#module-glob>`_
propose une fonction plus intéressante qui permet de retourner la liste
des éléments d'un répertoire en appliquant un filtre. Le programme
suivant permet par exemple de retourner la liste des fichiers et
des répertoires inclus dans un répertoire.

.. runpython::
    :showcode:

    import glob
    import os.path

    def liste_fichier_repertoire (folder, filter) :
        # résultats
        file,fold = [], []

        # recherche des fichiers obéissant au filtre
        res = glob.glob (folder + "\\" + filter)

        # on inclut les sous-répertoires qui n'auraient pas été
        # sélectionnés par le filtre
        rep = glob.glob (folder + "\\*")
        for r in rep :
            if r not in res and os.path.isdir (r) :
                res.append (r)

        # on ajoute fichiers et répertoires aux résultats
        for r in res :
            path = r
            if os.path.isfile (path) :
                # un fichier, rien à faire à part l'ajouter
                file.append (path)
            else :
                # sous-répertoire : on appelle à nouveau la fonction
                # pour retourner la liste des fichiers inclus
                fold.append (path)
                fi,fo = liste_fichier_repertoire (path, filter)
                file.extend (fi)  # on étend la liste des fichiers
                fold.extend (fo)  # on étend la liste des répertoires
        # fin
        return file,fold

    folder = r"."
    filter = "*.rst"
    file,fold = liste_fichier_repertoire (folder, filter)

    for f in file :
        print("fichier ", f)
    for f in fold :
        print("répertoire ", f)

Le programme repose sur l'utilisation d'une fonction récursive
qui explore d'abord le premier répertoire. Elle se contente d'ajouter à
une liste les fichiers qu'elle découvre puis cette fonction s'appelle
elle-même sur le premier sous-répertoire qu'elle rencontre.
La fonction `walk <https://docs.python.org/3/library/os.html?highlight=walk#os.walk>`_
permet d'obtenir la liste des fichiers et des sous-répertoire.
Cette fonction parcourt automatiquement les sous-répertoires inclus,
le programme est plus court mais elle ne prend pas en compte le filtre
qui peut être alors pris en compte grâce aux expressions régulières
(voir :ref:`regex_label_chap`).

.. runpython::
    :showcode:

    import os

    def liste_fichier_repertoire (folder) :
        file, rep = [], []
        for r, d, f in os.walk (folder) :
            for a in d : rep.append (r + "/" + a)
            for a in f : file.append (r + "/" + a)
        return file, rep

    folder = r"."
    file,fold = liste_fichier_repertoire (folder)

    for f in file :
        print ("fichier ", f)
    for f in fold :
        print ("répertoire ", f)

Format binaire
==============

.. index:: format binaire

Ecrire et lire des informations au travers d'un fichier texte revient
à convertir les informations quel que soit leur type dans un format
lisible pour tout utilisateur. Un entier est écrit sous forme de
caractères décimaux alors que sa représentation en mémoire est binaire.
Cette conversion dans un sens puis dans l'autre est parfois jugée
coûteuse en temps de traitement et souvent plus gourmande en terme
de taille de fichiers. Un fichier texte compressé, au format *zip* par
exemple, est une alternative aux fichiers binaires en terme de taille
mais il allonge la lecture et l'écriture par des étapes de compression
et de décompression. Même si elle permet de relire les informations écrites
grâce à n'importe quel éditeur de texte, il est parfois plus judicieux pour
une grande masse d'informations d'utiliser directement le format binaire,
c'est-à-dire celui dans lequel elles sont stockées en mémoire.
Les informations apparaissent dans leur forme la plus simple pour
l'ordinateur : une suite d'octets (bytes en anglais).
Deux étapes vont intervenir que ce soit pour l'écriture :

1. On récupère les informations dans une suite d'octets
   (fonction `pack <https://docs.python.org/3/library/struct.html?highlight=pack#struct.pack>`_
   du module `struct <https://docs.python.org/3/library/struct.html>`_).
2. On les écrit dans un fichier
   (méthode `write <https://docs.python.org/3.6/library/io.html?highlight=readlines#io.RawIOBase.write>`_
   affiliée aux fichiers).

Ou la lecture :

1. On lit une suite d'octets depuis un fichier
   (méthode `read <https://docs.python.org/3.6/library/io.html?highlight=readlines#io.BufferedIOBase.read>`_
   affiliée aux fichiers).
2. On transforme cette suite d'octets pour retrouver l'information
   qu'elle formait initialement
   (fonction `unpack <https://docs.python.org/3/library/struct.html?highlight=pack#struct.unpack>`_).

L'utilisation de fichiers binaires est moins évidente qu'il n'y paraît et
il faut faire appel à des modules spécialisés alors que la gestion des
fichiers texte ne pose aucun problème. Cela vient du fait que *python*
ne donne pas directement accès à la manière dont sont stockées les
informations en mémoire contrairement à des langages tels que le
`C++ <https://fr.wikipedia.org/wiki/C%2B%2B>`_.
L'intérêt de ces fichiers réside dans le fait que l'information qu'ils
contiennent prend moins de place stockée en binaire plutôt que convertie
en chaînes de caractères au format texte. Par exemple, un réel est toujours
équivalent à huit caractères en format binaire alors que sa conversion au
format texte va souvent jusqu'à quinze caractères.

L'écriture et la lecture d'un fichier binaire soulèvent les mêmes
problèmes que pour un fichier texte : il faut organiser les données
avant de les enregistrer pour savoir comment les retrouver. Les
types immuables (réel, entier, caractère) sont assez simples à gérer
dans ce format. Pour les objets complexes, *python* propose une solution grâce au module
`pickle <https://docs.python.org/3/library/pickle.html>`_
(voir aussi le modile `dill <https://pypi.python.org/pypi/dill>`_
pour des types telles que des fonctions).

Ecriture dans un fichier binaire
--------------------------------

L'écriture d'un fichier binaire commence par l'ouverture du fichier en mode
écriture par l'instruction ``open("<nom_fichier>", "wb")``.
C'est le code ``"wb"`` qui est important (*w* pour *write*, *b* pour *binary*),
il spécifie le mode d'ouverture ``"w"`` et le format ``"b"``.
La fermeture est la même que pour un fichier texte.

Le module `struct <https://docs.python.org/3/library/struct.html>`_
et la fonction `pack <https://docs.python.org/3/library/struct.html?highlight=pack#struct.pack>`_
permet de convertir les informations sous forme de chaîne de caractères
avant de les enregistrer au format binaire.
La fonction `pack <https://docs.python.org/3/library/struct.html?highlight=pack#struct.pack>`_
construit une chaîne de caractères égale
au contenu de la mémoire. Son affichage avec la fonction *print*
produit quelque chose d'illisible le plus souvent.
Le tableau suivant montre les principaux formats de conversion
(`liste complète <https://docs.python.org/3/library/struct.html?highlight=pack#format-characters>`_) :

* ``c`` : caractère
* ``B`` : caractère non signé (octet)
* ``i`` : entier (4 octets)
* ``I`` : entier non signé (4 octets)
* ``d`` : double (8 octets)

L'utilisation de ces codes est illustrée au paragraphe suivant.

Lecture d'un fichier binaire
----------------------------

Le code associé à l'ouverture d'un fichier binaire en mode
lecture est ``"rb"``, cela donne : ``open("<nom_fichier>", "rb")``.
La lecture utilise la fonction
`unpack <https://docs.python.org/3/library/struct.html?highlight=pack#struct.unpack>`_
pour effectuer la conversion inverse, celle d'une chaîne de caractères en
entiers, réels, ... Le paragraphe suivant illustre la lecture et l'écriture au format binaire.

Exemple fichier binaire
-----------------------

Cet exemple crée un fichier ``"info.bin"`` puis écrit des informations à
l'intérieur. Il ne sera pas possible d'afficher le contenu du
fichier à l'aide d'un éditeur de texte.

.. runpython::
    :showcode:

    import struct
    # on enregistre un entier, un réel et 4 caractères
    i = 10
    x = 3.1415692
    s = "ABCD"

    # écriture
    with open ("info.bin", "wb") as fb:
        fb.write ( struct.pack ("i" , i) )
        fb.write ( struct.pack ("d" , x) )
        octets = s.encode("ascii")                  # il faut convertir les caractères en bytes
        fb.write ( struct.pack ("4s" , octets) )

    # lecture
    with open ("info.bin", "rb") as fb:
        i = struct.unpack ("i",   fb.read (4))
        x = struct.unpack ("d",   fb.read (8))
        s = struct.unpack ("4s",   fb.read (4))

    # affichage pour vérifier que les données ont été bien lues
    print(i)
    print(x)
    print(s)

Les résultats de la méthode `unpack <https://docs.python.org/3/library/struct.html?highlight=pack#struct.unpack>`_
apparaissent dans un tuple mais les données sont correctement récupérées.
Ce programme fait aussi apparaître une des particularité du format
binaire. On suppose ici que la chaîne de caractères est toujours de
longueur 4. En fait, pour stocker une information de dimension variable,
il faut d'abord enregistrer cette dimension puis s'en servir lors de
la relecture pour connaître le nombre d'octets à lire. On modifie le
programme précédent pour sauvegarder une chaîne de caractères de longueur variable.

.. runpython::
    :showcode:

    import struct
    # on enregistre un entier, un réel et n caractères
    i = 10
    x = 3.1415692
    s = "ABCDEDF"

    # écriture
    with open ("info.bin", "wb") as fb:
        fb.write ( struct.pack ("i" , i) )
        fb.write ( struct.pack ("d" , x) )
        r = s.encode("utf-8")
        fb.write ( struct.pack ("i" , len(r)) )  # on sauve la dimension de r
        fb.write ( struct.pack ("{0}s".format(len(r)), r) )

    # lecture
    with open ("info.bin", "rb") as fb:
        i = struct.unpack ("i", fb.read (4))
        x = struct.unpack ("d", fb.read (8))
        size = struct.unpack ("i", fb.read (4)) # on récupère la dimension de s
        size = size [0]  # l est un tuple, on s'intéresse à son unique élément
        s = struct.unpack ("{0}s".format(size), fb.read (size))

    # affichage pour contrôler
    print(i)
    print(x)
    print(s)

Cette méthode utilisée pour les chaînes de caractères est applicable aux
listes et aux dictionnaires de longueur variable : il faut d'abord
stocker leur dimension. Il faut retenir également que la taille
d'un réel est de huit octets, celle d'un entier de quatre octets
et celle d'un caractère d'un octet. Cette règle est toujours vrai sur des ordinateurs 32 bits.
Cette taille varie sur les ordinateurs 64 bits. Le programme suivant donnera
la bonne réponse.

.. runpython::
    :showcode:

    from struct import pack
    print(len(pack('i', 0)))
    print(len(pack('d', 0)))
    print(len(pack('s', b'0')))

Cette taille doit être passée en argument à la méthode ``read``.

Objets plus complexes
---------------------

.. index:: sérialisation

Il existe un moyen de sauvegarder dans un fichier des objets
plus complexes à l'aide du module `pickle <https://docs.python.org/3/library/pickle.html>`_
Celui-ci permet de stocker dans un fichier le contenu d'un dictionnaire
à partir du moment où celui-ci contient des objets standard du
langage *python*. Le principe pour l'écriture est le suivant :

::

    import pickle

    dico = {'a': [1, 2.0, 3, "e"], 'b': ('string', 2), 'c': None}
    lis  = [1, 2, 3]

    with open ('data.bin', 'wb') as fb:
        pickle.dump(dico, fb)
        pickle.dump(lis, fb)

La lecture est aussi simple :

::

    with open('data.bin', 'rb') as fb:
        dico = pickle.load(fb)
        lis  = pickle.load(fb)

Un des avantages du module `pickle <https://docs.python.org/3/library/pickle.html>`_
est de pouvoir gérer les références circulaires : il est capable d'enregistrer
et de relire une liste qui se contient elle-même,
ce peut être également une liste qui en contient une autre qui contient la première...
Le module *pickle* peut aussi gérer les classes définies par un programmeur
à condition qu'elles puissent convertir leur contenu en un dictionnaire
dans un sens et dans l'autre, ce qui correspond à la plupart des cas.

.. runpython::
    :showcode:

    import pickle
    import copy

    class Test :
        def __init__ (self) :
            self.chaine = "a"
            self.entier = 5
            self.tuple  = { "h":1, 5:"j" }

        def __str__(self):
            return "c='{0}' e={1} t={2}".format(self.chaine, self.entier, self.tuple)

    t = Test ()

    with open('data.bin', 'wb')  # lecture
    pickle.dump (t, f)
    f.close()

    f = open('data.bin', 'rb')  # écriture
    t = pickle.load(f)
    f.close()

    print(t)

Lorsque la conversion nécessite un traitement spécial, il faut
surcharger les opérateurs
`__getstate__ <https://docs.python.org/3/library/pickle.html?highlight=__getstate__#object.__getstate__>`_
et `__setstate__ <https://docs.python.org/3/library/pickle.html?highlight=__setstate__#object.__setstate__>`_
Ce cas se produit par exemple lorsqu'il n'est pas nécessaire d'enregistrer
tous les attributs de la classe car certains sont calculés ainsi
que le montre l'exemple suivant :

.. runpython::
    :showcode:
    :process:

    import pickle
    import copy

    class Test :
        def __init__ (self) :
            self.x = 5
            self.y = 3
            self.calcule_norme ()   # attribut calculé
        def calcule_norme (self) :
            self.n = (self.x ** 2 + self.y ** 2) ** 0.5
        def __getstate__ (self) :
            """conversion de Test en un dictionnaire"""
            d = copy.copy (self.__dict__)
            del d ["n"]  # attribut calculé, on le sauve pas
            return d
        def __setstate__ (self,dic) :
            """conversion d'un dictionnaire dic en Test"""
            self.__dict__.update (dic)
            self.calcule_norme ()  # attribut calculé

        def __str__(self):
            return "x={0} y={1} n={2}".format(self.x, self.y, self.n)

    t = Test ()

    with open('data.bin', 'wb') as fb:  # lecture
        pickle.dump(t, fb)

    with open('data.bin', 'rb') as fb: # écriture
        t = pickle.load(fb)

    print(t)

Le module `pickle <https://docs.python.org/3/library/pickle.html>`_
ne permet de sérialiser tout type d'objet comme les fonctions. Il est
parfois utile de sauver une fonction car c'est un paramètre du programme.
Il faut dans ce cas soit le faire soi-même, soit utiliser le module
`dill <https://pypi.python.org/pypi/dill>`_.
