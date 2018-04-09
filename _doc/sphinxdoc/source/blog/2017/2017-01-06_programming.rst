
.. blogpost::
    :title: I hate programming sometimes
    :keywords:
    :date: 2017-01-06
    :categories: weird

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
