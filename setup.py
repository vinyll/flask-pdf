from distutils.core import setup

from flaskpdf import version

setup(
    name='flaskpdf',
    version=version,
    author='Vincent Agnano',
    license='MIT',
    long_description=open('readme.md').read(),
    install_requires=['flask']
)
