# Generador de diccionarios

Script para generar diccionarios de contraseñas basado en el utilizado por Elliot en el capítulo 1 de la primera temporada entre el minuto 0:52 y el 0:53

Genera **3030 contraseñas** con la opción -n habilitada y 30 contraseñas con -n deshabilitada

## La forma correcta de utilizarlo (En **Linux**) es:
```
python mrrobot.py (-h) palabra1 palabra2 palabra3 (-n)
```
## En **Windows** debería funcionar con:
```
py mrrobot.py (-h) palabra1 palabra2 palabra3 (-n)
```

## EJEMPLOS:
```
python mrrobot.py tennis alex gatos
py mrrobot.py tennis alex gatos

python mrrobot.py -h
py mrrobot.py -h

python tennis -e gatos
py tennis -e gatos
```

Necesita 3 palabras que se encargará de enlazar de diversas formas para crear el diccionario. El atributo -n es opcional y sirve para añadir números a las combinaciones ya que típicamente las contraseñas los tienen (clavesecreta99)

## Opciones
```
-e: Se utiliza en lugar de alguno de los tres parámetros necesarios para excluirlo.
-h: Imprime la ayuda
-n: Incluye numeros en las combinaciones

```

Los diccionarios son archivos .txt y se guardan en la carpeta "Generated".
Esta no es la versión final del script.

Próximas implementaciones:
  - Más métodos de mezcla para las contraseñas

### Svaazz (c)
