#!/usr/bin/env python
# -*- coding: utf-8 -*-

#By Svaazz

import sys
import time
import os

class Diccionario:
	

	def __init__(self, pri, seg, ter, num):
		self.palabra = [pri, seg, ter]
		self.num = num
		self.fecha = time.strftime("%c")

	#Escribir en el txt
	def escribe(self, clave):
		if os.path.exists("Generated") == False: # Crea la carpeta en caso de que no exista
			os.mkdir("Generated")
		os.chdir("Generated") #Se va al directorio Generated

		self.nombre = "Dictionary-" + self.fecha
		archivo = open(self.nombre, 'a')
		archivo.write(clave + "\n")

		if self.num == True:
			for n in range(100):
				archivo.write(clave + str(n) + "\n")

		archivo.close()
		os.chdir("../")

	def simple(self):
		for i in range(3):
			self.escribe(self.palabra[i])
	#Crea una contraseña uniendo las palabras dadas
	def plano(self):
		resultado = self.palabra[0] + self.palabra[1] + self.palabra[2]
		self.escribe(resultado)

	def inverso(self):
		resultado = self.palabra[2] + self.palabra[1] + self.palabra[0]
		self.escribe(resultado)

	def silabas(self):
		si1 = self.palabra[0][:2]
		si2 = self.palabra[1][:2]
		si3 = self.palabra[2][:2]

		resultado = si1 + si2 + si3
		self.escribe(resultado)






if len(sys.argv) >= 5:
	if sys.argv[4] == '-n':
		numeros = True
else:
	numeros = False

try:
	dicc = Diccionario(sys.argv[1], sys.argv[2], sys.argv[3], numeros)
	dicc.simple()
	dicc.plano()
	dicc.inverso()
	dicc.silabas()
	print "Dictionary created."
except:
	print "3 parameters are needed."

exit()






