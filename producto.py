class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def __str__(self):
        return f"{self.__nombre} cuesta - ${self.__precio}"

    def __repr__(self):
        return f"Producto('{self.__nombre}', '{self.__precio}')"

    def __lt__(self, other):
        return self.__precio < other.__precio

    def __gt__(self, other):
        return self.__precio > other.__precio

    def __add__(self, other):
        return self.__precio + other.__precio

    def __len__(self):
        return len(self.__nombre)
