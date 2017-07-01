
.. blogpost::
    :title: Inclure un partie C dans un module Python
    :keywords: python, C
    :date: 2017-07-01
    :categories: module

    Je me suis amusé à programmer un module Python
    qui inclut des fonctions écrites en C.
    J'ai ajouté un build automatique sur
    `travis <https://travis-ci.org/sdpython/cpyquickhelper>`_ et
    `appveyor <https://ci.appveyor.com/project/sdpython/cpyquickhelper>`_.
    La documentation du module
    `cpyquickhelper <http://www.xavierdupre.fr/app/cpyquickhelper/helpsphinx/index.html>`_
    et le code sur `github <https://github.com/sdpython/cpyquickhelper/>`_.

    Parmi les choses à retenir, il faut un compilateur C++,
    `Visual Studio Community Edition 2015 <https://docs.python.org/3/using/windows.html?highlight=visual#compiling-python-on-windows>`_
    et `gcc <https://fr.wikipedia.org/wiki/GNU_Compiler_Collection>`_
    sous Linux. Pour construire l'extension :

    ::

        python setup.y build_ext --inplace

    Le paramètre ``--inplace`` précise que le module doit être compilé
    sur place. Le module peut alors être importé. La partie intéressante
    commence
    `ici <https://github.com/sdpython/cpyquickhelper/blob/master/src/cpyquickhelper/io/stdchelper.cpp#L68>`_.
