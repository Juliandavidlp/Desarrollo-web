#Tratamiento de cadenas y colecciones con métodos y funciones:

#Operaciones con cadenas

cadena='4 Hours Chopin for Studying, Concentration & Relaxation' # declaro una variable

print(len(cadena)) # Devuelve longitud de la cadena.

print(cadena.count('Chopin')) # Cuenta la cantidad de veces que aparece el parámetro que le pasamos.
print(cadena.find('Concentration')) # Devuelve la posición de búsqueda de la cadena que le pasamos como parámetro.

cadena1= cadena.join('**') # Inserta los argumentos que le pasamos como parámetro entre la cadena de caracteres.
#print(cadena1)
lista= cadena.split(' ') # Divide una cadena en unidades menores separando los elementos en una lista.
#print(lista)
tupla= cadena.partition(' ') # Divide una cadena en unidades menores separando los elementos una tupla.
#print(tupla)
cadena1 = cadena.replace('Chopin','Mozart',1) # Busca/sustituye términos.
#print(cadena1)

if cadena.startswith("Tango"): 
    # evalúa si comienza por “tango” (Falta definir el bloque)
    pass 
elif cadena.endswith("Relaxation"): # evalúa si termina por “Relaxation” (Falta definir el bloque)
    pass 
elif cadena.find("Tango") != -1: 
    # evalúa si "Tango" es distinto a menos uno. (Falta definir el bloque)
    pass

print(cadena.upper()) # convierte la cadena a mayúsculas.
print(cadena.lower()) # convierte la cadena a minúsculas.



#Operaciones con tuplas, listas, diccionarios y conjuntos.


nombres= ["Damián","Julián","mamá"]# declaro una lista.          
print(nombres)# o print(nombres[0])


# Si quiero cambiar un elemento de una lista puedo volver a definirlo modificando el índice correspondiente.

nombres[2]="Patricia"
print(nombres) 


#El método list.append() es para agregar un elemento en la lista.
nombres.append("Néstor")
print(nombres)


#La función len() cuenta la cantidad de elementos que tiene una lista, 
# nos devuelve el valor de la longitud de la lista.

print(len(nombres))


#El método list.insert(i,"") permite insertar un elemento en un índice determinado de una lista.

nombres.insert(3,"Néstor")
print(nombres)


# El método list.extend() permite agregar varios elementos en una lista.
nombres.extend("Argentina", "Uruguay","Brasil")
print(nombres)

# El método list.pop() elimina lo que le pasemos como parámetro, o el último elemento de la lista por defecto.

nombres.pop()
print(nombres)

# Y además, si queremos retornar el elemento eliminado se hace lo siguiente:

elementoremovido=nombres.pop()
print(elementoremovido)