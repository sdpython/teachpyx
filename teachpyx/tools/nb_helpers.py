import uuid
import urllib.request as liburl
import urllib.error as liberror
from typing import List, Optional, Tuple
from IPython.display import display_html, display_javascript


class UrlNotFoundError(liberror.URLError):
    """
    Raised when a url does not exist.
    """

    def __init__(self, url, code):
        liberror.URLError.__init__(
            self, f"Url not found. Returned code={code} for {url!r}."
        )


class JavascriptScriptError(ValueError):
    """
    Raised when the class does not find what it expects.
    """

    pass


def check_url(url):
    "Checks urls."
    try:
        liburl.urlopen(url)
        return True
    except liberror.HTTPError as e:
        raise UrlNotFoundError(url, e.code) from e
    except liberror.URLError as e:
        raise UrlNotFoundError(url, e.reason) from e
    except Exception as e:
        raise AssertionError(f"Issue with url {url!r}.") from e


class RenderJSRaw:
    """
    Adds :epkg:`javascript` into a noteboook.

    :param script: script
    :param width: width
    :param height: height
    :param style: style (added in ``<style>...</style>``)
    :param divid: id of the div
    :param css: list of css
    :param libs: list of dependencies
    :param only_html: (bool) use only function
        :func:`IPython.display.display_html` and not
        :func:`IPython.display.display_javascript`
        to add javascript to the page.
    :param div_class: class of the section ``div`` which will host the results
        of the javascript
    :param check_urls: by default, check url exists
    """

    def __init__(
        self,
        script: str,
        width: str = "100%",
        height: str = "100%",
        divid: Optional[str] = None,
        css: Optional[List[str]] = None,
        libs: Optional[List[str]] = None,
        style: Optional[str] = None,
        only_html: bool = False,
        div_class: Optional[str] = None,
        check_urls: bool = True,
    ):
        self.script = script
        self.uuid = divid if divid else "M" + str(uuid.uuid4()).replace("-", "")
        if style is None:
            style = ""
            if width is not None and "width" not in style:
                style += f"width:{width};"
            if height is not None and "height" not in style:
                style += f"height:{height};"
            if not style:
                style = None
        else:
            if width is not None and "width" not in style:
                style += f"width:{width};"
            if height is not None and "height" not in style:
                style += f"height:{height};"
        self.style = style
        self.only_html = only_html
        self.div_class = div_class
        if "__ID__" not in script:
            raise JavascriptScriptError(
                f"The sript does not contain any string __ID__. "
                f"It is replaced by the ID value in script:\n{script}"
            )
        self.css, self.libs = self._preprocess_urls(css, libs)
        if check_urls:
            if self.css is not None:
                for c in self.css:
                    check_url(c)
            if self.libs is not None:
                for lib in self.libs:
                    if isinstance(lib, dict):
                        check_url(lib["path"])
                    else:
                        check_url(lib)

    def _preprocess_urls(
        self, css: List[str], libs: List[str]
    ) -> Tuple[List[str], List[str]]:
        """
        :param css: list of css
        :param libs: list of libraries
        :return: tuple (css, libs)
        """
        return css, libs

    def generate_html(self):
        """
        Overloads method :epkg:`_ipython_display_`.

        :return: :class:`IPython.display.HTML`, :class:`IPython.display.Javascript>`
        """
        if self.style:
            style = f' style="{self.style}"'
        else:
            style = ""
        if self.div_class:
            divcl = f' class="{self.div_class}"'
        else:
            divcl = ""
        if self.css:
            css = "".join(
                f'<link rel="stylesheet" href="{c}" type="text/css" />'
                for c in self.css
            )
            ht = (
                f'<div id="{self.uuid}-css">{css}'
                f'<div{divcl} id="{uuid}"{style}></div></div>'
            )
        else:
            ht = (
                f'<div id="{self.uuid}-cont">'
                f'<div{divcl} id="{uuid}"{style}></div></div>'
            )

        script = self.script.replace("__ID__", self.uuid)
        if self.libs:
            names = []
            paths = []
            shims = {}
            args = []
            exports = []
            for lib in self.libs:
                if isinstance(lib, dict):
                    name = lib.get("name", None)
                    if "path" in lib:
                        p = lib["path"]
                        if name is None:
                            name = ".".join((p.split("/")[-1]).split(".")[:-1])
                        path = ".".join(p.split(".")[:-1])
                        paths.append((name, path))
                    else:
                        raise KeyError(f"Unable to find 'path' in {lib!r}.")
                    names.append(name)
                    args.append(name)
                    if "exports" in lib:
                        if name not in shims:
                            shims[name] = {}
                        shims[name]["exports"] = lib["exports"]
                        if isinstance(lib["exports"], list):
                            exports.extend(lib["exports"])
                        else:
                            exports.append(lib["exports"])
                    if "deps" in lib:
                        if name not in shims:
                            shims[name] = {}
                        shims[name]["deps"] = lib["deps"]
                else:
                    names.append(lib)
            if len(names) == 0:
                raise ValueError(
                    "names is empty.\nlibs={0}\npaths={1}"
                    "\nshims={2}\nexports={3}".format(self.libs, paths, shims, exports)
                )
            require = ",".join(f"'{na}'" for na in names)

            config = ["require.config({"]
            if len(paths) > 0:
                config.append("paths:{")
                for name, path in paths:
                    config.append(f"'{name}':'{path}',")
                config.append("},")
            if len(shims) > 0:
                config.append("shim:{")

                def vd(d):
                    "vd"
                    rows = []
                    for k, v in sorted(d.items()):
                        rows.append(
                            "'{0}':{1}".format(
                                k, v if isinstance(v, list) else "'{0}'".format(v)
                            )
                        )
                    return "{%s}" % ",".join(rows)

                for k, v in sorted(shims.items()):
                    config.append(f"'{k}':{vd(v)},")
                config.append("},")
            config.append("});")
            if len(config) > 2:
                prefix = "\n".join(config) + "\n"
            else:
                prefix = ""
            js = prefix + """\nrequire([%s], function(%s) { %s });\n""" % (
                require,
                ",".join(args),
                script,
            )
        else:
            js = script
        if self.only_html:
            ht += f"\n<script>\n{js}\n</script>"
            return ht, None
        return ht, js


