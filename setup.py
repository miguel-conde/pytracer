from setuptools import setup, find_packages
import os

# Leer el README.md de manera segura
def read_file(filename):
    here = os.path.abspath(os.path.dirname(__file__))
    try:
        with open(os.path.join(here, filename), encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""

setup(
    name="pytracer",
    version="1.0.0",
    packages=find_packages(),  
    install_requires=[
        "python-dotenv>=1.0.1"  
    ],
    author="Miguel Conde",
    author_email="miguelco2000@gmail.com",
    description="Simple tracing tool",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/miguel-conde/pytracer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license="MIT"
)
