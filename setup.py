from setuptools import setup, find_packages

setup(
    name='Hack',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/DocStringP/Hack.git',
    author='Lesa Moloi>',
    author_email='<lesamoloi11@gmail.com>'
)
