
.. index:: culture algorithmique, algorithme, culture

Survol algorithmique
====================

Il est facile de caler un modèle statistiques lorsque les données sont propres
et de taille raisonnable. Ce n'est quasiment jamais le cas.
On a besoin de nettoyer ou de transformer les données. On a besoin
de réduire le temps de calcul d'un algorithme car il est inexploitable en l'état.
Pour ces deux raisons, il est utile de connaître quelques algorithmes
afin d'avoir d'avoir des idées. On a besoin d'avoir un moyen rapide, visuelle
et efficace de comparer deux résultats.

Ordres de grandeur
++++++++++++++++++

Qu'est-il raisonnable de faire à supposer qu'on ne dispose que d'une seule machine ?
La mémoire n'est plus un problème. Le temps de calcul l'est toujours.

* :math:`n \leqslant 10` : coût :math:`\leqslant O(2^n)`
* :math:`n \leqslant 15` : coût :math:`\leqslant O(n!)`
* :math:`n \leqslant 10^2` : coût :math:`\leqslant O(n^3)`
* :math:`n \leqslant 10^3` : coût :math:`\leqslant O(n^2)`
* :math:`n \leqslant 10^7` : coût :math:`\leqslant O(n \ln (n))`
* :math:`n > 10^8` : coût :math:`\leqslant O(n)`

Comprendre le coût d'un algorithme
++++++++++++++++++++++++++++++++++

Le coût de nombreux algorithmes non NP-complet se décomposer comme suit :
:math:`O(n^\alpha) O( \ln^\beta n ) O(1)`. Chaque terme correspond à :

* :math:`O(n^\alpha)` avec :math:`\alpha \in \mathbb{N} > 1` :
  un probème combinatoire se résume à un algorithme
  de coût quadratique, cela est dû à la `programmation dynamique
  <https://fr.wikipedia.org/wiki/Programmation_dynamique>`_.
  Dans la plupart des cas, on obtient ce coût après avoir transformé le problème dans une forme
  récurrente : on écrit ce qu'il faut faire pour calculer la solution avec *n+1* éléments
  sachant qu'on connaît la solution avec *n* éléments.
* :math:`O(n^\beta n)` avec :math:`\beta \in \mathbb{N} > 0`,
  coût `dichotomique <https://fr.wikipedia.org/wiki/Recherche_dichotomique>`_,
  on coupe le problème en deux à chaque itération.
* :math:`O(1)` : `table de hashage <https://fr.wikipedia.org/wiki/Table_de_hachage>`_

Dès qu'on sort des puissances entières, il faut s'attendre à un algorithme non trivial
tel que l':epkg:`algorithme de Strassen`
pour la multiplication de matrice (:math:`n^{2.807}`), ou celui
de `Marco Bodrato <http://www.bodrato.it/papers/>`_
(`A Strassen-like Matrix Multiplication Suited for Squaring and Higher Power Computation
<http://marco.bodrato.it/papers/Bodrato2010-StrassenLikeMatrixMultiplicationForSquares.pdf>`_).

Le coût minimal d'un algorithme de tri est :math:`O(n \ln n)` dans le cas générique
c'est-à-dire sans hypothèse sur les données. En revanche, dans le cas où les données
sont issues d'un ensemble fini de cardinal *m*, le meilleur tri revient à calculer un histogramme
et est de coût inférieur à :math:`O( \inf \{ n \ln n, m \} )`.

L'article de blog
`Fast Interesection of Sorted Lists Using SSE Instructions
<https://highlyscalable.wordpress.com/2012/06/05/fast-intersection-sorted-lists-sse/>`_
part d'un problème simple qui est l'intersection de deux listes triées et montre
comment optimiser son implémentation en introduisant la notion de partitions et un peu
de parallélisation.

Mot-clé
+++++++

L'objectif n'est pas de les comprendre tous mais plus de connaître
les problèmes pour lesquels ils ont été conçus.

La distance d'édition sert à calculer la distance entre deux mots.
On peut l'utiliser pour trouver les mots les plus proches d'un autre
à condition que ces mots ne soient pas nombreux (:math:`\sim 10^4`).
Que faire quand ils sont un milliard ? Ce serait plus facile
si les mots étaient représentés par des vecteurs (voir
`word2vec <https://pypi.python.org/pypi/word2vec>`_,
`Auto Encoders <https://piotrmirowski.wordpress.com/2014/03/27/tutorial-on-auto-encoders/>`_).

