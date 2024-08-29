# coding: utf-8
"""
================
Float Conversion
================

I came up with the following question
:math:`(float64)x < (float64)y \\Longrightarrow (float32) x < (float32)y`?
What is the probability this holds?

Probability (float64)x == (float32)x
====================================

Let's evaluate how many time we draw a random double
number equal to its float conversion.
"""

import random
import numpy
import pandas
import matplotlib.pyplot as plt


rnd = numpy.random.random(100000000)
rnd.shape, rnd.dtype

######################################
#

rnd32 = rnd.astype(numpy.float32).astype(numpy.float64)
equal = (rnd == rnd32).sum()
equal


######################################
# It is very low. Let's check the reverse is true.


rnd32b = rnd32.astype(numpy.float64).astype(numpy.float32)
equal = (rnd32b == rnd32).sum()
equal


######################################
# Let's study the distribution of the difference.


delta = rnd - rnd32
numpy.min(delta), numpy.max(delta)


######################################
#

numpy.min(rnd), numpy.max(rnd)


######################################
#


plt.hist(delta, bins=1000)


######################################
# We finally check that double operations between float numpers remain floats.


for i in range(100000):
    i, j = random.randint(0, len(rnd32) - 1), random.randint(0, len(rnd32) - 1)
    d32 = numpy.float64(rnd32[i] * rnd32[j])
    d64 = numpy.float64(rnd32[i]) * numpy.float64(rnd32[j])
    if d32 != d64:
        raise AssertionError(
            "Issue with somme={0} = {1} + {2}".format(
                rnd32[i] + rnd32[j], rnd32[i], rnd32[j]
            )
        )


######################################
# Interval length distribution
# ============================
#
# Let's imagine now we want to define an intervalle in which a
# double is converted to the same float. Let's find out about it length.


def find_interval(x):
    dx = numpy.abs(x - numpy.float32(x))  # usually not zero
    dx /= 100
    f = numpy.float32(x)
    x1 = x
    while numpy.float32(x1) == f:
        x1 -= dx
    x2 = x
    while numpy.float32(x2) == f:
        x2 += dx
    return x1 + dx, x2 - dx


length = numpy.zeros((2000,))
for i in range(length.shape[0]):
    x = rnd[i]
    x1, x2 = find_interval(x)
    length[i] = x2 - x1

min(length), max(length)


######################################

plt.hist(length, bins=50)


######################################
# So we can approximate this interval by something like this:


ql = numpy.sort(length)[int(length.shape[0] * 0.8)]
ql


######################################
# An answer to the initial question
# =================================
#
# Let's estimate
# :math:`\mathbb{P}\left(x_{64} < y_{64} \Longrightarrow x_{32}
# < y_{32} \; | \; |x-y| \leqslant d\right)` ?


def inf_strict(x, y):
    f1 = x < y
    f2 = numpy.float32(x) < numpy.float32(y)
    return f1, f2


def count_events(fct):
    rows = []
    for di in range(1, 1001):
        d = di * ql / 100
        total = 0
        ok = 0
        rnd = numpy.random.random((2000 * 3,))
        for i in range(0, rnd.shape[0], 3):
            s = -1 if rnd[i + 2] < 0.5 else 1
            x, y = rnd[i], rnd[i] + rnd[i + 1] * d * s
            f1, f2 = fct(x, y)
            if f1:
                total += 1
                if f2:
                    ok += 1
        if (di + 10) % 100 == 0:
            print(di, d, ":", ok, total)
        rows.append(dict(d=d, ratio=ok * 1.0 / total, total=total))

    return pandas.DataFrame(rows)


df = count_events(inf_strict)
df.head()


######################################

df.plot(x="d", y="ratio")


######################################

df.plot(x="d", y="ratio", logx=True)


######################################
# An answer to a similar question: what about not strict comparison?
# ==================================================================
#
# Let's estimate
# :math:`\mathbb{P}\left(x_{64} \leqslant y_{64} \Longrightarrow x_{32}
# \leqslant y_{32} \; | \; |x-y| \leqslant d\right)` ?


def inf_equal(x, y):
    f1 = x <= y
    f2 = numpy.float32(x) <= numpy.float32(y)
    return f1, f2


df2 = count_events(inf_equal)
df2.head()


######################################
#

ax = df.plot(x="d", y="ratio", logx=True, label="<")
df2.plot(x="d", y="ratio", logx=True, label="<=", ax=ax)


######################################
#


def sup_strict(x, y):
    f1 = x > y
    f2 = numpy.float32(x) > numpy.float32(y)
    return f1, f2


df3 = count_events(sup_strict)
df3.head()


######################################
#

ax = df.plot(x="d", y="ratio", logx=True, label="<")
df2.plot(x="d", y="ratio", logx=True, label="<=", ax=ax)
df3.plot(x="d", y="ratio", logx=True, label=">", ax=ax)


######################################
#


def sup_equal(x, y):
    f1 = x >= y
    f2 = numpy.float32(x) >= numpy.float32(y)
    return f1, f2


df4 = count_events(sup_equal)
df4.head()


######################################
#

ax = df.plot(x="d", y="ratio", logx=True, label="<")
df2.plot(x="d", y="ratio", logx=True, label="<=", ax=ax)
df3.plot(x="d", y="ratio", logx=True, label=">", ax=ax)
df4.plot(x="d", y="ratio", logx=True, label=">=", ax=ax)


######################################
#


def inf_strict_neg(x, y):
    f1 = (-x) >= (-y)
    f2 = (-numpy.float32(x)) >= (-numpy.float32(y))
    return f1, f2


dfn = count_events(inf_strict_neg)
dfn.head()


######################################
#

ax = df.plot(x="d", y="ratio", logx=True, label="<")
dfn.plot(x="d", y="ratio", logx=True, label="-1 x >=", ax=ax)


######################################
# Conclusion
# ==========
#
# The result is expected. As soon as two float are rounded to the same value,
# the strict inequality no longer holds. However, if you need to write a
# code which has to handle double and float (in a template for example),
# you should use not strict inequalities. It is easier to compare the results
# but you should read some article like `Is < faster than <=?
# <https://stackoverflow.com/questions/12135518/is-faster-than>`_.
# According to
# `Processing costs of non-strict versus strict comparison
# <http://www.crcummins.com/CRCProcessing.pdf>`_, ``<`` is 5-10% faster than ``<=``.
