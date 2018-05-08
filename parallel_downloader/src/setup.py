# License MIT

import os
from setuptools import setup, find_packages

DISTRO_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


def extract_requirements(path):
    """
    Extracts requirements from requirements file.

    :param path: Path to the requirements file.
    :type path: str.
    :return: list[str] -- list of requirements.
    """
    with open(path, 'r') as file:
        return file.read().splitlines()


setup(
    name='paralleldownloader-distro',
    version='0.1',
    description='Module allowing the parallel download of .jpg files.',
    author='Nickolay Amirkhanov',
    author_email='nick.amirkhanov@gmail.com',
    license='MIT',
    classifiers=[
        'Topic :: Education',
        'Programming Language :: Python :: 3.6'
    ],
    packages=find_packages(exclude=['tests', 'requirements']),
    install_requires=extract_requirements(os.path.join(DISTRO_ROOT_PATH, 'requirements.txt')),
    zip_safe=False
)
