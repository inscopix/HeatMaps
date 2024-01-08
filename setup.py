from setuptools import find_packages, setup

setup(
    name="HeatMaps",
    version="0.1.0",
    url="",
    author="",
    author_email="",
    description="Description of my package",
    packages=find_packages(),
    install_requires=[
        pandas,
        numpy,
        seaborn,
        matplotlib,
        networkx,
        plotly,
    ],
)
