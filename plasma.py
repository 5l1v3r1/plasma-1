#!/usr/bin/env python3
import sys
import os
import readline
import config
from config import *

python_ver = "python3"

def modules():
	config.recon_banner()
	modules = os.listdir("modules/")
	for module in modules:
		if "__pycache__" in module:
			continue
		if "config.py" in module:
			continue
		print (point + "[~] "+ item + str(module))
	print ("")
	no_of_modules = len(modules)
	if "__pycache__" in modules:
		no_of_modules = no_of_modules - 1
	if "config.py" in modules:
		no_of_modules = no_of_modules - 1
	print ("Modules Found: " + str(no_of_modules))
	print ("" + end)
	return True

def help():
	config.help_banner()
	print ("     banner                     Display the banner.")
	print ("     exit                       Ask Plasma to leave you alone and die in a hole.")
	print ("     help                       Display help menu.")
	print ("     list modules               List all the available modules.")
	print ("     use <module_name>          Use a specific module.")
	print ("" + end)
	return True

def run_module(module_name):
	modules = os.listdir("modules/")
	if module_name in modules:
		os.system(python_ver + " ./modules/" + module_name)
	else:
		print (error_module_not_found)
	return True

def menu():
	while (True):
		command  = input(cmd_tag)
		if (command == "banner"):
			config.banner()
		elif (command == "exit"):
			break
		elif (command == "help"):
			help()
		elif (command == "list modules"):
			modules()
		elif (command[0:4] == "use "):
			module_name = command[4:]
			run_module(module_name)
		else:
			print (warning_incorrect_command)
	return True

def main():
	config.banner()
	help()
	menu()
	return True

if __name__ == "__main__":
	main()