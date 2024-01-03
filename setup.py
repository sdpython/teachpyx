# coding: utf-8
import os

from setuptools import setup

######################
# beginning of setup
######################


here = os.path.dirname(__file__)
if here == "":
    here = "."
package_data = {
    "teachpyx": ["*.txt"],
    "teachpyx.datasets.data": ["*.csv", "*.gz", "*.json", "*.txt", "*.zip"],
}

try:
    with open(os.path.join(here, "requirements.txt"), "r") as f:
        requirements = f.read().strip(" \n\r\t").split("\n")
except FileNotFoundError:
    requirements = []
if len(requirements) == 0 or requirements == [""]:
    requirements = ["matplotlib", "numpy", "pandas"]

try:
    with open(os.path.join(here, "README.rst"), "r", encoding="utf-8") as f:
        long_description = "teachpyx:" + f.read().split("teachpyx:")[1]
except FileNotFoundError:
    long_description = ""

version_str = "0.1.0"
with open(os.path.join(here, "teachpyx/__init__.py"), "r") as f:
    line = [
        _
        for _ in [_.strip("\r\n ") for _ in f.readlines()]
        if _.startswith("__version__")
    ]
    if len(line) > 0:
        version_str = line[0].split("=")[1].strip('" ')

# see https://pypi.org/classifiers/
setup(
    name="teachpyx",
    version=version_str,
    description="Programmation Python",
    long_description=long_description,
    author="Xavier Dupré",
    author_email="xavier.dupre@gmail.com",
    url="https://github.com/sdpython/teachpyx",
    package_data=package_data,
    install_requires=requirements,
    classifiers=[
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Education",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
