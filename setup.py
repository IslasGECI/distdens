from setuptools import setup, find_packages

setup(
    name="distdens",
    version="0.1.0",
    packages=find_packages(),
    install_requires = [
        "geoambiental @ git+https://git@github.com/islasgeci/geoambiental@v0.1.0#egg=geoambiental-v0.1.0",
        "numpy",
        "pandas",
        "scipy",
        "utm",
    ]
)