from setuptools import find_packages, setup

setup(
    name="distdens",
    version="0.1.0",
    packages=find_packages(),
    install_requires = [
        "numpy",
        "pandas",
        "scipy",
        "utm",
        "geoambiental @ git+https://git@github.com/islasgeci/geoambiental@v0.1.0"
    ]
)
