# coding: utf-8
import tkinter as tk
import tkMessageBox
import math
from library import getVPIOL




root = tk.Tk()
root.title("Vapor Pressure (Pa) Calculator")
root.resizable(0,0)



class Calculator:
	def __init__(self):
		self.var1 = ""
		self.var2 = ""
		self.result = 0
		self.current = 0
		self.operator = 0

	def numb_butt(self, index):
		if self.current is 0:
			self.var1 = str(self.var1) + str(index)
			displayTemperature.delete(0, tk.END)
			displayTemperature.insert(0, string=self.var1)
		else:
			self.var2 = str(self.var2) + str(index)
			displayTemperature.delete(0, tk.END)
			displayTemperature.insert(0, string=self.var2)

	def clear(self):
		self.__init__()
		displayTemperature.delete(0, tk.END)

	def init(self):
		try:
			C1val = getVPIOL(str(nameCompound_entry.get().lower()))[0]
			C2val = getVPIOL(str(nameCompound_entry.get().lower()))[1]
			C3val = getVPIOL(str(nameCompound_entry.get().lower()))[2]
			C4val = getVPIOL(str(nameCompound_entry.get().lower()))[3]
			C5val = getVPIOL(str(nameCompound_entry.get().lower()))[4]
		except TypeError:
			raise tkMessageBox.showinfo("Invalid Input", "The chemical that you are looking for is not yet available in the library")

		c1Entry = tk.Label(root, text=C1val, width=17, height=3)
		c2Entry = tk.Label(root, text=C2val, width=17, height=3)
		c3Entry = tk.Label(root, text=C3val, width=17, height=3)
		c4Entry = tk.Label(root, text=float(C4val), width=17, height=3)
		c5Entry = tk.Label(root, text=C5val, width=17, height=3)

		c1Entry.grid(row=2, column=1)
		c2Entry.grid(row=3, column=1)
		c3Entry.grid(row=4, column=1)
		c4Entry.grid(row=5, column=1)
		c5Entry.grid(row=6, column=1)

	def solve(self):
		try:
			C1val = getVPIOL(nameCompound_entry.get().lower())[0]
			C2val = getVPIOL(nameCompound_entry.get().lower())[1]
			C3val = getVPIOL(nameCompound_entry.get().lower())[2]
			C4val = getVPIOL(nameCompound_entry.get().lower())[3]
			C5val = getVPIOL(nameCompound_entry.get().lower())[4]
			T     = float(displayTemperature.get())

			P = math.exp(C1val+(C2val / T) + C4val * (T**C5val)) * T**C3val
		except TypeError:
			raise tkMessageBox.showinfo("Invalid Input", "The chemical that you are looking for is not yet available in the library")
		except ValueError:
			raise tkMessageBox.showinfo("Invalid Input", "String input is not allowed")
		except OverflowError:
			P = float('inf')


		displayScreen = tk.Label(root,text=P, width=20, font=("bold"))
		displayScreen.grid(row=0, columnspan=3, pady=5, ipady=5)




calc = Calculator()

b0 		= tk.Button(root, text="0", width=15, height=3, command=lambda: calc.numb_butt(0), bg = "lightgrey")
b1		= tk.Button(root, text="1", width=15, height=3, command=lambda: calc.numb_butt(1), bg = "lightgrey")
b2 		= tk.Button(root, text="2", width=15, height=3, command=lambda: calc.numb_butt(2), bg = "lightgrey")
b3 		= tk.Button(root, text="3", width=15, height=3, command=lambda: calc.numb_butt(3), bg = "lightgrey")
b4 		= tk.Button(root, text="4", width=15, height=3, command=lambda: calc.numb_butt(4), bg = "lightgrey")
b5 		= tk.Button(root, text="5", width=15, height=3, command=lambda: calc.numb_butt(5), bg = "lightgrey")
b6 		= tk.Button(root, text="6", width=15, height=3, command=lambda: calc.numb_butt(6), bg = "lightgrey")
b7 		= tk.Button(root, text="7", width=15, height=3, command=lambda: calc.numb_butt(7), bg = "lightgrey")
b8 		= tk.Button(root, text="8", width=15, height=3, command=lambda: calc.numb_butt(8), bg = "lightgrey")
b9 		= tk.Button(root, text="9", width=15, height=3, command=lambda: calc.numb_butt(9), bg = "lightgrey")
dot     = tk.Button(root, text=".", width=15, height=3, command=lambda: calc.numb_butt("."), bg = "lightgrey")
equals  = tk.Button(root, text="=", width=15, height=3, bg = "lightgreen", command=calc.solve)
clear   = tk.Button(root, text="CE", width=40, height=3, command=calc.clear, bg = "#ff9999", font=("bold"))
enter   = tk.Button(root, text="Enter", width=15, height=1, bg = "lightgreen", command=calc.init)

b7.grid(row=8, column=0, padx=5)
b8.grid(row=8, column=1)
b9.grid(row=8, column=2, padx=5)
b4.grid(row=9, column=0, padx=5)
b5.grid(row=9, column=1)
b6.grid(row=9, column=2)
b1.grid(row=10, column=0, padx=5)
b2.grid(row=10, column=1)
b3.grid(row=10, column=2)
b0.grid(row=11, column=0, padx=5)
dot.grid(row=11, column=1)
equals.grid(row=11, column=2)
clear.grid(row=12, columnspan=5, sticky = "S", pady=5)
enter.grid(row=1, column=2)


nameCompound 		= tk.Label(root, text="Compound", width=15, height=3)
nameCompound_entry  = tk.Entry(root)
labelTemperature 	= tk.Label(root, text="Temperature (K)", width=15, height=3)
displayTemperature  = tk.Entry(root)


nameCompound.grid(row=1, sticky="E")
nameCompound_entry.grid(row=1, column=1)
labelTemperature.grid(row=7, sticky="E")
displayTemperature.grid(row=7, column=1)

c1 		= tk.Label(root, text="C1 =", width=15, height=3)
c2 		= tk.Label(root, text="C2 =", width=15, height=3)
c3 		= tk.Label(root, text="C3 =", width=15, height=3)
c4 		= tk.Label(root, text="C4 =", width=15, height=3)
c5 		= tk.Label(root, text="C5 =", width=15, height=3)

c1.grid(row=2, column=0)
c2.grid(row=3, column=0)
c3.grid(row=4, column=0)
c4.grid(row=5, column=0)
c5.grid(row=6, column=0)

root.mainloop() 