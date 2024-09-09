print("Manejo de funciones V!")
def hola_mundo():
    print("Hola aqui estoy dentro de la funcion")

def mensa(msg):
    print(msg)
def escribeNC(Nombre,Apellido):
    print(Nombre,Apellido)
    print(f"Tu nombre completo es {Nombre} {Apellido}")
def suma2numeros(n1,n2):
    s=n1+n2
    return f"La suma de {n1} + {n2} = ", s
# Llamando a la funcion
hola_mundo()
mensa("Hola WhatsAPP")# Llama a mensa con 1 parametro
mensa("El profe me sorprendio enviando mensajes")# Llama a mensa con 1 parametro
escribeNC("Jose","Bonilla")
print("Funciones que regresan valores")
print(suma2numeros(7,3))
print(suma2numeros(15,45))