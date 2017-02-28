from distutils.core import setup


setup(
    name='flaskpdf',
    version='0.1',
    author='Vincent Agnano',
    license='MIT',
    long_description=open('readme.md').read(),
    install_requires=['Flask'],
)
