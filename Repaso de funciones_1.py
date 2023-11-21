#Definir una función:

def hello_world():
    print('Hola mundo con funciones')

def sumar(a,b):
    resultado= a + b
    return resultado
    # return a+b

# hello_world()
# r = sumar(30)
# numero_1 = int(input('Ingrese un valor 1: '))
# numero_2 = int(input('Ingrese un valor 2: '))

# print(f'La suma es {sumar(numero_1,numero_2)}')

#Parámetros por defecto:
def saludar(nombre="Pepe",saludo="Hola"):    
    print(f'{saludo}, {nombre}')

# saludar('Pedro','Buen día')
# saludar('Damián')
# saludar()

#Indicando los argumentos de forma explicita:
# saludar(saludo="Buenas tardes",nombre="Nicolás")


"""
###Tipos de parámetros en una función de Python

A la hora de definir una función, podemos indicar una serie de parámetros.
Sin embargo, si al llamar a la función no le pasamos todos sus argumentos,
el intérprete nos lanzará una excepción donde nos va a indicar que falta
un argumento posicional obligatorio y no se ha especificado.

#Parámetros opcionales en una función

Consideremos a continuación la siguiente función:

def saludo(nombre, mensaje="cómo andás?"):
	print("Hola {}, {}".format(nombre, mensaje))
     
El parámetro "nombre" no indica un valor por defecto, por lo tanto, es posicional u obligatorio. No ocurre lo mismo con el parámetro "mensaje", cuyo valor por defecto es "cómo andás?". 
En caso de no pasar este argumento, se tomará dicho valor por defecto. Por el contrario, si se indica, se sobreescribirá con un nuevo valor pisado.

En una función se pueden especificar tantos parámetros opcionales como se quiera. Pero una vez que se indica uno, los demás parámetros a la derecha deben ser opcionales. 
Entonces, primero se colocan los parámetros posicionales u obligatorios, después los parámetros opcionales.


#Parámetros posicionales y parámetros con nombre en una función:

Cuando invocamos una función en Python con diferentes argumentos, los valores se asignan a los parámetros en el orden que le indicamos.
Sin embargo, el orden se puede cambiar si llamamos a la función a partir del nombre de los parámetros. Para que lo veas más claro, los siguientes ejemplos son todos válidos.

saludo(mensaje="¿cómo estás?", nombre="Damián")
#Hola Damián, ¿cómo estás?

>>>saludo(nombre="Julián", mensaje="¿cómo estás?")
#Hola Julián, ¿cómo estás?

###Conclusión

Por defecto, al llamar a una función los valores de los argumentos se asignan en el
mismo orden en el que se pasan al invocar a dicha función.

Los parámetros opcionales se indican con el operador ‘=’, tienen un valor por defecto y siempre se definen después de los parámetros obligatorios.
Se puede modificar el orden de los argumentos con el que se invoca a una función si se indica el nombre de los parámetros. Los parámetros con nombre siempre aparecen después de los posicionales.
"""


"""Los parámetros *Args y **kwargs:

En los lenguajes de programación de alto nivel, Python entre ellos, al declarar una función podemos definir una serie de parámetros con los que invocar a dicha función.
Por regla general, el número y el nombre de estos parámetros son inmutables. Sin embargo, hay situaciones en las que es mucho más apropiado que el número de parámetros sea opcional y/o variable.

### ¿Qué significan los parámetros indefinidos en Python?

En Python, el parámetro especial *args en una función se usa para pasar, de forma opcional, un número variable de argumentos posicionales.
Lo que realmente indica que el parámetro es de este tipo es el símbolo ‘*’, el nombre args se usa por convención.
El parámetro recibe los argumentos como una tupla. Es un parámetro opcional. Se puede invocar a la función haciendo uso del mismo, o no.
Entonces el número de argumentos al invocar la función es variable.
"""

def sumar_dos(a,b,*args): #*args guarda o devuelve una tupla con todas las variables que le pasemos como parámetro.
    total= a + b

    for numero in args:        
        total += numero #"total" es igual a "total" más "numero"...    
    return total

resultado1= sumar_dos(1,4,10,3)
resultado2= sumar_dos(1,4,77)
print(f'El resultado: {resultado1}')
print(f'El resultado: {resultado2}')

"""
Otra opción es reimplementar nuestra función de la siguiente manera:
"""

def sum(*args):
    valor = 0

    for i in args:
        valor += i    
          
    return valor

"""
Con esta nueva implementación, podemos llamar a la función con cualquier número variable de valores, por ejemplo:
sum()

sum(2, 3)
sum(2, 3, 4)
sum(2, 3, 9, 90)


Veamos ahora el uso de **kwargs como parámetro. En Python, el parámetro especial **kwargs en una función se usa para pasar, de manera opcional,
un número variable de argumentos con nombre. Las principales diferencias con respecto *args son:

Lo que realmente indica que el parámetro es de este tipo es el símbolo **, el nombre kwargs se usa por convención.
El parámetro recibe argumentos como un diccionario, por lo que, al tratarse de un diccionario, el orden de los parámetros no importa.
Los parámetros se asocian en función de las claves del diccionario.
"""

#**kwargs sirve para guardar en un diccionario en forma de llave-valor los elementos que le pasemos como parámetro.

def saludar_dos(nombre,saludo, **kwargs):
    print(f'{saludo}, {nombre}')
    print(kwargs)

    for key,value in kwargs.items():
        print(f'Key: {key}, Value:{value}')

saludar_dos(nombre='Julian', saludo='Hi!', mensaje_uno='Como estas?', mensaje_dos='Nos vemos')





