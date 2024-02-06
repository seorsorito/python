#esto se realiza para paquetes distribuibles 
from setuptools import setup

setup( #hay que poner una coma 

    name="FuncionesMatematicas",
    version="1.0",
    description="Funciones para realizar cálculos",
    author="Victor",
    author_email="victorchamberi@gmail.com",
    url="",
    packages=["Módulos","Módulos.Funciones_Matematicas"]
)

#Una vez terminado en el terminal se pone el siguiente comando: python setup.py sdist