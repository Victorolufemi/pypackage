from setuptools import setup, find_packages

setup(
    name='pypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Python package that sort a list of tuples',
    long_description=open('README.md').read(),
    url='https://github.com/Victorolufemi/pypackage',
    author='Olufemi Victor',
    author_email='olufe17@gmail.com'
)