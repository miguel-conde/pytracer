from setuptools import setup, find_packages

setup(
    name="pytracer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],  # Aquí puedes agregar dependencias si es necesario
    author="Miguel Conde",
    author_email="miguelco2000@gmail.com",
    description="Simple tracing tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tu_usuario/mi_libreria",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
