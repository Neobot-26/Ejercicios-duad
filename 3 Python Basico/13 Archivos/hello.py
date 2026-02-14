def open_and_print_file(path):
	import os
    print(os.getcwd())
	file = open("cancion.txt","r",encoding="utf-8")
	print(file.read())

open_and_print_file('cancion.txt')