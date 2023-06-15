from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str)-> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='e2eMLproject',
    version='0.0.1',
    author='sherine',
    author_email='sherine.jva@gmail.com',
    packages=find_packages(),
    package_data={'': ['requires.txt']},
    include_package_data=True,
    install_requires=get_requirements('requirements.txt')
)
