print("funciones creadas por el usuario")
# Las funciones
def mi_lista():
    print("---lista---")
    amigos=["Homero","Paty","Lety"]
    for bonilla in amigos :
        print(bonilla)
def tuplas():
    print("---Tuplas---")
    tupla = ("Amarillo", "Azul", "Morado", "Naranja", "Verde")
    for colores in tupla:
        print(colores)
def con():
    print("---Conjunto---")
    conj = {"Manzana", "banana", "Melon"}
    for fruta in conj:
        print(fruta)
def dic():
    print("---Diccionario---")
    dicc= {
    "Marca": "Ford",
    "modelo": "Mustang",
    "año": 2024
    }
    for datos,datos2 in dicc.items():
        print(datos,datos2)
# Llamadas a funciones
mi_lista()
tuplas()
con()
dic()