from os.path import dirname, join
from setuptools import setup, find_packages


with open(join(dirname(__file__), 'aes_encrypter/VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()


setup(
    name='aes_encrypter',
    version=version,
    url='http://placeholder.com',
    description='encryption utils',
    long_description=open('README.rst').read(),
    entry_points= {
        'console_scripts': ['aes-encrypter=aes_encrypter:main']
    },
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pycrypto>=2.6.1'
    ],
)
