FROM python:3
WORKDIR /workdir
COPY . .
RUN pip install \
    autopep8 \
    black \
    codecov \
    flake8 \
    mutmut \
    pylint \
    pylint-fail-under \
    pytest \
    pytest-cov \
    rope
CMD make
