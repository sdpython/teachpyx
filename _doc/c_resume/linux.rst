
.. _l-cheatsheet-linux:

Cheat Sheet on Linux
====================

Classic
+++++++

::

    ls
    ls -l
    cd
    find "<pattern>"
    find <path> -name "<pattern>"

Remove packages
+++++++++++++++

::

    apt-get autoremove

Another to remove packages:

::

    aptitude purge ~c

Find large packages:

::

    dpkg --get-selections | cut -f1 | while read pkg; do dpkg -L $pkg | xargs -I'{}' bash -c 'if [ ! -d "{}" ]; then echo "{}"; fi' | tr '\n' '\000' | du -c --files0-from - | tail -1 | sed "s/total/$pkg/"; done | sort -rn

Clean cache:

::

    apt-get clean

Error with a package
++++++++++++++++++++

::

    rm /var/lib/dpkg/info/the-package-causing-error

Clean temporary files
+++++++++++++++++++++

::

    find /tmp -mtime +7 -and -not -exec fuser -s {} ';' -and -exec echo {} ';'

Hard drive
++++++++++

Analysis:

::

    ncdu

Existing partitions:

::

    sfdisk -l
    df -lhT
    df --local --human-readable -T

Folder size:

::

    du -sh /var
    du -shc /var/*

Top heavy folders:

::

    du -h /var/ | sort -rh | head -10

Find top files in a folder:

::

    du -a /var | sort -n -r | head -n 10

Processes
+++++++++

List of processes:

::

    ps aux

Kill a process:

::

    kill <pid>

List of processes memory:

::

    ps -eo size,pid,user,command --sort -size

Environment variable
++++++++++++++++++++

Stores the standard output into an environment variable.

::

    <ENVVAR> = $(<cmd>)

Example:

::

    VERSION=$(python -c "import onnx_extended;print(onnx_extended.__version__)")

Others
++++++

Retrieve the path of an executable:

::

    type -p python3.11
