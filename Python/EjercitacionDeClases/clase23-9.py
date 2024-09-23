'''
Ejercicios con Tuplas en Python
Ejercicio 1: Crear una Tupla
Escribe un programa que cree una tupla con los números del 1 al 5 y la imprima en pantalla. 
Ejercicio 2: Acceder a un Elemento
Crea una tupla con los días de la semana y accede al tercer elemento.
Ejercicio 3: Reemplazar un Elemento (Convertir a Lista)
Dado que las tuplas son inmutables, convierte una tupla a lista para cambiar el valor "Lunes" a "Lun". Luego, vuelve a convertirla en una tupla.
Ejercicio 4: Unir Tuplas
Crea dos tuplas de números y únelas en una sola tupla.
Ejercicio 5: Comprobar Existencia de un Elemento
Verifica si el número 3 está en la tupla (1, 2, 3, 4, 5).
Ejercicio 6: Longitud de una Tupla
Crea una tupla con nombres de frutas y muestra cuántos elementos tiene.
Ejercicio 7: Iterar Sobre una Tupla
Itera sobre una tupla con los números del 1 al 5 y muestra cada número por pantalla.
Ejercicio 8: Contar Elementos en una Tupla
Crea una tupla con números repetidos y cuenta cuántas veces aparece el número 2.
Ejercicio 9: Obtener el Índice de un Elemento
Crea una tupla con los números (10, 20, 30, 40, 50) y encuentra el índice del número 30.
Ejercicio 10: Tuplas Anidadas
Crea una tupla que contenga otras dos tuplas: una con nombres de frutas y otra con números del 1 al 3. Imprime el elemento "Banana".
'''

#Ejercicio 1: Crear una Tupla
tupla = ('perro','gato','conejo')
#print(tupla)
tupla = (1,2,'perro')
#print(tupla)

#Ejercicio 2: Acceder a un Elemento
#Crea una tupla con los días de la semana y accede al tercer elemento.

semana = ('lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo' )
#print(semana[2])

#Ejercicio 3: Reemplazar un Elemento (Convertir a Lista)
#Dado que las tuplas son inmutables, convierte una tupla a lista para cambiar el valor "Lunes" a "Lun". Luego, vuelve a convertirla en una tupla.
#semana[0] = 'monday'
lista = list(semana)
#print(lista)

lista[0] = 'monday'

#print(lista)

tuplafinal = tuple(lista)
#print(tuplafinal)

#Ejercicio 4: Unir Tuplas
#Crea dos tuplas de números y únelas en una sola tupla.

tupla1 = (1,2,3)
tupla2 = (4,5,6)

fusion = tupla1+tupla2
#print(fusion)

#Ejercicio 5: Comprobar Existencia de un Elemento
#Verifica si el número 3 está en la tupla (1, 2, 3, 4, 5).

tupla = (1, 2, 3, 4, 5)
valor = 6 in tupla
#print(valor)

#Ejercicio 6: Longitud de una Tupla
#Crea una tupla con nombres de frutas y muestra cuántos elementos tiene.

frutas = ('manzana', 'pera', 'platano')
conteo = len(frutas)
#print(conteo)

#Ejercicio 7: Iterar Sobre una Tupla
#Itera sobre una tupla con los números del 1 al 5 y muestra cada número por pantalla.

tupla = (1, 2, 3, 4, 5)

#for numero in tupla:
#    print(numero)

#Ejercicio 8: Contar Elementos en una Tupla
#Crea una tupla con números repetidos y cuenta cuántas veces aparece el número 2.

tupla = (1, 2, 2, 4, 1)
#print(tupla.count(1))

#Ejercicio 9: Obtener el Índice de un Elemento
#Crea una tupla con los números (10, 20, 30, 40, 50) y encuentra el índice del número 30.

numeros = (10, 20, 30, 40, 50, 30)
resultado = numeros.index(30)
#print(resultado)

#Ejercicio 10: Tuplas Anidadas
#Crea una tupla que contenga otras dos tuplas: una con nombres de frutas y otra con números del 1 al 3. Imprime el elemento "Banana".
frutas = ('manzana', 'banana', 'platano')
tupla = (1, 2, 3)
apellidos = ('guzman', 'sanchez', 'gonzalez')
tuplaanidada = (frutas, tupla, apellidos)
print(tuplaanidada[1][1])