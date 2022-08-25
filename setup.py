import os

import setuptools

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'README.md')) as f:
    long_description = f.read()

# with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')) as f:
#     install_requires = f.read().splitlines()

setuptools.setup(
    name='podch',
    version='1.0.2',
    author='Aleksandr Sup',
    author_email='sup@tmat.me',
    description='Abstract board game',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SashaVonSup/podch',
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: Free for non-commercial use',
        'Operating System :: OS Independent',
        'Topic :: Games/Entertainment :: Board Games',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=setuptools.find_packages(),
    # data_files=[(os.path.dirname(os.path.realpath(__file__)), ['requirements.txt'])],
    # install_requires=install_requires,
    python_requires='>=3.10',
)
