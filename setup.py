from setuptools import setup, find_packages

setup(
    name="Particulas_Elementales",
    version="1.0.0",
    author="Ivan Jafet Davila Vergara",
    author_email="davilaivan777@gmail.com",
    description="Un paquete para gestionar y visualizar partículas subatómicas con una interfaz gráfica",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/IvanDavila777/Particulas-Elementales",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "PyQt5>=5.15",
        "pandas>=1.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics",
        "Intended Audience :: Education"
    ],
    python_requires=">=3.8",
    entry_points={
    "console_scripts": [
        "particulas-gui=Particulas_Elementales:main",  # Nombre del archivo y función principal
    ],
    },

)
