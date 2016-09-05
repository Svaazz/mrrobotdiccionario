# Generador de diccionarios

Script para generar diccionarios de contraseñas basado en el utilizado por Elliot en el capítulo 1 de la primera temporada de Mr Robot entre el minuto 0:52 y el 0:53

Genera **7.408.140 contraseñas** con las opciones -a y -n habilitadas y 150 contraseñas con estas opciones deshabilitadas.

Tarda una media de **7'86118897 segundos** en generar el diccionario (con -n y -a habilitados)

## La forma correcta de utilizarlo (En **Linux**) es:
```
python mrrobot.py (-h) palabra1 palabra2 palabra3 (-n) (-a) (y/and/et/...)
```

El orden de los parámetros -n y -a no importa

## En **Windows** debería funcionar con:
```
py mrrobot.py (-h) palabra1 palabra2 palabra3 (-n) (-a) (y/and/et/...)
```

## EJEMPLOS:
```
python mrrobot.py tennis alex gatos
py mrrobot.py tennis alex gatos

python mrrobot.py -h
py mrrobot.py -h

python tennis -e gatos
py tennis -e gatos

python mrrobot.py tennis alex gatos -n -a y
py mrrobot.py tennis alex gatos -n -a y
```

Necesita 3 palabras que se encargará de enlazar de diversas formas para crear el diccionario. No puede haber dos palabras iguales, y su longitud tiene que ser superior a 2 caracteres.
Los atributos -n y -a son opcionales y sirven para añadir números a las combinaciones (clavesecreta99, clavesecreta6969, clavesecreta777...) y para añadir conjunciones (perrosygatos, dogsandcats, chiensetchats...), respectivamente.

## Opciones
```
-e: Se utiliza en lugar de alguno de los tres parámetros necesarios para excluirlo.
-h: Imprime la ayuda
-n: Incluye numeros en las combinaciones
-a: Añade conjunciones a las claves generadas, tiene que estar seguido de una.
```

Los diccionarios son archivos .txt y se guardan en la carpeta "Generated".
Esta no es la versión final del script.

Próximas implementaciones:
  - Más métodos de mezcla para las contraseñas

### Svaazz (c)
