import os
import sys
from sphinx_runpython.conf_helper import has_dvipng, has_dvisvgm
from sphinx_runpython.github_link import make_linkcode_resolve
from teachpyx import __version__


extensions = [
    "nbsphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.githubpages",
    "sphinx.ext.ifconfig",
    "sphinx.ext.intersphinx",
    "sphinx.ext.linkcode",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx_gallery.gen_gallery",
    "sphinx_issues",
    "sphinx_runpython.blocdefs.sphinx_exref_extension",
    "sphinx_runpython.blocdefs.sphinx_faqref_extension",
    "sphinx_runpython.blocdefs.sphinx_mathdef_extension",
    "sphinx_runpython.epkg",
    "sphinx_runpython.gdot",
    "sphinx_runpython.runpython",
    "sphinxcontrib.blockdiag",
    "matplotlib.sphinxext.plot_directive",
]

if has_dvisvgm():
    extensions.append("sphinx.ext.imgmath")
    imgmath_image_format = "svg"
elif has_dvipng():
    extensions.append("sphinx.ext.pngmath")
    imgmath_image_format = "png"
else:
    extensions.append("sphinx.ext.mathjax")

templates_path = ["_templates"]
html_logo = "_static/project_ico.png"
source_suffix = ".rst"
master_doc = "index"
project = "teachpyx"
copyright = "2016-2025, Xavier Dupré"
author = "Xavier Dupré"
version = __version__
release = __version__
language = "fr"
exclude_patterns = ["auto_examples/prog/*.ipynb", "auto_examples/ml/*.ipynb"]
pygments_style = "sphinx"
todo_include_todos = True
nbsphinx_execute = "never"

html_theme = "furo"
html_theme_path = ["_static"]
html_theme_options = {}
html_sourcelink_suffix = ""
html_static_path = ["_static"]

issues_github_path = "sdpython/teachpyx"

nbsphinx_prolog = """

.. _nbl-{{ env.doc2path(env.docname, base=None).replace("/", "-").split(".")[0] }}:

"""

nbsphinx_epilog = """
----

`Notebook on github <https://github.com/sdpython/teachpyx/tree/main/_doc/{{ env.doc2path(env.docname, base=None) }}>`_
"""

# The following is used by sphinx.ext.linkcode to provide links to github
linkcode_resolve = make_linkcode_resolve(
    "teachpyx",
    (
        "https://github.com/sdpython/teachpyx/"
        "blob/{revision}/{package}/"
        "{path}#L{lineno}"
    ),
)

latex_elements = {
    "papersize": "a4",
    "pointsize": "10pt",
    "title": project,
}

mathjax3_config = {"chtml": {"displayAlign": "left"}}

