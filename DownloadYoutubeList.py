#!/bin/python
# -*- coding: utf-8 -*-
#
#				[kuuhaku]
#Descargar lista de reproduccion en youtube
#
#
#Usted puede copiar, editar, distribuir y hacer lo que quiera
#con el codigo presente...
#
#Leer licencia MIT

import urllib2
import argparse
import commands
import os


href = "pl-video-title-link yt-uix-tile-link yt-uix-sessionlink  spf-link "
fichero = "youtube.txt"

parse = argparse.ArgumentParser()
parse.add_argument("-u", "--url", help="Introduce la lista de reproduccion a descargar")
parse.add_argument("-w", "--write", help="Si quieres que los urls de los videos esten en un fichero", action="store_true")
parse.add_argument("-o", "--output", help="Archivo de salida")
parse.add_argument("-p", "--program", help="El programa que descargara la lista de reproduccion")
parse.add_argument("-d", "--download", help="Descargar los videos en uget-gtk, para esto es necesario -w", action="store_true")
argv = parse.parse_args()


#Extraer los links de los videos
if argv.url:
	print "[+] Descargando codigo fuente."
	lineas = []
	for linea in urllib2.urlopen(argv.url):
		if href in linea:
			lineas.append(linea)
	print "[+] Codigo fuente descargado"
	
	print "[+] Extrayendo los urls de los videos."
	links = []
	for linea in lineas:
		index 		= linea.find("href=\"")
		indexInicio = linea.find("\"", index, len(linea)) + 1
		indexFin 	= linea.find("&", indexInicio, len(linea)) 
		links.append("https://youtube.com" + linea[indexInicio:indexFin])
	print "[+] Exito al extraer los urls de los videos"

#Escribri los links en pantalla
if argv.write:
	if argv.output:
		fichero = argv.output
		print "[+] Escribiendo en " + fichero
		file = open(fichero, "w")
		for linea in links:
			file.write(linea + "\n")
		file.close()
		print "[+] Escritura exitosa"
	else:
		print "[+] Escribiendo en " + fichero
		file = open(fichero, "w")
		for linea in links:
			file.write(linea + "\n")
		file.close()
		print "[+] Escritura exitosa"
else:
	print "\n"
	for linea in links:
		print linea

#Ejecutar comando para descargar en un gestor de descarga
if argv.download:
	print "[+] Abriendo uget-gtk"
	direccion = os.path.abspath(fichero)
	commands.getoutput('uget-gtk --input-file=' + direccion)