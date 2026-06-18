
teachpyx.tools.pandas
=====================

Example
-------

.. plot::

    import pandas
    import matplotlib.pyplot as plt
    from teachpyx.tools.pandas import plot_waterfall

    plt.close("all")

    df = pandas.DataFrame({"name": ["A", "B", "C"], "delta": [10, -3, 5]})
    ax, _ = plot_waterfall(df, "delta", "name", total_label="TOTAL")
    ax.set_title("Example waterfall")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.show()

.. automodule:: teachpyx.tools.pandas
    :members:
    :no-undoc-members:
