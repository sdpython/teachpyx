import os
import subprocess
import sys
from typing import List, Optional, Tuple


def find_in_PATH(prog: str) -> Optional[str]:
    """
    Looks into every path mentioned in ``%PATH%`` a specific file,
    it raises an exception if not found.

    :param prog: program to look for
    :return: path
    """
    sep = ";" if sys.platform.startswith("win") else ":"
    path = os.environ["PATH"]
    for p in path.split(sep):
        f = os.path.join(p, prog)
        if os.path.exists(f):
            return p
    return None


def find_graphviz_dot(exc: bool = True) -> str:
    """
    Determines the path to graphviz (on Windows),
    the function tests the existence of versions 34 to 45
    assuming it was installed in a standard folder:
    ``C:\\Program Files\\MiKTeX 2.9\\miktex\\bin\\x64``.

    :param exc: raise exception of be silent
    :return: path to dot
    :raises FileNotFoundError: if graphviz not found
    """
    if sys.platform.startswith("win"):
        version = list(range(34, 60))
        version.extend([f"{v}.1" for v in version])
        for v in version:
            graphviz_dot = f"C:\\Program Files (x86)\\Graphviz2.{v}\\bin\\dot.exe"
            if os.path.exists(graphviz_dot):
                return graphviz_dot
        extra = ["build/update_modules/Graphviz/bin"]
        for ext in extra:
            graphviz_dot = os.path.join(ext, "dot.exe")
            if os.path.exists(graphviz_dot):
                return graphviz_dot
        p = find_in_PATH("dot.exe")
        if p is None:
            if exc:
                raise FileNotFoundError(
                    f"Unable to find graphviz, look into paths such as {graphviz_dot}."
                )
            return None
        return os.path.join(p, "dot.exe")
    # linux
    return "dot"


def run_subprocess(
    args: List[str],
    cwd: Optional[str] = None,
):
    assert not isinstance(
        args, str
    ), "args should be a sequence of strings, not a string."

    p = subprocess.Popen(
        args,
        cwd=cwd,
        shell=False,
        env=os.environ,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    raise_exception = False
    output = ""
    while True:
        output = p.stdout.readline().decode(errors="ignore")
        if output == "" and p.poll() is not None:
            break
        if output:
            if (
                "fatal error" in output
                or "CMake Error" in output
                or "gmake: ***" in output
                or "): error C" in output
                or ": error: " in output
            ):
                raise_exception = True
    p.poll()
    p.stdout.close()
    if raise_exception:
        raise RuntimeError(
            "An error was found in the output. The build is stopped.\n{output}"
        )
    return output


def run_graphviz(filename: str, image: str, engine: str = "dot") -> str:
    """
    Run :epkg:`Graphviz`.

    :param filename: filename which contains the graph definition
    :param image: output image
    :param engine: *dot* or *neato*
    :return: output of graphviz
    """
    ext = os.path.splitext(image)[-1]
    if ext != ".png":
        raise RuntimeError(f"Extension of {image!r} should be '.png' not {ext!r}.")
    if sys.platform.startswith("win"):
        bin_ = os.path.dirname(find_graphviz_dot())
        # if bin not in os.environ["PATH"]:
        #    os.environ["PATH"] = os.environ["PATH"] + ";" + bin
        exe = os.path.join(bin_, engine)
    else:
        exe = engine
    if os.path.exists(image):
        os.remove(image)
    output = run_subprocess([exe, "-Tpng", filename, "-o", image])
    assert os.path.exists(image), f"Graphviz failed due to {output}"
    return output


def edges2gv(vertices: List[Tuple[int, str]], edges: List[Tuple[int, int, str]]) -> str:
    """
    Converts a graph into a :epkg:`Graphviz` file format.

    :param edges: see below
    :param vertices: see below
    :return: gv format

    The function creates a file ``<image>.gv``.

    .. runpython::
        :showcode:

        from teachpyx.tools.graphviz_helper import edges2gv
        gv = edges2gv([(1, "eee", "red")],
                      [(1, 2, "blue"), (3, 4), (1, 3)])
        print(gv)
    """
    memovertex = {}
    for v in vertices:
        if isinstance(v, tuple):
            if len(v) == 1:
                memovertex[v[0]] = None
            else:
                memovertex[v[0]] = v[1:]
        else:
            memovertex[v] = None
    for edge in edges:
        i, j = edge[:2]
        if i not in memovertex:
            memovertex[i] = None
        if j not in memovertex:
            memovertex[j] = None

    li = ["digraph{"]
    for k, v in memovertex.items():
        if v is None:
            li.append(f"{k} ;")
        elif len(v) == 1:
            li.append(f'"{k}" [label="{v[0]}"];')
        elif len(v) == 2:
            li.append(f'"{k}" [label="{v[0]}",fillcolor={v[1]},color={v[1]}];')
        else:
            raise ValueError(f"Unable to understand {v}.")

    for edge in edges:
        i, j = edge[:2]
        if len(edge) == 2:
            li.append(f'"{i}" -> "{j}";')
        elif len(edge) == 3:
            li.append(f'"{i}" -> "{j}" [label="{edge[2]}"];')
        elif len(edge) == 4:
            li.append(f'"{i}" -> "{j}" [label="{edge[2]}",color={edge[3]}];')
        else:
            raise ValueError(f"Unable to understand {edge}.")
    li.append("}")

    text = "\n".join(li)
    return text


def draw_graph_graphviz(
    vertices: List[Tuple[int, str]],
    edges: List[Tuple[int, int, str]],
    image: Optional[str] = None,
    engine: str = "dot",
) -> str:
    """
    Draws a graph using :epkg:`Graphviz`.

    :param edges: see below
    :param vertices: see below
    :param image: output image, None, just returns the output
    :param engine: *dot* or *neato*
    :return: :epkg:`Graphviz` output or
        the dot text if *image* is None

    The function creates a file ``<image>.gv`` if *image* is not None.

    ::

        edges = [(1,2, label, color), (3,4), (1,3)]  # edges list
        vertices = [(1, label, color), (2)]  # vertices list
        image = "image_name.png"

    """
    text = edges2gv(vertices, edges)
    if image is None:
        return text
    filename = image + ".gv"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

    assert os.path.exists(
        filename
    ), f"File {filename!r} cannot be created to store the graph."
    out = run_graphviz(filename, image, engine=engine)
    if not os.path.exists(image):
        raise FileNotFoundError(f"Graphviz failed with no reason, {image!r} not found.")
    return out