class RenderJSObj(RenderJSRaw):
    """
    Renders JS using :epkg:`javascript`.
    """

    def _ipython_display_(self):
        """
        Overloads method :epkg:`_ipython_display_`.
        """
        # if "display" not in dir(ipydisplay):
        #    # Weird bug introduced in IPython 8.0.0
        #    import IPython.core.display_functions
        #    ipydisplay.display = IPython.core.display_functions.display

        ht, js = self.generate_html()
        display_html(ht, raw=True)
        if js is not None:
            display_javascript(js, raw=True)


class RenderJS(RenderJSRaw):
    """
    Renders :epkg:`javascript`, only outputs :epkg:`HTML`.
    """

    def _repr_html_(self):
        """
        Overloads method :epkg:`_repr_html_`.
        """
        ht, js = self.generate_html()
        if js is not None:
            ht += f"\n<script>\n{js}\n</script>\n"
        return ht


class RenderJsDot(RenderJS):
    """
    Renders a graph in a :epkg:`notebook`
    defined in :epkg:`DOT` language
    with :epkg:`viz.js`.

    :param dot: dot
    :param script: script
    :param width: width
    :param height: height
    :param style: style (added in ``<style>...</style>``)
    :param divid: id of the div
    :param only_html: (bool) use only function
        :func:`IPython.display.display_html` and not
        :func:`IPython.display.display_javascript`
        to add javascript to the page.
    :param div_class: class of the section ``div`` which will host the results
        of the javascript
    :param check_urls: by default, check url exists
    """

    def __init__(
        self,
        dot: str,
        width: str = "100%",
        height: str = "100%",
        divid: Optional[str] = None,
        style: Optional[str] = None,
        only_html: bool = True,
        div_class: Optional[str] = None,
        check_urls: bool = True,
    ):
        script = RenderJsDot._build_script(dot)
        libs, css = RenderJsDot._get_libs_css()
        RenderJS.__init__(
            self,
            script,
            width=width,
            height=height,
            divid=divid,
            only_html=only_html,
            div_class=div_class,
            check_urls=True,
            libs=libs,
            css=css,
            style=style,
        )

    @staticmethod
    def _get_libs_css() -> Tuple[List[str], List[str]]:
        """
        Returns the dependencies.

        :return: tuple *(libs, css)*
        """
        libs = [
            "https://sdpython.github.io/js/viz-standalone.js",
            # "https://github.com/mdaines/viz-js/releases/download/v3.1.0%2B1/viz-standalone.js"
        ]
        css = None
        return libs, css

    @staticmethod
    def _build_script(dot):
        """
        Builds the javascript script based wrapping the
        :epkg:`DOT` language.

        :param dot: epkg:`DOT` language
        :return: javascript
        """
        dot = dot.replace('"', '\\"').replace("\n", "\\n")
        script = (
            f'var svgGraph = Viz("{dot}");'
            f'document.getElementById("__ID__").innerHTML = svgGraph;'
        )
        return script
