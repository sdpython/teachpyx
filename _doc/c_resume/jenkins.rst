Cheat Sheet on Jenkins
======================

Installation
++++++++++++

Install Java:

::

    apt-get install openjdk-11-jdk

Install Jenkins:

::

    wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
    sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > \
        /etc/apt/sources.list.d/jenkins.list'
    sudo apt-get update
    sudo apt-get install jenkins

Remove Jenkins:

::

    apt-get remove --purge jenkins

Change Jenkins user:

::

    nano /etc/init.d/jenkins
    chown -R dupre:dupre /var/lib/jenkins
    chown -R dupre:dupre /var/cache/jenkins
    chown -R dupre:dupre /var/log/jenkins

    chown -R jenkins:jenkins /var/lib/jenkins
    chown -R jenkins:jenkins /var/cache/jenkins
    chown -R jenkins:jenkins /var/log/jenkins

    /etc/init.d/jenkins restart

Plugins
+++++++

* `Build timeout plugin <https://plugins.jenkins.io/build-timeout/>`_
* `Console column plugin <https://plugins.jenkins.io/console-column-plugin/>`_
* `Next executions <https://wiki.jenkins.io/display/JENKINS/Next+Executions>`_
* `Collapsing Console Sections Plugin <https://wiki.jenkins.io/display/JENKINS/Collapsing+Console+Sections+Plugin>`_
* `Exclusive Execution <https://plugins.jenkins.io/exclusive-execution/>`_

Start, Restart
++++++++++++++

::

    /etc/init.d/jenkins start

Reset passwords
+++++++++++++++

* Edit file ``/var/lib/jenkins/config.xml``.
* Search for ``<useSecurity>true</useSecurity>``,
  change ``true`` to ``false``.
* Restarts the service ``/etc/init.d/jenkins restart``.
* Change the security settings.
* Restart again.
