# coding: utf-8
"""

===============================
Mathador, énigme à 4 opérations
===============================

Un petit problème de chiffre, le
`mathador <https://maitressedelaforet.fr/le-mathador-rituel-de-calcul-mental/>`_
consiste à trouver un montant à partir de 5 nombres et 4 opérations.

Example : composer 28 avec 17, 12, 3, 2, 1 et les opérations `*`, `+`, `/`, `-`.

Il faut tout utiliser.

C'est plus simple avec un programme, non ?

J'ai fait ça très vite. Il y a sans doute mieux.
"""

from itertools import permutations

nombres = [17, 12, 3, 2, 1]
ops = ["+", "-", "/", "*"]
total = 28

solution = []
parentheses = [(i, j) for i in range(3) for j in range(i + 1, 4)]

# permutations sur les nombres
for pn in permutations(nombres):
    # permutations sur les opérations
    for po in permutations(ops):
        exp = []
        for d, o in zip(pn, po):
            exp.append(str(d))
            exp.append(str(o))
        exp.append(str(pn[-1]))

        # 0 parenthèse
        text = "".join(exp)
        res = eval(text)
        if res == 28:
            print(res)
            solution.append(res)

        # 2 parenthèses
        for i, j in parentheses:
            exp[i * 2] = "(" + exp[i * 2]
            exp[j * 2] = exp[j * 2] + ")"
            text = "".join(exp)
            try:
                res = eval(text)
                if res == 28:
                    print(res, text)
                    solution.append(res)
            except ZeroDivisionError:
                pass
            exp[i * 2] = exp[i * 2][1:]
            exp[j * 2] = exp[j * 2][:-1]

        # 4 parenthèses
        for a, b in parentheses:
            exp[a * 2] = "(" + exp[a * 2]
            exp[b * 2] = exp[b * 2] + ")"
            for c, d in parentheses:
                exp[c * 2] = "(" + exp[c * 2]
                exp[d * 2] = exp[d * 2] + ")"
                text = "".join(exp)
                try:
                    res = eval(text)
                    if res == 28:
                        print(res, text)
                        solution.append(res)
                except ZeroDivisionError:
                    pass
                exp[c * 2] = exp[c * 2][1:]
                exp[d * 2] = exp[d * 2][:-1]
            exp[a * 2] = exp[a * 2][1:]
            exp[b * 2] = exp[b * 2][:-1]

        # 6 parenthèses...
