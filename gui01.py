#!/usr/bin/python
"""This is module gui01.py\nIt is for python training purpose """
import sys
import Tkinter

author = "DannyM"
purpose = "exercise Python language reference"
globalVar = 11 # globalVar is not used in this module

def message():
	"""This function is called by  button in the module\nIt takes no arguments"""
	print "\t=== [CALLING] ===  message() function ==========="
	print "\t=== [EXITING] === "
	sys.exit()

def message_box():
	"""This function is empty"""
	pass

if __name__ == "__main__":
	"""This module has a __main__ function for execution on the command line"""
	rut = Tkinter.Tk()
	rut.geometry("250x100+10+10")
	rut.title("Welcome")
	print "===MAIN:[",sys.argv[0][2:],"]================="
	wid = Tkinter.Label(None, text = "Aplicatie OK")
	b1 = Tkinter.Button(None, text = "click me")
	b2 = Tkinter.Button(None, text = "Quit", command=message)

	wid.pack()
	b1.pack()
	b2.pack()
	wid.mainloop()
	print "===MAIN:[",sys.argv[0][2:],"]=========[END]==="
