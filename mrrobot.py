#!/usr/bin/env python
# -*- coding: utf-8 -*-

#By Svaazz

import sys
import time
import os

comienzo = time.time()

def ayuda():
	print "\nHelp of mrrobot.py: \n\n mrrobot.py needs at least 3 parametters to work, \n if you want to exclude any of them, type '-e' instead \n\n For example: python mrrobot.py tennis -e gatos \n\n-Options-\n  -e: Excludes the parametter that should be where it is\n  -h: Prints this help message\n  -n: Add it after the 3rd parametter to make mrrobot.py include numbers in the generated passwords\n  -a: Used to add a conjunction in your language and use it in the passwords.\n      Must be followed by the conjunction (python mrrobot.py tennis alex gatos -a and) \n\nScript by Svaazz\n"

class Diccionario:
	

	def __init__(self, pri, seg, ter, num, conjun):

		self.palabra = [pri, seg, ter]
		for x in range(3): #Comprueba si se han omitido parametros
			if self.palabra[x] == '-e':
				self.palabra[x] = ''

		self.num = num
		self.fecha = time.strftime("%c")
		self.conj = conjun

	def pumayus(self, clave):
		return clave.title()[:-1] + clave[-1].upper()
	def umayus(self, clave):
		return clave[:-1] + clave[-1].upper()
	def pmayus(self, clave):
		return clave.title()
	def mayus(self, clave):
		return clave.upper()
	def vocales(self, clave):
		resultado = clave.replace('a', '4')
		resultado = resultado.replace('A', '4')
		resultado = resultado.replace('e', '3')
		resultado = resultado.replace('E', '4')
		resultado = resultado.replace('o', '0')
		resultado = resultado.replace('O', '0')

		return resultado



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
			
			#Repite, con numeros sustituyendo a vocales
			archivo.write(self.vocales(clave) + "\n")
			archivo.write(self.mayus(self.vocales(clave)) + "\n")
			archivo.write(self.pmayus(self.vocales(clave)) + "\n")
			archivo.write(self.umayus(self.vocales(clave)) + "\n")
			archivo.write(self.pumayus(self.vocales(clave)) + "\n")

			if self.num == True:
				for n in range(10000):
					if n < 10: # Añade un 0 delante del numero mientras que sea de una sola cifra
						archivo.write(clave + '0' + str(n) + "\n")
						archivo.write(self.mayus(clave) + '0' + str(n) + "\n")
						archivo.write(self.pmayus(clave) + '0' + str(n) + "\n")
						archivo.write(self.umayus(clave) + '0' + str(n) + "\n")
						archivo.write(self.pumayus(clave) + '0' + str(n) + "\n")

						#Repite, con numeros sustituyendo a vocales
						archivo.write(self.vocales(clave) + '0' + str(n) + "\n")
						archivo.write(self.mayus(self.vocales(clave)) + '0' + str(n) + "\n")
						archivo.write(self.pmayus(self.vocales(clave)) + '0' + str(n) + "\n")
						archivo.write(self.umayus(self.vocales(clave)) + '0' + str(n) + "\n")
						archivo.write(self.pumayus(self.vocales(clave)) + '0' + str(n) + "\n")

					archivo.write(clave + str(n) + "\n") # De todas formas se escribe tambien el numero sin el cero delante para abarcar mas posibilidades
					archivo.write(self.mayus(clave) + str(n) + "\n")
					archivo.write(self.pmayus(clave) + str(n) + "\n")
					archivo.write(self.umayus(clave) + str(n) + "\n")
					archivo.write(self.pumayus(clave) + str(n) + "\n")

					#Repite, con numeros sustituyendo a vocales
					archivo.write(self.vocales(clave) + str(n) + "\n")
					archivo.write(self.mayus(self.vocales(clave)) + str(n) + "\n")
					archivo.write(self.pmayus(self.vocales(clave)) + str(n) + "\n")
					archivo.write(self.umayus(self.vocales(clave)) + str(n) + "\n")
					archivo.write(self.pumayus(self.vocales(clave)) + str(n) + "\n")

		archivo.close()
		os.chdir("../")

	def simple(self):
		for i in range(3):
			self.escribe(self.palabra[i]) #Escribe las tres palabras tal cual
	#Crea una contraseña uniendo las palabras dadas
	def plano(self):
		resultado = self.palabra[0] + self.palabra[1] + self.palabra[2]
		self.escribe(resultado)
	#Crea una contraseña uniendo las palabras dadas en orden inverso
	def inverso(self):
		resultado = self.palabra[2] + self.palabra[1] + self.palabra[0]
		self.escribe(resultado)
	#Construye una contraseña recortando las dos primeras letras de cada palabra y uniéndolas
	def silabas(self):
		si1 = self.palabra[0][:2]
		si2 = self.palabra[1][:2]
		si3 = self.palabra[2][:2]

		resultado = si1 + si2 + si3
		self.escribe(resultado)
	#Si se usa -a crea contraseñas metiendo la conjunción en medio
	def conjuncion(self):
		if self.conj != '':
			for i in range(0, 3): #Intento abarcar la mayoría de posibilidades con 3 palabras
				mezcla = self.palabra[i] + self.conj + self.palabra[i] + self.conj + self.palabra[i]
				self.escribe(mezcla)
			for i in range(0, 2):
				mezcla = self.palabra[i] + self.conj + self.palabra[i+1] + self.conj + self.palabra[i+1]
				self.escribe(mezcla)
			for i in range(0, 2):
				mezcla = self.palabra[i+1] + self.conj + self.palabra[i] + self.conj + self.palabra[i+1]
				self.escribe(mezcla)
			for i in range(0, 2):
				mezcla = self.palabra[i+1] + self.conj + self.palabra[i] + self.conj + self.palabra[i]
				self.escribe(mezcla)
			for i in range(0, 2):
				mezcla = self.palabra[i] + self.conj + self.palabra[i] + self.conj + self.palabra[i+1]
				self.escribe(mezcla)
			for i in range(0, 2):
				mezcla = self.palabra[i] + self.conj + self.palabra[i+1] + self.conj + self.palabra[i]
				self.escribe(mezcla)
			for i in range(0, 2):
				mezcla = self.palabra[i+1] + self.conj + self.palabra[i+1] + self.conj + self.palabra[i]
				self.escribe(mezcla)
			
			for i in range(0, 3): #Intento abarcar la mayoría de posibilidades con 2 palabras
				mezcla = self.palabra[i] + self.conj + self.palabra[i]
				self.escribe(mezcla)
			for i in range(0, 2):
				mezcla = self.palabra[i+1] + self.conj + self.palabra[i]
				self.escribe(mezcla)
			for i in range(0, 2):
				mezcla = self.palabra[i] + self.conj + self.palabra[i+1]
				self.escribe(mezcla)
	#Junta cada palabra con las dos otras y ella misma		
	def juntar(self):
		n = 0
		while n <= 2:
			for i in range(0, 3):
				resultado = self.palabra[n] + self.palabra[i]
				self.escribe(resultado)
			n += 1
	#Cuenta cuantas lineas tiene el archivo para ver cuantas contraseñas se han generado
	def contar(self):
		os.chdir("Generated")
		archivo = open(self.nombre, 'r')
		lectura = list(archivo)
		os.chdir("../")
		return len(lectura)



numeros = False
conjun = ''
#Esto es lo que interpreta los parametros
if len(sys.argv) >= 5:
	if sys.argv[4] == '-n':
		numeros = True
	elif sys.argv[4] == '-a':
		conjun = sys.argv[5]
	if len(sys.argv) == 7:
		if sys.argv[5] == '-a':
			conjun = sys.argv[6]
		elif sys.argv[4] == '-a' and sys.argv[6] == '-n':
			conjun = sys.argv[5]
			numeros = True

elif len(sys.argv) == 2:
	if sys.argv[1] == '-h':
		ayuda()


try:
	dicc = Diccionario(sys.argv[1], sys.argv[2], sys.argv[3], numeros, conjun)
	dicc.simple()
	dicc.plano()
	dicc.inverso()
	dicc.silabas()
	dicc.conjuncion()
	dicc.juntar()
	print "\nDictionary created."
	print "File name: " + dicc.nombre
	fin = time.time()
	print "Elapsed time: " + str(fin - comienzo) + " seconds."
	print str(dicc.contar()) + " passwords generated.\n"
except:
	ayuda()

exit()
