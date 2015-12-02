===============
ListenAndBabble
===============

.. warning::
    This repository is still work in progress and contains largely undocumented code.

This repository contains the code for the model published in 'Murakami et al.
(2015): "Seeing [u] aids vocal learning: babbling and imitation of vowels using
a 3D vocal tract model, reinforcement learning, and reservoir computing."
International Conference on Development and Learning and on Epigenetic Robotics
2015 (in press).'

Installing
==========
The code is written in Python 2.7 and was tested in Ubuntu 14.04. Apart from
standard Python libraries, it requires:

* numpy_
* scipy_
* matplotlib_
* brian_
* Oger_
* mpi4py_

You can run ``create_python_environment.sh`` in order to create an python
environment and install into that environment all the dependencies. You need to
have ``virtualenv`` installed.

Additionally, you'll need the VocalTractLab API for Linux, which you can
download at vocaltractlab_.
After downloading it, extract the content into the VTL_API subfolder.


Usage
=====

generatedata.py :
    generates training samples for the auditory learning.
learndata.py :
    does the auditory learning with the ESN.
rl_agent_mpi.py :
    does the sensomotoric learning. While doing the learning it uses
    ``environment_fun.py`` as a resource.
environment_fun.py :
    supplies the environment for the reinforcement learning. It transforms the
    motor signals into reward signals by using the trained ESN.


.. _numpy: http://sourceforge.net/projects/numpy/files/NumPy/
.. _scipy: http://sourceforge.net/projects/scipy/files/scipy/
.. _matplotlib: http://matplotlib.org/downloads.html
.. _brian: http://brian.readthedocs.org/en/latest/installation.html
.. _Oger: http://reservoir-computing.org/installing_oger
.. _mpi4py: https://pypi.python.org/pypi/mpi4py
.. _vocaltractlab: http://vocaltractlab.de/index.php?page=vocaltractlab-download