On veut comparer deux modèles de ranking.
On veut pouvoir comparer visuellement les résultats. Quel ordre
est mieux qu'un autre ? Comment afficher les résultats
de deux moteurs de recherche de telle sorte que l'oeil
humain saisisse rapidement la différence ?

Tout ce qui suit vous donnera des idées.

.. _l-algoculture-shortlist:

Catalogue d'algorithmes
+++++++++++++++++++++++

* Tri
    * `tri fusion <http://fr.wikipedia.org/wiki/Tri_fusion>`_ **algo**
    * `bucket sort <http://en.wikipedia.org/wiki/Bucket_sort>`_ **algo**
    * `tri à bulles <http://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles>`_ **algo**
* Complexité
    * `Complexité de Lempel-Ziv <https://github.com/Naereen/Lempel-Ziv_Complexity>`_ **algo**
* Distance
    * `Python implementation of Kullback-Leibler divergences and kl-UCB indexes <https://github.com/Naereen/Kullback-Leibler-divergences-and-kl-UCB-indexes>`_ **algo**
* Calcul matriciel
    * `Winograd Minimum Filtering <https://arxiv.org/abs/2111.00977>`_ **algo** convolution rapide
    * `im2col <http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/notebooks/convolutation_matmul.html>`_ **algo**
      ou comment réarranger une matrice pour transformer une convolution entre un produit matriciel
* Diviser pour reigner
    * `dichotomie <http://fr.wikipedia.org/wiki/Dichotomie>`_ **algo**
    * `branch and bound <http://en.wikipedia.org/wiki/Branch_and_bound>`_ **algo**
    * `The Ultimate Planar Convex Hull Algorithm?
      <https://www.cs.princeton.edu/~chazelle/temp/451/451-2019/KirkSeidel.pdf>`_ **algo**
      (relectures `Kirkpatrick-Seidel’s Prune-and-Search Convex Hull Algorithm
      <http://www.cse.yorku.ca/~andy/courses/6114/lecture-notes/KirkSeidel.pdf>`_,
      `An Algorithm for Finding Convex Hulls of Planar Point Sets
      <https://arxiv.org/ftp/arxiv/papers/1212/1212.6043.pdf>`_),
      détermine l'enveloppe convexe d'un ensemble de points avec
      un coût de :math:`O(n \ln H)` où *H* est le nombre de segments
      de l'enveloppe
* Programmation dynamique
    * `distance d'édition <http://fr.wikipedia.org/wiki/Distance_de_Levenshtein>`_ **algo**
    * `plus court chemin dans un graphe <orghttp://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra>`_ **algo**
    * `problème d'ordonnancement <http://fr.wikipedia.org/wiki/Th%C3%A9orie_de_l'ordonnancement>`_ **algo**
* Permutations
    * `Sattolo's algorithm <https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#Sattolo's_algorithm>`_ **algo**
* Problème non `NP-complet <http://fr.wikipedia.org/wiki/Liste_de_probl%C3%A8mes_NP-complets>`_
    * `Problème du voyageur de commerce <http://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce>`_  **algo**
      (ou `Graphe Hamiltonien <http://fr.wikipedia.org/wiki/Graphe_hamiltonien>`_),
      lire `Solution of a Large-Scale Traveling-Salesman Problem <http://www.cs.uleth.ca/~benkoczi/OR/read/tsp-dantzig-fulkerson-johnson-54.pdf>`_.
    * `Problème de tournées de véhicules <https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_tourn%C3%A9es_de_v%C3%A9hicules>`_ **algo**,
      extension du problème du voyageur de commerce
    * `problème d'affectation, méthode hongroise <http://fr.wikipedia.org/wiki/Algorithme_hongrois>`_ **algo**
    * `arbre de poids miminum (Kruskal) <http://fr.wikipedia.org/wiki/Algorithme_de_Kruskal>`_ **algo**
    * `arbre de poids miminum (Borůvka) <https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm>`_ **algo**
    * `problème du sac-à-dos <http://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos>`_ **algo**
