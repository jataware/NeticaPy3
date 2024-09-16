## NeticaPy3: A Python 3 Wrapper for Netica

NeticaPy3 is a Python 3 wrapper for Netica, a Bayesian inference engine developed by Norsys. It wraps the C API of the Netica inference engine, providing access to over 400 API calls in Python.

This is a fork of NeticaPy to support Python 3: [NeticaPy3 Fork](https://github.com/ValueFromData/NeticaPy)

**Note:** Mac is currently not supported.


## Installation

### Requirements
- Python version 3.5 or newer.
- Cython version 0.29.37.

### For Conda Users

1. Create and activate your environment:
    ```bash
    conda create -y -n netica python=3.9
    conda activate netica
    conda install cython==0.29.21
    ```

2. Get NeticaPy3:
    ```bash
    git clone git@github.com:jataware/NeticaPy3.git
    ```

3. Compile and install NeticaPy3:
    ```bash
    cd NeticaPy3
    ./compile_linux.sh ~/anaconda3/envs/netica/include/python3.10/
    pip install -e .
    ```