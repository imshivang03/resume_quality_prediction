from setuptools import setup, find_packages
from typing import List


PROJECT_NAME= "Resume Quality Prediction"
VERSION= "0.0.1"
AUTHOR= "Shivang Shritu"
DESCRIPTION= "Implementing Resume Quality Prediction Project"
HYPHEN_E_DOT= "-e ."
REQUIREMENT_FILE_NAME= "requirements.txt"


def get_requirements_list()-> List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list= requirement_file.readlines()
        requirement_list= [i.replace ("\n", "") for i in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list
    

setup(
    name= PROJECT_NAME,
    version= VERSION,
    author= AUTHOR,
    description= DESCRIPTION,
    packages= find_packages(),
    install_requires= get_requirements_list()
)