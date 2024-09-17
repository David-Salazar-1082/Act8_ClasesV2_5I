class Informacion:
    
    def mi_lista(self):
        lista_Nomperros=["boby","Dollar","fany"]
        for x in lista_Nomperros:
            print(x)
            

# Tuplas
    def mi_tuplas(self):
        tupla_Razas=["Pastor aleman","Pastor belga","Golden retriever"]
        for x in tupla_Razas:
            print(x)

    def conjunto(self):
        perros = {"Chicos", "Medianos", "Grandes"}
        print(perros)

# Diccionario
    def mi_dicci(self):
        print("genero:")
        diccionario_py={
            "Pastor aleman" : "Perro",
            "Pastor belga" : "Perro",
            "Golden retriever" : "Perro",
        }
        for x,y in diccionario_py.items():
            print(x,y)
# Creando el objeto
datos=Informacion()
print("Listado de nombre de perros")
datos.mi_lista()
print("Listado de razas de perros")
datos.mi_tuplas()
print("Diccionario")
datos.mi_dicci()
