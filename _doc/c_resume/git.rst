Cheat Sheet on Git
==================

Add a remote
++++++++++++

::

    git remote add <remote_name> <url_repo.git>

Example::

    git remote add upstream_dmlc https://github.com/dmlc/xgboost.git

Add a submodule
+++++++++++++++

::

    git submodule add -b <branch> https://<repo>.git <local path>

Example::

    git submodule add -b branchpy https://github.com/sdpython/machinelearning.git cscode/machinelearning

Checkout a specific file from a remote
++++++++++++++++++++++++++++++++++++++

::

    git checkout [-p|--patch] [<tree-ish>] [--] <pathspec>...

Example::

    git checkout origin/main -- include/xgboost/predictor.h

Create a new local branch
+++++++++++++++++++++++++

::

    git checkout -b <new_branch>

Example::

    git checkout -b modif

Create a new remote branch
++++++++++++++++++++++++++

::

    git push -u <remote> <new_branch>

Example::

    git push -u upstream modif

Push modification to remote repository
++++++++++++++++++++++++++++++++++++++

::

    git push

Example::

    git push

Remove a submodule
++++++++++++++++++

::

    git rm <localpath>

The corresponding folder in ``.git/modules/<localpath>`` must be removed too.

Example::

    git rm cscode/machinelearning -f

Reset a branch
++++++++++++++

Reset to local branch

::

    git reset --hard <branch>

Reset to a remote branch

::

    git reset --hard <remote>/<branch>

Example:

::

    git reset --hard upstream/master

Reset a submodule
+++++++++++++++++

::

    git submodule foreach git reset --hard

The option ``--recursive`` does it for submodules included
in submodules. Another to do it is to remove the submodule
folder and to type ``git reset --hard`` which removes
every modification made since the last pull.

Update a branch
+++++++++++++++

::

    git pull <remote> <branch>

Example::

    git pull origin master

You can also rebase the repository:

::

    git fetch <remote>
    git rebase <remote>/<banch>

Example::

    git fetch upstream
    git rebase upstream/master

Update a submodule
++++++++++++++++++

::

    git submodule update --remote --merge

Example::

    git submodule update --remote --merge

Update a submodule to the remote branch
+++++++++++++++++++++++++++++++++++++++

::

    git submodule update --init

Example::

    git submodule update --init

Option ``--recursive`` can be added to fetch
submodules inside submodules.

Fix submodules
++++++++++++++

::

    git submodule sync

Example::

    git submodule sync

Move multiple files
+++++++++++++++++++

Assuming the reposity has no ongoing modification
You can move files and then type right away:

::

    git add -A

Rebase a branch to upsteam branch
+++++++++++++++++++++++++++++++++

This instruction retains some part of the logs.

::

    git pull --rebase upstream main
    git push --force origin

As it may seem that github renamed the default branch from *master* to *main* (see
`Renaming the default branch from master <https://github.com/github/renaming>`_).

Rebase a branch to upsteam branch and erase history
+++++++++++++++++++++++++++++++++++++++++++++++++++

::

    git rebase upstream/main
    git push -f origin main

If there are some commit of your own, they will be moved
to the top of history. The following command deletes the last
commit in the history.

::

    git reset --hard HEAD~1

The remote repository needs to be updated.

Clone a part of a repository, not all
+++++++++++++++++++++++++++++++++++++

The following instructions clone some folder from the specific
tagged version.

::

    # Create a local repository and declare a remote repository
    git init
    git remote add -f origin https://github.com/sdpython/onnx-extended.git
    git config core.sparsecheckout true

    # paths to clone
    echo _unittests/ >> .git/info/sparse-checkout
    echo _doc/examples/ >> .git/info/sparse-checkout
    echo pyproject.toml >> .git/info/sparse-checkout
    echo requirements-dev.txt >> .git/info/sparse-checkout

    # The branch it is cominf from
    git pull origin main

    # Stores the version in environment variable VERSION
    VERSION=$(python -c "import onnx_extended;print(onnx_extended.__version__)")

    # checks out the tag into a new branch.
    git checkout tags/${VERSION} -b thistag
