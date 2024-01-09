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
        "pandas >= 1.3.3",
        "numpy >= 1.21.2",
        "seaborn >= 0.11.2",
        "matplotlib >= 3.4.3",
        "networkx >= 2.6.3",
        "plotly >= 5.3.1",
        "scipy >= 1.7.1"
    ],
)
