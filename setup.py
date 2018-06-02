from setuptools import setup

setup(
    name='GitHubPR',
    version='1.0',
    description='Module to find provide the status of the Pull Requests',
    author='Ganesh Kumar J',
    author_email='ganesh.kumar.j@live.com',
    packages=['GitHubPR'],
    install_requires=['urllib3','requests','validators']
)