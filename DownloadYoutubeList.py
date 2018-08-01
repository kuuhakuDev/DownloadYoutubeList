#!/bin/python
# -*- coding: utf-8 -*-
#
#				[kuuhaku]
#Descargar lista de reproduccion en youtube

import urllib2
import argparse

href = "pl-video-title-link yt-uix-tile-link yt-uix-sessionlink  spf-link "

parse = argparse.ArgumentParser()
parse.add_argument("-u", "--url", help="Introduce la lista de reproduccion a descargar")
parse.add_argument("-w", "--write", help="Archivo de salida")
parse.add_argument("-p", "--program", help="El programa que descargara la lista de reproduccion")
argv = parse.parse_args()

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
		links.append(linea[indexInicio:indexFin])

