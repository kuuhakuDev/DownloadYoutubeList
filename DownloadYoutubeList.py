#!/bin/python
# -*- coding: utf-8 -*-
#
#				[kuuhaku]
#Descargar lista de reproduccion en youtube

import urllib2
import argparse

parse = argparse.ArgumentParse()
parse.add_argument("-u", "--url", help="Introduce la lista de reproduccion a descargar")
parse.add_argument("-w", "--write", help="Archivo de salida")
parse.add_argument("-p", "--program", help="El programa que descargara la lista de reproduccion")
argv = parse.parse_args()