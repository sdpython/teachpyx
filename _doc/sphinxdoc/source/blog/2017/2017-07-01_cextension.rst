
.. blogpost::
    :title: Inclure un partie C dans un module Python
    :keywords: python, C
    :date: 2017-07-01
    :categories: module

    Je me suis amus� � programmer un module Python
    qui inclut des fonctions �crites en C.
    J'ai ajout� un build automatique sur
    `travis <https://travis-ci.org/sdpython/cpyquickhelper>`_ et
    `appveyor <https://ci.appveyor.com/project/sdpython/cpyquickhelper>`_.
    La documentation du module
    `cpyquickhelper <http://www.xavierdupre.fr/app/cpyquickhelper/helpsphinx/index.html>`_
    et le code sur `github <https://github.com/sdpython/cpyquickhelper/>`_.

    Parmi les choses � retenir, il faut un compilateur C++,
    `Visual Studio Community Edition 2015 <https://docs.python.org/3/using/windows.html?highlight=visual#compiling-python-on-windows>`_
    et `gcc <https://fr.wikipedia.org/wiki/GNU_Compiler_Collection>`_
    sous Linux. Pour construire l'extension :

    ::

        python setup.y build_ext --inplace

    Le param�tre ``--inplace`` pr�cise que le module doit �tre compil�
    sur place. Le module peut alors �tre import�. La partie int�ressante
    commence
    `ici <https://github.com/sdpython/cpyquickhelper/blob/master/src/cpyquickhelper/io/stdchelper.cpp#L68>`_.
