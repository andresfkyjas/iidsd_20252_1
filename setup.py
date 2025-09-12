from setuptools import setup, find_packages

setup(
    name="iudigital_ad",
    version="0.0.1",
    author="Andres Callejas",
    author_email="andres.callejas@iudigital.edu.co",
    description="ETL para análisis de datos ",
    py_modules=["prueba_etl"],
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "beautifulsoup4",
        "matplotlib",
        "kagglehub[pandas-datasets]>=0.3.8",
        "seaborn",
        "pyarrow"
    ]
)