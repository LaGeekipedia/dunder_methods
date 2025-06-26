from producto import Producto

producto1 = Producto("Mouse", 20)
producto2 = Producto("Mouse Deluxe", 150)

# Llamado a __str__
print(producto1)
print(producto2)

# Llamado a __repr__
print(repr(producto1))
print(repr(producto2))

print("\nComparaciones:")
print(producto1 < producto2)

print("\nSumas:")
print(producto1 + producto2)

print("\nLongitud del nombre:")
print(len(producto2))