* Structure de données
    * `liste chaînée <http://fr.wikipedia.org/wiki/Liste_cha%C3%AEn%C3%A9e>`_ **déf**
    * `table de hachage <http://fr.wikipedia.org/wiki/Table_de_hachage>`_ **déf**
    * `table de hashage distribuée <https://en.wikipedia.org/wiki/Distributed_hash_table>`_
    * `suffix tree <http://fr.wikipedia.org/wiki/Arbre_des_suffixes>`_ **déf**
    * `trie <http://fr.wikipedia.org/wiki/Trie_(informatique)>`_ **déf**
    * `b-tree <http://fr.wikipedia.org/wiki/Arbre_B>`_ **déf**
    * `x-fast-trie <https://en.wikipedia.org/wiki/X-fast_trie>`_ **déf**
    * `tas ou heap <https://fr.wikipedia.org/wiki/Tas_(informatique)>`_ ,
      `Fibonacci Heap <https://en.wikipedia.org/wiki/Fibonacci_heap>`_ **déf**
    * `Judy Arrays <https://en.wikipedia.org/wiki/Judy_array>`_,
      `site <http://judy.sourceforge.net/>`_,
      `en python <https://github.com/arnimarj/py-judy>`_,
      `en C <https://github.com/JanX2/judy-arrays>`_,
      cette structure implémente un mapping int/int plus efficace que
      l'implémentation traditionnelle avec une table de hashage,
      la structure utilise les propriétés des caches dans les
      processeurs **déf**
* Graphes
    * composantes connexes ou `parcours de graphe en profondeur <http://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur>`_,
      `parcours de graphe en largeur <http://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur>`_ **déf/algo**
    * `graphe orienté <http://fr.wikipedia.org/wiki/Graphe_orient%C3%A9>`_, `graphe acyclique <http://fr.wikipedia.org/wiki/Graphe_acyclique>`_ **déf**
    * `degré <http://fr.wikipedia.org/wiki/Degr%C3%A9_(th%C3%A9orie_des_graphes)>`_ **déf**
    * `FLoyd-Flukerson <http://fr.wikipedia.org/wiki/Algorithme_de_Ford-Fulkerson>`_ **algo**
    * `minimum cut <http://en.wikipedia.org/wiki/Minimum_cut>`_ **algo**
    * `maximum cut <http://en.wikipedia.org/wiki/Maximum_cut>`_ **algo**
    * `graphe bi-parti <http://fr.wikipedia.org/wiki/Graphe_biparti>`_ **déf**
    * `PageRank <http://fr.wikipedia.org/wiki/PageRank>`_ **algo**
    * `Appariement <http://fr.wikipedia.org/wiki/Couplage_(th%C3%A9orie_des_graphes)>`_,
      `Edmonds Blossum <http://en.wikipedia.org/wiki/Blossom_algorithm>`_,
      `Hopcroft–Karp <http://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm>`_,
      `Blossom 5 <http://pub.ist.ac.at/~vnk/papers/blossom5.pdf>`_,
      **déf/algo** (ou couplage)
    * `Algorithme de Gale-Shapley <http://fr.wikipedia.org/wiki/Probl%C3%A8me_des_mariages_stables>`_, **algo**, problème des mariages stables
    * `distance de Robinson–Foulds <https://en.wikipedia.org/wiki/Robinson%E2%80%93Foulds_metric>`_, **algo**, distance entre deux arbres
    * robustesse d'un réseau
      `Quantifying the robustness of metro networks <https://arxiv.org/abs/1505.06664>`_
    * détection de motif fréquents
      `fp-growth <https://en.wikibooks.org/wiki/Data_Mining_Algorithms_In_R/Frequent_Pattern_Mining/The_FP-Growth_Algorithm>`_,
