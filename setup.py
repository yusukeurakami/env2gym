import os
from setuptools import setup
from setuptools import find_packages

setup(
    name='env2gym',
    version='1.0.0',
    author='Yusuke Urakami based on the code of Denis Yarats',
    description=('a gym like wrapper for dm_control and else env'),
    license='',
    keywords='gym dm_control openai deepmind bullet',
    packages=find_packages(),
    install_requires=[
        'gym',
        'dm_control',
    ],
)
