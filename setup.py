from setuptools import setup,find_packages

def get_requirements(file_path):
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name='Diabetes Prediction',
    version='0.0.1',
    author='Aaditya Komerwar',
    author_email='aadityakomerwar@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)