* Texte
    * `Algorithme de Knuth-Morris-Pratt <http://fr.wikipedia.org/wiki/Algorithme_de_Knuth-Morris-Pratt>`_ **algo**
    * `Algorithme de Rabin-Karp <http://fr.wikipedia.org/wiki/Algorithme_de_Rabin-Karp>`_ **algo**
    * `distance de Jaccard <http://fr.wikipedia.org/wiki/Indice_et_distance_de_Jaccard>`_ **algo**
    * `n-grammes <http://fr.wikipedia.org/wiki/N-gramme>`_ **déf**
    * `Algorithme d'Aho-Corasick <http://fr.wikipedia.org/wiki/Algorithme_d%27Aho-Corasick>`_ **algo**,
      voir aussi `Commentz-Walter <https://en.wikipedia.org/wiki/Commentz-Walter_algorithm>`_
    * `Transformée de Burrows-Wheeler <http://fr.wikipedia.org/wiki/Transform%C3%A9e_de_Burrows-Wheeler>`_ **algo**
    * `algorithme Apriori <https://en.wikipedia.org/wiki/Apriori_algorithm>`_ : apprentissage de règles d'associations **algo**
    * `Boyer–Moore string-search algorithm <https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm>`_
* Optimisation
    * `Simplexe <http://fr.wikipedia.org/wiki/Simplexe>`_ **algo**
    * `Optimisation Combinatoire : Programmation Linéaire et Algorithmes <http://www-desir.lip6.fr/~fouilhoux/documents/OptComb.pdf>`_ **thèse**
    * `Méthode de Nelder-Mead <https://fr.wikipedia.org/wiki/M%C3%A9thode_de_Nelder-Mead>`_ **algo**,
      `implémentation en Python <https://github.com/fchollet/nelder-mead>`_
* Autre
    * `codage Huffman <http://fr.wikipedia.org/wiki/Codage_de_Huffman>`_ (voir aussi `LZ77, LZ78 <http://fr.wikipedia.org/wiki/LZ77_et_LZ78>`_) **algo**
    * `bootstrap, intervalles de confiance <http://fr.wikipedia.org/wiki/Bootstrap_(statistiques)#Intervalle_de_confiance>`_ **algo**
    * `filtre de Bloom <http://fr.wikipedia.org/wiki/Filtre_de_Bloom>`_ **algo**
    * :epkg:`Algorithme de Strassen` **algo**
    * `Woodbury matrix identity <http://en.wikipedia.org/wiki/Woodbury_matrix_identity>`_ **algo**
    * `Blockwise inversion <http://en.wikipedia.org/wiki/Invertible_matrix#Blockwise_inversion>`_ **algo**
    * `Toom-Cook <https://en.wikipedia.org/wiki/Toom%E2%80%93Cook_multiplication>`_ **algo**
    * `Canopy Clustering <https://en.wikipedia.org/wiki/Canopy_clustering_algorithm>`_ **algo**
    * `LRU - Last Recent Used <https://fr.wikipedia.org/wiki/Algorithmes_de_remplacement_des_lignes_de_cache>`_ **algo**
* Programmation
    * `itérateur <http://fr.wikipedia.org/wiki/It%C3%A9rateur>`_ (mot-clé `yield <http://sametmax.com/comment-utiliser-yield-et-les-generateurs-en-python/>`_) **déf**
    * `mémoïzation <http://fr.wikipedia.org/wiki/M%C3%A9mo%C3%AFsation>`_ **déf**
      (voir aussi `Mémoïzation d'une fonction Python
      <https://sametmax.oprax.fr/memoization-dune-fonction-python/index.html>`_)
    * `programmation fonctionnelle <http://fr.wikipedia.org/wiki/Programmation_fonctionnelle>`_ **déf**
    * `récursivité <http://fr.wikipedia.org/wiki/R%C3%A9cursivit%C3%A9>`_ **déf**
    * `Kahan summation algorithm <https://en.wikipedia.org/wiki/Kahan_summation_algorithm>`_ **algo**
* Algorithmes probabilistes
    * `Probabilistic Data Structures for Web Analytics and Data Mining <https://highlyscalable.wordpress.com/2012/05/01/probabilistic-structures-web-analytics-data-mining/>`_
* Compression
    * `LZFSE <https://github.com/lzfse/lzfse>`_ **algo**
    * `LZMA <https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm>`_ **algo**
    * `LZ77 and LZ78 <https://en.wikipedia.org/wiki/LZ77_and_LZ78>`_ **algo**
    * `Squash Benchmark <http://quixdb.github.io/squash-benchmark/>`_
* Algorithmes d'inspiration quantique
    * `A quantum-inspired classical algorithm for recommendation systems
      <https://arxiv.org/abs/1807.04271>`_

