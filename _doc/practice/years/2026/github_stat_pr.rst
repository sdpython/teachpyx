.. _l-github-stat-pr-2026:

Statistiques de PR fusionnées par auteur et par semaine
=======================================================

Ce script récupère, via l'API GitHub, le nombre de *pull requests* (PR) fusionnées
pour **un ou plusieurs dépôts**, les regroupe par auteur et par semaine sur l'année
écoulée, puis enregistre les graphiques sous forme d'images PNG.

Les données récupérées sont **mises en cache** localement (un fichier CSV par dépôt).
Lors des exécutions suivantes, seules les PR plus récentes que la dernière date mise
en cache sont requêtées.

**Dépendances :** ``requests``, ``pandas``, ``matplotlib``.

**Usage :**

.. code-block:: bash

    export GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx  # optionnel mais recommandé
    python github_stat_pr.py

Images générées :

* ``github_stat_pr_bar.png`` — diagramme empilé (toutes repos confondues)
* ``github_stat_pr_heatmap.png`` — heatmap (toutes repos confondues)
* ``github_stat_pr_lines.png`` — graphe en lignes comparant les dépôts

.. literalinclude:: github_stat_pr.py
    :language: python
