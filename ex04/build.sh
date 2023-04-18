#!/bin/sh
pip install wheel
python setup.py bdist_wheel
tar czvf dist/my_minipack-1.0.0.tar.gz __init__.py setup.py logger.py progress_bar.py LICENCE.md README