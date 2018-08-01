#!/bin/python
# -*- coding: utf-8 -*-
#
#				[kuuhaku]
#Descargar lista de reproduccion en youtube

import urllib2
import argparse

href = "pl-video-title-link yt-uix-tile-link yt-uix-sessionlink  spf-link "
file = "youtube.txt"

parse = argparse.ArgumentParser()
parse.add_argument("-u", "--url", help="Introduce la lista de reproduccion a descargar")
parse.add_argument("-w", "--write", help="Si quieres que los urls de los videos esten en un fichero", action="store_true")
parse.add_argument("-o", "--output", help="Archivo de salida")
parse.add_argument("-p", "--program", help="El programa que descargara la lista de reproduccion")
argv = parse.parse_args()


#Extraer los links de los videos
if argv.url:
	lineas = []
	for linea in urllib2.urlopen(argv.url):
		if href in linea:
			lineas.append(linea)

	links = []
	for linea in lineas:
		index 		= linea.find("href=\"")
		indexInicio = linea.find("\"", index, len(linea)) + 1
		indexFin 	= linea.find("&", indexInicio, len(linea)) 
		links.append("https://youtube.com" + linea[indexInicio:indexFin])

#Escribri los links en pantalla
if argv.write:
	if argv.output:
		file = open(argv.output, "w")
		for linea in links:
			file.write(linea + "\n")
		file.close()
	else:
		file = open(file, "w")
		for linea in links:
			file.write(linea + "\n")
		file.close()