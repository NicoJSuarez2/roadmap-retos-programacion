'''
# #05 VALOR Y REFERENCIA
> #### Dificultad: Fácil | Publicación: 29/01/24 | Corrección: 05/02/24

## Ejercicio

```
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */
```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.
'''
# Valor

mi_int = 10
mi_int2 = mi_int
mi_int2 = 20
print(mi_int)
print(mi_int2)

mi_tupla = (10, 20)
mi_tupla2 = mi_tupla
mi_tupla2 = (20, 30)
print(mi_tupla)
print(mi_tupla2)

mi_string = "Hola"
mi_string2 = mi_string
mi_string2 = "Adios"
print(mi_string)
print(mi_string2)


# Referencia

mi_lista = [10, 20] 
mi_lista2 = mi_lista
mi_lista2.append(30)
print(mi_lista)
print(mi_lista2)


mi_diccionario = {"nombre": "Nico", "edad": 30}
mi_diccionario2 = mi_diccionario
mi_diccionario2["nombre"] = "Juan"
print(mi_diccionario)
print(mi_diccionario2)


# Funciones por valor y por referencia 

def funcion_valor(int1:int, int2:int):
    int1 = int2
    int2 = 3
    return print(f"Este es el int 1 = {int1}, este es el int2 = {int2}")

def funcion_referencia(lista1:list, lista2:list):
    lista1 = lista2
    lista1.append(30)
    return print(f"esta es la lista 1 = {lista1}, esta es la lista 2 = {lista2}")

funcion_valor(1, 2)
funcion_referencia([1, 2], [3, 4])