import setuptools
from setuptools import find_packages

setuptools.setup(
    version="5.0.12",
    name="dbacademy",
    author="Databricks, Inc",
    maintainer="Databricks Academy",
    url="https://github.com/heritamas/dbacademy",
    install_requires=[],
    package_dir={"": "src"},
    packages=find_packages(where="src")
)
