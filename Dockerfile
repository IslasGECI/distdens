FROM python:3.7
COPY . /workdir/
WORKDIR /workdir
RUN pip install numpy \
    autopep8 \
    codecov \
    git+https://git@github.com/islasgeci/geoambiental@v0.1.0 \
    mutmut \
    pandas \
    pylint \
    pylint-fail-under \
    pytest-cov \
    pytest==5.0.1 \
    rope \
    scipy \
    utm