Beaucoup de ces algorithmes sont implémentés dans ce projet :
`TheAlgorithms <https://github.com/TheAlgorithms/Python>`_.

Le module `algorithms <https://github.com/nryoung/algorithms>`_
implémente beaucoup d'algorithmes classiques tels que
la `recherche binaire <https://github.com/nryoung/algorithms/blob/master/algorithms/searching/binary_search.py>`_,
le générateur de nombre aléatoire de
`Mersenne <https://github.com/nryoung/algorithms/blob/master/algorithms/random/mersenne_twister.py>`_,
le tri `heapsort <https://github.com/nryoung/algorithms/blob/master/algorithms/sorting/heap_sort.py>`_.

Problèmes NP-complets
+++++++++++++++++++++

* `21 problèmes NP-complet de Karp <https://fr.wikipedia.org/wiki/21_probl%C3%A8mes_NP-complets_de_Karp>`_
* `Liste de problèmes NP complets <https://fr.wikipedia.org/wiki/Liste_de_probl%C3%A8mes_NP-complets>`_
  (`en <https://en.wikipedia.org/wiki/List_of_NP-complete_problems>`_)
* :ref:`l-np-complets`

.. index:: morphisme

Un peu de morphisme parce que ça m'a toujours fasciné :

* `Efficient and practical tree preconditioning for solving Laplacian systems <http://www.lix.polytechnique.fr/~maks/papers/SEA_2015_draft.pdf>`_
* `A Survey on Data-driven Dictionary-based Methods for 3D Modeling <http://www.lix.polytechnique.fr/~maks/papers/dictionary_survey.pdf>`_

Liens
+++++

* `Liste d'algorithme sur Wikipédia <http://en.wikipedia.org/wiki/List_of_algorithms>`_
  (`version française <http://fr.wikipedia.org/wiki/Liste_d%27algorithmes>`_)
* `List of machine learning concepts <http://en.wikipedia.org/wiki/List_of_machine_learning_concepts>`_
* `Machine Learning, Statistiques et Programmation <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/index.html>`_
* `Introduction to graphs and networks <http://freakonometrics.hypotheses.org/51106>`_
  (échantillon dans un graphe, chaîne de Markov, centralité, ...)
* `Networks and Flows #2 <http://freakonometrics.hypotheses.org/51457>`_

Articles sur des algorithmes
++++++++++++++++++++++++++++

* `Blossom5 <http://pub.ist.ac.at/~vnk/papers/blossom5.pdf>`_ **matching**
* `Local max-cut in smoothed polynomial time <https://arxiv.org/abs/1610.04807>`_ **max-cut**
* `Expander Flows, Geometric Embeddings and Graph Partitioning <http://snap.stanford.edu/class/cs224w-readings/arora04expansion.pdf>`_ **graph partitionning**
* `The Read-Optimized Burrows-Wheeler Transform <https://arxiv.org/pdf/1809.07320.pdf>`_
* `String Periods in the Order-Preserving Model <https://arxiv.org/pdf/1801.01404.pdf>`_
* `Recursive n-gram hashing is pairwise independent, at best <https://arxiv.org/pdf/0705.4676.pdf>`_,
  `Hash-Grams: Faster N-Gram Features for Classification and Malware Detection <http://www.edwardraff.com/publications/hash-grams-faster.pdf>`_
* `Computing Higher Order Derivatives of Matrix and Tensor Expressions <https://papers.nips.cc/paper/7540-computing-higher-order-derivatives-of-matrix-and-tensor-expressions.pdf>`_

Livres
++++++

* `Précis de recherche opérationnelle <https://www.dunod.com/sciences-techniques/precis-recherche-operationnelle-methodes-et-exercices-d-application>`_,
  Robert Faure, Bernard Lemaire, Christophe Picouleau
* `Programming Pearls <https://www.amazon.com/Programming-Pearls-2nd-Jon-Bentley/dp/0201657880>`_,
  Jon Bentley
* `Introduction to Algorithms 3rd Edition
  <https://github.com/calvint/AlgorithmsOneProblems/blob/master/Algorithms/Thomas%20H.%20Cormen,%20Charles%20E.%20Leiserson,%20Ronald%20L.%20Rivest,%20Clifford%20Stein%20Introduction%20to%20Algorithms,%20Third%20Edition%20%202009.pdf>`_,
  Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein
