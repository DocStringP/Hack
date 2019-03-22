from setuptools import setup, find_packages

setup(
    name='edsahack',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/VestaM94/edsahack.git',
    author='<Sylvester Manganye>',
    author_email='<manganye.so@gmail.com>'
)
