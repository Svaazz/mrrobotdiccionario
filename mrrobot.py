#!/usr/bin/env python
# -*- coding: utf-8 -*-

#By Svaazz

import sys
import time
import os

comienzo = time.time()

def ayuda():
	print "\nHelp of mrrobot.py: \n\n mrrobot.py needs at least 3 parametters to work, \n if you want to exclude any of them, type '-e' instead \n\n For example: python mrrobot.py tennis * gatos \n\n-Options-\n  -e: Excludes the parametter that should be where it is\n  -h: Prints this help message\n  -n: Add it after the 3rd parametter to make mrrobot.py include numbers in the generated passwords \n\nScript by Svaazz\n"

class Diccionario:
	

	def __init__(self, pri, seg, ter, num):

		self.palabra = [pri, seg, ter]
		for x in range(3): #Comprueba si se han omitido parametros
			if self.palabra[x] == '-e':
				self.palabra[x] = ''

		self.num = num
		self.fecha = time.strftime("%c")

	def pumayus(self, clave):
		return clave.title()[:-1] + clave[-1].upper()
	def umayus(self, clave):
		return clave[:-1] + clave[-1].upper()
	def pmayus(self, clave):
		return clave.title()
	def mayus(self, clave):
		return clave.upper()


	#Escribir en el txt
	def escribe(self, clave):
		if os.path.exists("Generated") == False: # Crea la carpeta en caso de que no exista
			os.mkdir("Generated")
		os.chdir("Generated") #Se va al directorio Generated

		self.nombre = "Dictionary-" + self.fecha
		archivo = open(self.nombre, 'a')
		if len(clave) > 0:
			archivo.write(clave + "\n")
			archivo.write(self.mayus(clave) + "\n")
			archivo.write(self.pmayus(clave) + "\n")
			archivo.write(self.umayus(clave) + "\n")
			archivo.write(self.pumayus(clave) + "\n")

			if self.num == True:
				for n in range(100):
					archivo.write(clave + str(n) + "\n")
					archivo.write(self.mayus(clave) + str(n) + "\n")
					archivo.write(self.pmayus(clave) + str(n) + "\n")
					archivo.write(self.umayus(clave) + str(n) + "\n")
					archivo.write(self.pumayus(clave) + str(n) + "\n")

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

	def contar(self):
		os.chdir("Generated")
		archivo = open(self.nombre, 'r')
		lectura = list(archivo)
		os.chdir("../")
		return len(lectura)





numeros = False

if len(sys.argv) >= 5:
	if sys.argv[4] == '-n':
		numeros = True
elif len(sys.argv) == 2:
	if sys.argv[1] == '-h':
		ayuda()

try:
	dicc = Diccionario(sys.argv[1], sys.argv[2], sys.argv[3], numeros)
	dicc.simple()
	dicc.plano()
	dicc.inverso()
	dicc.silabas()
	print "\nDictionary created."
	print "File name: " + dicc.nombre
	fin = time.time()
	print "Elapsed time: " + str(fin - comienzo) + " seconds."
	print str(dicc.contar()) + " passwords generated.\n"

except:
	ayuda()

exit()
