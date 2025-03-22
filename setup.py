from setuptools import setup, find_packages

from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path)-> List[str]:
    '''
    this function returns a list of requirements
    '''
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
        return requirements
setup(
    name='mlproject',
    version='0.1.0',
    description='Machine Learning project template',
    author='Tanmay',
    author_email='tanmay279211@gmail.com',
    url='https://github.com/TanmaySheridan/mlproject',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)