intersphinx_mapping = {
    "IPython": ("https://ipython.readthedocs.io/en/stable/", None),
    "matplotlib": ("https://matplotlib.org/", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "onnx": ("https://onnx.ai/onnx/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "python": (f"https://docs.python.org/{sys.version_info.major}", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    "skl2onnx": ("https://onnx.ai/sklearn-onnx/", None),
    "sklearn": ("https://scikit-learn.org/stable/", None),
    "skrub": ("https://skrub-data.org/stable/", None),
    "torch": ("https://pytorch.org/docs/stable/", None),
}

# Check intersphinx reference targets exist
nitpicky = True
# See also scikit-learn/scikit-learn#26761
nitpick_ignore = [
    ("py:class", "False"),
    ("py:class", "True"),
    ("py:class", "pipeline.Pipeline"),
    ("py:class", "default=sklearn.utils.metadata_routing.UNCHANGED"),
]

sphinx_gallery_conf = {
    # path to your examples scripts
    "examples_dirs": os.path.join(os.path.dirname(__file__), "examples"),
    # path where to save gallery generated examples
    "gallery_dirs": "auto_examples",
    "ignore_pattern": "schema_pb.*[.]py",
}

# next

preamble = """
%%% \\usepackage{etex}
%%% \\usepackage{fixltx2e} % LaTeX patches, \\textsubscript
%%% \\usepackage{cmap} % fix search and cut-and-paste in Acrobat
%%% \\usepackage[raccourcis]{fast-diagram}
%%% \\usepackage{titlesec}
%%% \\usepackage{amsmath}
%%% \\usepackage{amssymb}
%%% \\usepackage{amsfonts}
%%% \\usepackage{graphics}
%%% \\usepackage{epic}
%%% \\usepackage{eepic}
%%% \\usepackage{pict2e}
%%% Redefined titleformat
%%% \\setlength{\\parindent}{0cm}
%%% \\setlength{\\parskip}{1ex plus 0.5ex minus 0.2ex}
\\newcommand{\\hsp}{\\hspace{20pt}}
\\newcommand{\\acc}[1]{\\left\\{#1\\right\\}}
\\newcommand{\\cro}[1]{\\left[#1\\right]}
\\newcommand{\\pa}[1]{\\left(#1\\right)}
\\newcommand{\\R}{\\mathbb{R}}
\\newcommand{\\HRule}{\\rule{\\linewidth}{0.5mm}}
%%% \\titleformat{\\chapter}[hang]{\\Huge\\bfseries\\sffamily}{\\thechapter\\hsp}{0pt}{\\Huge\\bfseries\\sffamily}
%%% \\usepackage[all]{xy}
\\newcommand{\\vecteur}[2]{\\pa{#1,\\dots,#2}}
\\newcommand{\\N}[0]{\\mathbb{N}}
\\newcommand{\\indicatrice}[1]{ {1\\!\\!1}_{\\acc{#1}} }
\\newcommand{\\infegal}[0]{\\leqslant}
\\newcommand{\\supegal}[0]{\\geqslant}
\\newcommand{\\ensemble}[2]{\\acc{#1,\\dots,#2}}
\\newcommand{\\fleche}[1]{\\overrightarrow{ #1 }}
\\newcommand{\\intervalle}[2]{\\left\\{#1,\\cdots,#2\\right\\}}
\\newcommand{\\independant}[0]{\\perp \\!\\!\\! \\perp}
\\newcommand{\\esp}{\\mathbb{E}}
\\newcommand{\\espf}[2]{\\mathbb{E}_{#1}\\pa{#2}}
\\newcommand{\\var}{\\mathbb{V}}
\\newcommand{\\pr}[1]{\\mathbb{P}\\pa{#1}}
\\newcommand{\\loi}[0]{{\\cal L}}
\\newcommand{\\vecteurno}[2]{#1,\\dots,#2}
\\newcommand{\\norm}[1]{\\left\\Vert#1\\right\\Vert}
\\newcommand{\\norme}[1]{\\left\\Vert#1\\right\\Vert}
\\newcommand{\\scal}[2]{\\left<#1,#2\\right>}
\\newcommand{\\dans}[0]{\\rightarrow}
\\newcommand{\\partialfrac}[2]{\\frac{\\partial #1}{\\partial #2}}
\\newcommand{\\partialdfrac}[2]{\\dfrac{\\partial #1}{\\partial #2}}
\\newcommand{\\trace}[1]{tr\\pa{#1}}
\\newcommand{\\sac}[0]{|}
\\newcommand{\\abs}[1]{\\left|#1\\right|}
\\newcommand{\\loinormale}[2]{{\\cal N} \\pa{#1,#2}}
\\newcommand{\\loibinomialea}[1]{{\\cal B} \\pa{#1}}
\\newcommand{\\loibinomiale}[2]{{\\cal B} \\pa{#1,#2}}
\\newcommand{\\loimultinomiale}[1]{{\\cal M} \\pa{#1}}
\\newcommand{\\variance}[1]{\\mathbb{V}\\pa{#1}}
\\newcommand{\\intf}[1]{\\left\\lfloor #1 \\right\\rfloor}
"""

epkg_dictionary = {
    "_ipython_display_": "https://ipython.readthedocs.io/en/stable/config/integrating.html?highlight=Integrating%20",
    "_repr_html_": "https://ipython.readthedocs.io/en/stable/config/integrating.html#custom-methods",
    "Algorithme de Strassen": "https://fr.wikipedia.org/wiki/Algorithme_de_Strassen",
    "algorithme de Strassen": "https://fr.wikipedia.org/wiki/Algorithme_de_Strassen",
    "ACP": "https://fr.wikipedia.org/wiki/Analyse_en_composantes_principales",
    "AESA": "https://tavianator.com/aesa/",
    "algorithme": "https://fr.wikipedia.org/wiki/Algorithme",
    "algorithmes de tri": "https://fr.wikipedia.org/wiki/Algorithme_de_tri",
    "algorithmes numériques": "https://fr.wikipedia.org/wiki/Numerical_Recipes",
    "API REST": "https://fr.wikipedia.org/wiki/Representational_state_transfer",
    "Anaconda": "https://www.anaconda.com/",
    "ApproximateNMFPredictor": "https://sdpython.github.io/doc/mlinsights/dev/api/mlmodel.html#approximatenmfpredictor",
    "AUC": "https://en.wikipedia.org/wiki/Receiver_operating_characteristic#Area_under_the_curve",
    "Awesome Python": "https://awesome-python.com/",
    "B+ tree": "https://en.wikipedia.org/wiki/B%2B_tree",
    "BLAS": "https://www.netlib.org/blas/",
    "blockdiag": "https://github.com/blockdiag/blockdiag",
    "Branch and Bound": "https://en.wikipedia.org/wiki/Branch_and_bound",
    "bytearray": "https://docs.python.org/3/library/functions.html#bytearray",
    "C++": "https://fr.wikipedia.org/wiki/C%2B%2B",
    "cloudpickle": "https://github.com/cloudpipe/cloudpickle",
    "Bresenham": "https://fr.wikipedia.org/wiki/Algorithme_de_trac%C3%A9_de_segment_de_Bresenham",
    "category_encoders": "https://contrib.scikit-learn.org/category_encoders/",
    "copy": "https://docs.python.org/3/library/copy.html?highlight=copy#copy.copy",
    "cProfile.Profile": "https://docs.python.org/3/library/profile.html#profile.Profile",
    "Custom Criterion for DecisionTreeRegressor": "https://sdpython.github.io/doc/mlinsights/dev/auto_examples/plot_piecewise_linear_regression_criterion.html",
    "cython": "https://cython.org/",
    "DecisionTreeClassifier": "https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html",
    "DecisionTreeRegressor optimized for Linear Regression": "https://sdpython.github.io/doc/mlinsights/dev/auto_examples/plot_piecewise_linear_regression_criterion.html",
    "deepcopy": "https://docs.python.org/3/library/copy.html?highlight=copy#copy.deepcopy",
    "dill": "https://dill.readthedocs.io/en/latest/",
    "dir": "https://docs.python.org/3/library/functions.html?highlight=dir#dir",
    "dot": "https://fr.wikipedia.org/wiki/DOT_(langage)",
    "DOT": "https://fr.wikipedia.org/wiki/DOT_(langage)",
    "encoding": "https://fr.wikipedia.org/wiki/Codage_des_caract%C3%A8res",
    "eval": "https://docs.python.org/3/library/functions.html?highlight=id#eval",
    "Excel": "https://fr.wikipedia.org/wiki/Microsoft_Excel",
    "folium": "https://python-visualization.github.io/folium/latest/",
    "format": "https://pyformat.info/",
    "format style": "https://pyformat.info/",
    "garbage collector": "https://fr.wikipedia.org/wiki/Ramasse-miettes_(informatique)",
    "Graphviz": "https://graphviz.org/",
    "Holm-Bonferroni method": "https://en.wikipedia.org/wiki/Holm%E2%80%93Bonferroni_method",
    "HTML": "https://fr.wikipedia.org/wiki/Hypertext_Markup_Language",
    "ICML 2016": "https://icml.cc/2016/index.html",
    "indentation": "https://fr.wikipedia.org/wiki/Style_d%27indentation",
    "issubclass": "https://docs.python.org/3/library/functions.html?highlight=issubclass#issubclass",
    "joblib": "https://joblib.readthedocs.io/en/stable/",
    "JSON": "https://en.wikipedia.org/wiki/JSON",
    "jupyter": "https://jupyter.org/",
    "KMeans": "https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html",
    "LAESA": "https://tavianator.com/aesa/",
    "LAPACK": "http://www.netlib.org/lapack/",
    "librosa": "https://librosa.org/doc/latest/index.html",
    "lifelines": "https://lifelines.readthedocs.io/en/latest/",
    "matplotlib": "https://matplotlib.org/",
    "Method Resolution Order": "https://www.python.org/download/releases/2.3/mro/",
    "miniconda": "https://docs.conda.io/en/latest/miniconda.html",
    "Miniconda": "https://docs.conda.io/en/latest/miniconda.html",
    "mlinsights": "https://sdpython.github.io/doc/mlinsights/dev/",
    "mlstatpy": "https://sdpython.github.io/doc/mlstatpy/dev/",
    "NP-complet": "https://fr.wikipedia.org/wiki/Probl%C3%A8me_NP-complet",
    "neato": "https://www.graphviz.org/pdf/neatoguide.pdf",
    "notebook": "https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html#notebook-document",
    "numpy": (
        "https://www.numpy.org/",
        ("https://docs.scipy.org/doc/numpy/reference/generated/numpy.{0}.html", 1),
        ("https://docs.scipy.org/doc/numpy/reference/generated/numpy.{0}.{1}.html", 2),
    ),
    "OneHotEncoder": "https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html",
    "OpenMP": "https://www.openmp.org/",
    "orange3": "https://orangedatamining.com/",
    "pandas": (
        "https://pandas.pydata.org/pandas-docs/stable/",
        ("https://pandas.pydata.org/pandas-docs/stable/generated/pandas.{0}.html", 1),
        (
            "https://pandas.pydata.org/pandas-docs/stable/generated/pandas.{0}.{1}.html",
            2,
        ),
    ),
    "pandas-profiling": "https://docs.profiling.ydata.ai/latest/",
    "PiecewiseTreeRegressor": "https://sdpython.github.io/doc/mlinsights/dev/api/mlmodel_tree.html#piecewisetreeregressor",
    "Pillow": "https://pillow.readthedocs.io/en/stable/",
    "pip": "https://pip.pypa.io/en/stable/",
    "pipeline": "https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html",
    "plotly": "https://plotly.com/python/",
    "Predictable t-SNE": "https://sdpython.github.io/doc/mlinsights/dev/auto_examples/plot_predictable_tsne.html",
    "printf-style String Formatting": "https://docs.python.org/3/library/stdtypes.html#old-string-formatting",
    "programmation impérative": "https://fr.wikipedia.org/wiki/Programmation_imp%C3%A9rative",
    "programmation fonctionnelle": "https://fr.wikipedia.org/wiki/Programmation_fonctionnelle",
    "prophet": "https://facebook.github.io/prophet/docs/installation.html",
    "protobuf": "https://protobuf.dev/",
    "pygame": "https://www.pygame.org/",
    "pyinstrument": "https://github.com/joerick/pyinstrument",
    "pyflux": "https://pyflux.readthedocs.io/en/latest/",
    "pylint": "https://github.com/pylint-dev/pylint",
    "pypi": "https://pypi.org/",
    "PyPi": "https://pypi.org/",
    "python": "https://www.python.org/",
    "Python": "https://www.python.org/",
    "QuantileLinearRegression": "https://sdpython.github.io/doc/mlinsights/dev/api/mlmodel.html#quantilelinearregression",
    "R-tree": "https://en.wikipedia.org/wiki/R-tree",
    "R* tree": "https://en.wikipedia.org/wiki/R*_tree",
    "range": "https://docs.python.org/3/library/functions.html?highlight=map#func-range",
    "Regression with confidence interval": "https://sdpython.github.io/doc/mlinsights/dev/auto_examples/plot_regression_confidence_interval.html",
    "relu": "https://en.wikipedia.org/wiki/Rectifier_(neural_networks)",
    "ROC": "https://fr.wikipedia.org/wiki/Courbe_ROC",
    "rst": "https://fr.wikipedia.org/wiki/ReStructuredText",
    "scikit-image": "https://scikit-image.org/",
    "scikit-learn": "https://scikit-learn.org/stable/index.html",
    "scikit-survival": "https://scikit-survival.readthedocs.io/en/stable/index.html",
    "scipy": "https://scipy.org/",
    "sérialisation": "https://fr.wikipedia.org/wiki/S%C3%A9rialisation",
    "skforecast": "https://skforecast.org/",
    "sklearn": "https://scikit-learn.org/stable/index.html",
    "sklearn-onnx": "https://onnx.ai/sklearn-onnx/",
    "sktime": "https://www.sktime.net/en/stable/index.html",
    "skrub": "https://skrub-data.org/stable/",
    "SQLite": "https://www.sqlite.org/",
    "statsmodels": "http://www.statsmodels.org/stable/index.html",
    "SVD": "https://fr.wikipedia.org/wiki/D%C3%A9composition_en_valeurs_singuli%C3%A8res",
    "sys.modules": "https://docs.python.org/3/library/sys.html?highlight=modules#sys.modules",
    "sys.path": "https://docs.python.org/3/library/sys.html#sys.path",
    "teachpyx": "https://sdpython.github.io/doc/teachpyx/dev/",
    "threads": "https://fr.wikipedia.org/wiki/Thread_(informatique)",
    "tkinter": "https://docs.python.org/3/library/tk.html",
    "tqdm": "https://tqdm.github.io/",
    "ultrajson": "https://github.com/ultrajson/ultrajson",
    "ujson": "https://github.com/ultrajson/ultrajson",
    "Visual Studio Code": "https://code.visualstudio.com/",
    "Visualize a scikit-learn pipeline": "https://sdpython.github.io/doc/mlinsights/dev/auto_examples/plot_visualize_pipeline.html",
    "viz.js": "https://github.com/mdaines/viz-js",
    "X-tree": "https://en.wikipedia.org/wiki/X-tree",
    "XML": "https://fr.wikipedia.org/wiki/Extensible_Markup_Language",
    "wikipedia dumps": "https://dumps.wikimedia.org/frwiki/latest/",
    "wxPython": "https://wxpython.org/",
}

epkg_dictionary.update(
    {
        "tkinter.Button": "https://tkdocs.com/widgets/button.html",
        "tkinter.Button.config": "https://tkdocs.com/widgets/button.html",
        "tkinter.Canvas": "https://tkdocs.com/tutorial/canvas.html",
        "tkinter.Canvas.create_line": "https://tkdocs.com/tutorial/canvas.html",
        "tkinter.Canvas.create_rectangle": "https://tkdocs.com/tutorial/canvas.html",
        "tkinter.Canvas.create_text": "https://tkdocs.com/tutorial/canvas.html",
        "tkinter.CheckButton": "https://tkdocs.com/tutorial/widgets.html#checkbutton",
        "tkinter.CheckButton.config": "https://tkdocs.com/tutorial/widgets.html#checkbutton",
        "tkinter.Entry": "https://tkdocs.com/pyref/entry.html",
        "tkinter.Entry.delete": "https://tkdocs.com/pyref/entry.html",
        "tkinter.Entry.config": "https://tkdocs.com/pyref/entry.html",
        "tkinter.Entry.get": "https://tkdocs.com/pyref/entry.html",
        "tkinter.Entry.insert": "https://tkdocs.com/pyref/entry.html",
        "tkinter.Event": "https://tkdocs.com/tutorial/eventloop.html",
        "tkinter.Frame": "https://tkdocs.com/tutorial/widgets.html#frame",
        "tkinter.filedialog": "https://docs.python.org/3/library/dialog.html#module-tkinter.filedialog",
        "tkinter.IntVar": "https://tkdocs.com/pyref/intvar.html",
        "tkinter.Label": "https://tkdocs.com/tutorial/widgets.html#label",
        "tkinter.Label.after_cancel": "https://tkdocs.com/tutorial/widgets.html#label",
        "tkinter.ListBox": "https://tkdocs.com/tutorial/widgets.html#listbox",
        "tkinter.ListBox.config": "https://tkdocs.com/tutorial/widgets.html#listbox",
        "tkinter.ListBox.curselection": "https://tkdocs.com/tutorial/widgets.html#listbox",
        "tkinter.ListBox.delete": "https://tkdocs.com/tutorial/widgets.html#listbox",
        "tkinter.ListBox.get": "https://tkdocs.com/tutorial/widgets.html#listbox",
        "tkinter.ListBox.insert": "https://tkdocs.com/tutorial/widgets.html#listbox",
        "tkinter.ListBox.itemconfig": "https://tkdocs.com/tutorial/widgets.html#listbox",
        "tkinter.ListBox.select_all": "https://tkdocs.com/tutorial/widgets.html#listbox",
        "tkinter.ListBox.select_clear": "https://tkdocs.com/tutorial/widgets.html#listbox",
        "tkinter.ListBox.select_get": "https://tkdocs.com/tutorial/widgets.html#listbox",
        "tkinter.ListBox.select_set": "https://tkdocs.com/tutorial/widgets.html#listbox",
        "tkinter.Menu": "https://tkdocs.com/tutorial/widgets.html#menu",
        "tkinter.Menu.add_command": "https://tkdocs.com/tutorial/widgets.html#menu",
        "tkinter.Menu.add_cascade": "https://tkdocs.com/tutorial/widgets.html#menu",
        "tkinter.Menu.delete": "https://tkdocs.com/tutorial/widgets.html#menu",
        "tkinter.RadioButton": "https://tkdocs.com/tutorial/widgets.html#radiobutton",
        "tkinter.Text": "https://tkdocs.com/tutorial/text.html",
        "tkinter.Text.config": "https://tkdocs.com/tutorial/text.html",
        "tkinter.Text.delete": "https://tkdocs.com/tutorial/text.html",
        "tkinter.Text.get": "https://tkdocs.com/tutorial/text.html",
        "tkinter.Text.insert": "https://tkdocs.com/tutorial/text.html",
        "tkinter.Toplevel": "https://tkdocs.com/pyref/toplevel.html",
        "tkinter.Toplevel.deiconify": "https://tkdocs.com/pyref/toplevel.html",
        "tkinter.Toplevel.destroy": "https://tkdocs.com/pyref/toplevel.html",
        "tkinter.Toplevel.geometry": "https://tkdocs.com/pyref/toplevel.html",
        "tkinter.Toplevel.iconify": "https://tkdocs.com/pyref/toplevel.html",
        "tkinter.Toplevel.resizable": "https://tkdocs.com/pyref/toplevel.html",
        "tkinter.Toplevel.title": "https://tkdocs.com/pyref/toplevel.html",
        "tkinter.Toplevel.withdraw": "https://tkdocs.com/pyref/toplevel.html",
        "tkinter.ttk.Combobox": "https://tkdocs.com/pyref/ttk_combobox.html",
        "tkinter.ttk.Notebook": "https://tkdocs.com/pyref/ttk_notebook.html",
        "tkinter.ttk.Progressbar": "https://tkdocs.com/pyref/ttk_progressbar.html",
        "tkinter.ttk.Treeview": "https://tkdocs.com/pyref/ttk_treeview.html",
        "tkinter.Widget.bind": "https://tkdocs.com/tutorial/index.html",
        "tkinter.Widget.bind_all": "https://tkdocs.com/tutorial/index.html",
        "tkinter.Widget.focus": "https://tkdocs.com/tutorial/index.html",
        "tkinter.Widget.focus_set": "https://tkdocs.com/tutorial/index.html",
        "tkinter.Widget.grid": "https://tkdocs.com/tutorial/index.html",
        "tkinter.Widget.grid_forget": "https://tkdocs.com/tutorial/index.html",
        "tkinter.Widget.pack": "https://tkdocs.com/tutorial/index.html",
        "tkinter.Widget.pack_forget": "https://tkdocs.com/tutorial/index.html",
        "tkinter.Widget.place": "https://tkdocs.com/tutorial/index.html",
        "tkinter.Widget.place_forget": "https://tkdocs.com/tutorial/index.html",
        "tkinter.Widget.unbind": "https://tkdocs.com/tutorial/index.html",
        "tkinter.Widget.unbind_all": "https://tkdocs.com/tutorial/index.html",
    }
)

epkg_dictionary.update(
    {
        "An Effective Implementation of the Lin-Kernighan Traveling Salesman Heuristic": "http://www.akira.ruc.dk/~keld/research/LKH/LKH-2.0/DOC/LKH_REPORT.pdf",
        "backtest": "https://en.wikipedia.org/wiki/Backtesting",
        "Trend Following": "https://en.wikipedia.org/wiki/Trend_following",
        "pair trading": "https://en.wikipedia.org/wiki/Pairs_trade",
    }
)

epkg_dictionary.update(
    {
        "cartopy": "https://scitools.org.uk/cartopy/docs/latest/",
        "catboost": "https://catboost.ai/",
        "csv": "https://fr.wikipedia.org/wiki/Comma-separated_values",
        "Enedis": "https://data.enedis.fr/",
        "fonction": "https://fr.wikipedia.org/wiki/Fonction_(math%C3%A9matiques)",
        "fonction continue": "https://fr.wikipedia.org/wiki/Continuit%C3%A9_(math%C3%A9matiques)",
        "fortran": "https://en.wikipedia.org/wiki/Fortran",
        "GEOFLA": "https://www.data.gouv.fr/en/datasets/geofla-r/",
        "lightgtbm": "https://lightgbm.readthedocs.io/en/stable/",
        "machine learning": "https://en.wikipedia.org/wiki/Machine_learning",
        "matrice de confusion": "https://fr.wikipedia.org/wiki/Matrice_de_confusion",
        "nuage de points": "https://fr.wikipedia.org/wiki/Nuage_de_points_(statistique)",
        "pytorch": "https://pytorch.org/",
        "R": "https://www.r-project.org/",
        "recherche dichotomique": "https://fr.wikipedia.org/wiki/Recherche_dichotomique",
        "seaborn": "https://seaborn.pydata.org/",
        "UCI": "https://archive.ics.uci.edu/datasets",
        "variable aléatoire": "https://fr.wikipedia.org/wiki/Variable_al%C3%A9atoire",
        "voyageur de commerce": "https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce",
        "xgboost": "https://xgboost.readthedocs.io/en/stable/",
    }
)

imgmath_latex_preamble = preamble
latex_elements["preamble"] = imgmath_latex_preamble
