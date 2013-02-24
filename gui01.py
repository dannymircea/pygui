#!/usr/bin/python

import sys
import Tkinter

if __name__ == "__main__":
	rut = Tkinter.Tk()
	rut.geometry("250x100+10+10")
	rut.title("Welcome")
	print "===MAIN:[",sys.argv[0][2:],"]================="
	wid = Tkinter.Label(None, text = "Aplicatie OK")
	b1 = Tkinter.Button(None, text = "click me")
	wid.pack()
	b1.pack()
	wid.mainloop()
	print "===MAIN:[",sys.argv[0][2:],"]=========[END]==="
