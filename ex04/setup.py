# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    setup.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/18 09:25:59 by archid-           #+#    #+#              #
#    Updated: 2023/04/18 13:02:08 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from setuptools import setup, find_packages

setup(
    name='my_minipack',
    download_url='modules',
    author='Anas Rchid',
    author_email='archid-@student.1337.ma',
    description='my_minipack bundle',
    version='1.0.0',
    license='GPLv2',
    url="None",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Students",
        "Topic :: Education",
        "Topic :: HowTo",
        "Topic :: Package",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only"
    ],
    python_requires=">=3.7",
    packages=find_packages()
)