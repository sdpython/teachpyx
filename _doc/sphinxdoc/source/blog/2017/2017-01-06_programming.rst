
.. blogpost::
    :title: I hate programming sometimes
    :keywords:
    :date: 2017-01-06
    :categories: weird

    This is the kind of example I never imagined
    maybe because I trust too much the code I write
    and I can't see it fail for something like what
    follows.

    .. runpython::
        :showcode:
        :nopep8:

        s1 = 'İ'
        s2 = s1.lower()
        print(s1, s2)
        print(len(s1), len(s2))

        b = bytes(s2, "utf-8")
        print(chr(b[0]), chr(b[1]))

    Do you believe it?

    The length of a lower case character is longer.

    I need a drink.
