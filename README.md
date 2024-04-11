## NeticaPy3 : a Python 3 wrapper for Netica
NeticaPy3 is a Python 3 wrapper for Netica (Netica is a norsys baysian inference engine). The C API of Norsys inference engine called Netica is wrapped into Python using Cython to make the 400+ API's calls of Netica available in Python.

This is a fork of NeticaPy to support Python 3: https://github.com/ValueFromData/NeticaPy

Mac is currently not supported.

Minimal required Python version is 3.5.


## Installation
Example installation in linux/conda environment
```
$ conda create -y -n netica python=3.10
$ conda activate netica
$ conda install cython==0.29.37
$ git clone git@github.com:jataware/NeticaPy3.git
$ cd NeticaPy3
$ ./compile_linux.sh ~/anaconda3/envs/netica/include/python3.10/
### path is to location of python library headers
$ pip install -e .
```
