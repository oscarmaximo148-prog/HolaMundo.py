#Datos compuesto
lista = ["hola","bien","real",30]
lista[3]=["adios","mal",20]
print(lista[0])
print(lista[3][2])

tupla = ("compra" , "venta",50)
print(tupla[0])
#no valido
#tupla[4] = ("el","ok",True)
#print(tupla[4])

#crear un (set) conjunto
conjunto = {"ten","cien",100,100}


print(conjunto)

#crear un diccionario 
diccionario = {
    "nombre" : "lola",
    "edad" : 20,
    "fecha" : "2000-10-10"
}
print(diccionario["edad"])