from setuptools import find_packages, setup

setup(
    name="fastapi_service_example",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    author="Matt Kafonek",
    author_email="kafonek@gmail.com",
    url="https://github.com/kafonek/fastapi_service_example",
    install_requires=open("requirements.txt").readlines(),
)
