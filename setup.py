#!/usr/bin/env python

from setuptools import setup

setup(
    name='dtx-defer',
    version='0.9.1',
    description='Django Twisted Extensions - Remote Deferrer',
    author='Alexander Zykov',
    author_email='tigernwh@gmail.com',
    url='https://github.com/TigerND/dtx-defer',
    package_dir={
        'dtx': 'src'
    },
    packages=[
        'dtx.web.client.defer',
    ],
    data_files=[
    ],
    install_requires = [
        'dtx-core>=0.9.1',
    ],
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
