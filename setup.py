from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path, "r") as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.strip() for req in requirements if req.strip() != "-e ."]

        return requirements

setup(
    name="DiamondPricePrediction",
    version="0.0.1",
    author="Devds",
    author_email="devds10072002@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages(),

)