* `Programmation efficace - 128 algorithmes qu'il faut avoir compris et codés en Python au cours de sa vie <http://www.editions-ellipses.fr/product_info.php?products_id=10829>`_,
  ce livre est accompagné d'un répertoire sur GitHub :
  `tryalgo <https://github.com/jilljenn/tryalgo>`_
  (`documentation <http://jilljenn.github.io/tryalgo/>`_)
  et d'un site web `Résolution de problèmes algorithmiques <http://tryalgo.org/>`_

Pour s'entraîner
++++++++++++++++

* `Project Euler <https://projecteuler.net/about>`_
* `Archives de Google Jam <https://github.com/google/coding-competitions-archive>`_,
  voir aussi `Solutions to problems of Code Jam 2020, 2019, 2018, 2017 and earlier
  <https://github.com/salvois/codejam>`_
* `LeetCode <https://leetcode.com/>`_
* `Compétitions de programmation <http://tryalgo.org/contests/>`_,
  ce site recensent plusieurs compétitions comme celle-ci
  `Southwestern Europe Regional Contest (SWERC) <https://swerc.eu/2018/about/>`_
  dont les précédents exercices sont disponibles :
  `ACM-ICPC Live Archive <https://www.udebug.com/LA/icpc-archive-volumes>`_,
  mais aussi les problèmes du
  `Castor Informatique <https://castor-informatique.fr>`_
  pour les plus jeunes.

Google's recommandations
++++++++++++++++++++++++

*Coding*

You should know at least one programming language really well,
and it should preferably be C++ or Java. C# is OK too, since
it's pretty similar to Java. You will be expected to write some code
in at least some of your interviews. You will be expected to know a
fair amount of detail about your favorite programming language.

*Sorting*

Know how to sort. Don't do bubble-sort. You should know the details of
at least one :math:`n \log(n)` sorting algorithm, preferably two
(say, quick sort and merge sort). Merge sort can be highly useful
in situations where quick sort is impractical, so take a look at it.

*Hashtables*

Arguably the single most important data structure known to mankind.
You absolutely should know how they work. Be able to implement one
using only arrays in your favorite language, in about the space
of one interview.

*Trees*

Know about trees; basic tree construction, traversal and manipulation
algorithms. Familiarize yourself with binary trees, n-ary trees,
and trie-trees. Be familiar with at least one type of balanced binary
tree, whether it's a red/black tree, a splay tree or an AVL tree,
and know how it's implemented. Understand treetraversal

*Algorithms*

BFS and DFS, and know the difference between inorder, postorder and preorder.

*Graphs*

Graphs are really important at Google. There are 3 basic ways to
represent a graph in memory (objects and pointers, matrix, and
adjacency list); familiarize yourself with each representation and its
pros & cons. You should know the basic graph traversal algorithms:
breadth-first search and depth-first search. Know their computational
complexity, their tradeoffs, and how to implement them in real code.
If you get a chance, try to study up on fancier algorithms, such
as Dijkstra and A*.

*Other Data Structures*

You should study up on as many other data structures and algorithms as
possible. You should especially know about the most famous classes of
NP-complete problems, such as traveling salesman and the knapsack problem,
and be able to recognize them when an interviewer asks you them in disguise.
Find out whatNP-complete means.

*Mathematics*

Some interviewers ask basic discrete math questions. This is more prevalent
at Google than at other companies because counting problems, probability problems
, and other Discrete Math 101 situations surrounds us. Spend some time
before the interview refreshing your memory on (or teaching yourself)
the essentials of combinatorics and probability. You should be familiar
with n-choose-k problems and their ilk – the more the better.

*Operating Systems*

Know about processes, threads and concurrency issues. Know about locks and
mutexes and semaphores and monitors and how they work. Knowabout deadlock
and livelock and how to avoid them. Know what resources a processes needs,
and a thread needs, and how context switching works, and how it's initiated
by the operating system and underlying hardware. Know a little about
scheduling. The world is rapidly moving towards multi-core, so know the
fundamentals of "modern" concurrency constructs. For information on System

*Design*

`Distributed Systems and Parallel Computing <http://research.google.com/pubs/DistributedSystemsandParallelComputing.html>`_
