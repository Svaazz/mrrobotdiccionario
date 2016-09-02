# Generador de diccionarios

Script para generar diccionarios de contraseñas basado en el utilizado por Elliot en el capítulo 1 de la primera temporada entre el minuto 0:52 y el 0:53

La forma correcta de utilizarlo (En **Linux**) es:

**python mrrobot.py palabra1 palabra2 palabra3 (-n)**

En **Windows** debería funcionar con:

**py mrrobot.py palabra1 palabra2 palabra3 (-n)**

EJEMPLO:
python mrrobot.py tennis alex cats

Necesita 3 palabras que se encargará de enlazar de diversas formas para formar el diccionario. El atributo -n es opcional y sirve para añadir numeros a las combinaciones ya que típicamente las contraseñas los tienen (clavesecreta99)

Los diccionarios son archivos .txt y se guardan en la carpeta "Generated".
Esta no es la versión final del script.

Próximas implementaciones:
  - Más métodos de mezcla para las contraseñas
  - Una pequeña ayuda con instrucciones al escribir -h

### Svaazz (c)
