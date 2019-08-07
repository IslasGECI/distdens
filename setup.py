from setuptools import setup, find_packages

setup(
    name="distdens",
    version="0.1.0",
    packages=find_packages(),
    install_requires = [        
        "numpy",
        "pandas",
        "scipy",
        "utm",
    ]
)