diccionario={
    'nombre':"Juan",
    'edad':33,
    'hinchaverde':True,
    'comidafavorita':['yogur','arandanos','alpiste']
}
print(diccionario['comidafavorita'][2])

#

diccionario={}

diccionario['nombre']=input("Digite su nombre ")

print(diccionario)
print(diccionario['nombre'])

#recorrer

for llave,valor in diccionario.items():
    print(llave)
    print(valor)

