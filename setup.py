from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    
    '''This function will return a list of objects line by line from the requirements.txt file'''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements
    


setup(
name='mlproject',
version='0.0.1',
author='Siddharth Kumar',
author_email='sidas270@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')

)


# -e . in the requirements.txt is used to automatically trigger the setup.py file