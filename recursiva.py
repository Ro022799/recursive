#!/usr/bin/env python3
import os

directory = os.path.expanduser('~')
directory_backup = directory + '/backup/' 
new_list = [directory for directory in os.listdir(directory) if os.path.isdir(directory)== True]
print(new_list)

def recursiva_archivos(lista):
	if len(lista) == 0:
		return []
	else:
		print(os.path.join(directory_backup,lista[0])) 
		return recursiva_archivos(lista[1:])
def recursiva(lista, directory):
	if len(lista) == 0:
		return []
	else:
		print(lista[0])
		list_files = os.listdir(lista[0])
		recursiva_archivos(list_files)
		return [lista[0]] + recursiva(lista[1:], directory)
recursiva(new_list, directory_backup)
