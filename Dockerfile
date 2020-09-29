FROM python:3.8
COPY . /workdir
WORKDIR /workdir
RUN pip install \
    autopep8 \
    black \
    codecov \
    flake8 \
    git+https://git@github.com/islasgeci/geoambiental@v0.1.0 \
    mutmut \
    numpy \
    pandas \
    pylint \
    pylint-fail-under \
    pytest \
    pytest-cov \
    rope \
    scipy \
    utm
CMD make
