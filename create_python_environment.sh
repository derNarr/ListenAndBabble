#!/usr/bin/env dash

# create python environment with all prerequisites
#
# in order to activate it in the end use:
#
#   source pyenv/bin/activate
#

virtualenv --python=python2.7 pyenv
source pyenv/bin/activate
pip install --upgrade pip
pip install pyopenssl ndg-httpsclient pyasn1

pip install numpy scipy matplotlib
pip install brian
pip install mpi4py

mkdir build
cd build

# MDP
git clone git://github.com/mdp-toolkit/mdp-toolkit
cd mdp-toolkit
python setup.py install
cd ..
rm -rf mdp-toolkit

# Oger (http://organic.elis.ugent.be/installing_oger)
wget http://organic.elis.ugent.be/sites/organic.elis.ugent.be/files/Oger-1.1.3.tar.gz
tar xzf Oger-1.1.3.tar.gz
cd Oger-1.1.3
python setup.py install
cd ..
rm -rf Oger-1.1.3
rm Oger-1.1.3.tar.gz

cd ..
rm -r build

