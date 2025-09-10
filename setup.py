from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    Read the requirements file and return a list of dependencies.
    Removes '-e .' if present.
    """
    with open(file_path) as file_obj:
        requirements = file_obj.read().splitlines()

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Olamide Rasheed",
    author_email="olamiderashed001@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)