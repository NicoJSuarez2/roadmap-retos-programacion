'''
# #04 CADENAS DE CARACTERES
> #### Dificultad: Media | Publicación: 22/01/24 | Corrección: 29/01/24

## Ejercicio

```
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.
'''
import re 

cadena  = "Hola Mundo"
len(cadena) # 9
cadena[0] # H
subcadena = cadena[0:4] # Hola
cadena2 = " python"
cadena + cadena2 
cadena.upper() # HOLA MUNDO
cadena.lower() # hola mundo
cadena.replace("Hola", "Adios")
cadena.strip()
cadena.startswith("Hola")
cadena.endswith("Mundo")
cadena.find("Mundo")
x , y= cadena.split(" ")
verificacion = "Hola" in cadena
verificacion2 = "Hola" not in cadena


def comprobaciones(palabra1, palabra2):
    if palindromo(palabra1,palabra2):
        print("Es palindromo")
    if anagrama(palabra1, palabra2):
        print("Es anagrama")
    if isograma(palabra1):
        print("Es isograma")

def palindromo(palabra1 , palabra2):
    print(f"la palabra {palabra1} es palindromo {palabra1 == palabra1[::-1]}")
    print(f"la palabra {palabra2} es palindromo {palabra2 == palabra2[::-1]}")

def anagrama(palabra1, palabra2):   
    if sorted(palabra1) == sorted(palabra2):
        return True
    else:
        return False
    
def  isograma(palabra1):
    if len(palabra1) == len(set(palabra1)):
        return True

comprobaciones("amor","roma")