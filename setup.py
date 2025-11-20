from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    requirements:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                require=line.strip()
                if require and require!='-e .':
                    requirements.append(require)
    except:
        print('Requirements.txt not found')

    return requirements


print(get_requirements())

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Aaqid',
    author_email='aaqidget@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
