Installing Xgboost 
=====================

> Make sure that python version is 2.7.13 (instead of 2.7.8) by checking python --version in Anaconda

> conda update conda

> conda update python

> conda install py-xgboost

## This will take time to update conda, python and download/install xgboost 

### PyCharm
~~Point the Debugger to updated version of Python compiler (pythonw.exe of 2.7.13) instead of the older version for xgboost to work~~

> For using Xgboost in PyCharm, install latest version of Anaconda with Python 2.7.13 as default, because due to multiple versions of Python internally dependency cannot be resolved so Xgboost doesn't work with just conda update python
