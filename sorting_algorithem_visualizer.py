from tkinter import *
import time
from tkinter import ttk
import random
import bubble_sort
from tkinter.messagebox import *
#creating main window class

class MainWindow(Tk): #inheriting from the Tk class
	def __init__(self): #initializing the main window constructor
		super().__init__() #calling the constructor of the tk class
		self.title("sorting algorithm visualizer")
		self.config(background = "#191919")
		self.geometry("1140x640")
		self.line_width = None
		self.no_of_lines = None
		self.time_delay = None
		x_gapes = None
		self.line_widget_array = None
		self.line_widget_y_co_array = None
		self.line_state = False
		self.sorted_state = None
		self.combostyle = ttk.Style()

		self.combostyle.theme_create('combostyle', parent='alt',
                         			settings = {'TCombobox':
                                     			{'configure':
                                      			{'selectbackground': 'black',
                                       			'fieldbackground': '#191919',
                                       			'background': '#191919',
                                       			'foreground' : 'pink'
                                       			}}}
                         			)
# ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
		self.combostyle.theme_use('combostyle') 
		self.top_frame = Frame(width = 1050,height = 350,bg = "blue")
		self.bottom_frame = Frame(width = 1050,height = 170,bg = "black")
		self.top_frame.pack(side = TOP,pady = 30)
		self.bottom_frame.pack(side = BOTTOM,pady = 30)
		self.slate = Canvas(self.top_frame,bg = "black",width = 1044,height = 344)
		self.slate.pack(padx = 3,pady = 3)
		self.line_width_label = Label(self.bottom_frame,text = "select width of lines",bg = "black",fg = "blue",font = "helvatica 16 normal")
		self.line_width_label.grid(row = 0,column = 0,padx = 28,pady = 20)
		self.line_width_array = [1,2,3,4]
		self.line_width_combo = ttk.Combobox(self.bottom_frame,value = self.line_width_array,font = "helvatica 14 normal")
		self.line_width_combo.set(1)
		self.line_width_combo.grid(row = 0,column = 1,padx = 28,pady = 20)
		self.sorting_array = ["bubble sort","quick sort","merge sort","insertion sort","radix sort","selection sort"]
		self.sorting_label = Label(self.bottom_frame,text = "select sorting algo",font = "helvatica 16 normal",bg = "black",fg = "blue")
		self.sorting_label.grid(row = 0,column = 2,padx = 28,pady = 20)
		self.sorting_combo = ttk.Combobox(self.bottom_frame,value = self.sorting_array,font = "helvatica 14 normal")
		self.sorting_combo.set("bubble sort")
		self.sorting_combo.grid(row = 0,column = 3,padx = 28,pady = 20)
		self.line_create_button = Button(self.bottom_frame,text = "create random lines",bg = "green",fg = "white",font = "helvatica 14 normal",command = self.line_create)
		self.line_create_button.grid(row = 1,column = 0,pady = 20)
		self.clear_slate_button = Button(self.bottom_frame,text = "clear screen",bg = "green",fg = "white",font = "helvatica 14 normal",command = self.clear_screen)
		self.clear_slate_button.grid(row = 1,column = 1,pady = 20)
		self.line_sort_button = Button(self.bottom_frame,text = "sort lines",bg = "green",fg = "white",font = "helvatica 14 normal",command = self.sort)
		self.line_sort_button.grid(row = 1,column = 2,pady = 20)
		self.time_lapse_array = [i for i in range(1,100)]
		self.time_lapse_combo = ttk.Combobox(self.bottom_frame,value = self.time_lapse_array,height = 4,font = "helvatica 14 normal")
		self.time_lapse_combo.grid(row = 1,column = 3,pady = 20)
		self.time_lapse_combo.set("set delay")


	def line_create(self):
		if self.line_state == True:
			self.clear_screen()
			self.line_widget_array = None
			self.line_widget_y_co_array = None
		x = int(self.line_width_combo.get())
		self.line_width = x
		self.no_of_lines = int(1044 / x)
		self.line_widget_array = [None] * self.no_of_lines
		self.line_widget_y_co_array = [None] * self.no_of_lines
		for i in range(self.no_of_lines):
			y = random.randint(1,343)
			self.line_widget_array[i] = self.slate.create_line(i * self.line_width,344,i * self.line_width,344 - y,fill = "white",width = self.line_width)
			self.line_widget_y_co_array[i] = y
		self.line_state = True
		self.sorted_state = False

	def clear_screen(self):
		for i in range(self.no_of_lines):
			self.slate.delete(self.line_widget_array[i])
			self.line_widget_array[i] = None
			self.line_state = False
			self.sorted_state = None

	def draw_lines(self):
		self.clear_screen()
		for i in range(self.no_of_lines):
			self.line_widget_array[i] = self.slate.create_line(i * self.line_width,344,i * self.line_width,344 - self.line_widget_y_co_array[i],fill = "white",width = self.line_width)

	def sort(self):
		if self.sorted_state == True:
			#print("LINES ARE ALREADY SORTED")
			showinfo("user message","lines are already sorted!!!")
			return
		elif self.sorted_state == None:
			#print("FIRST YOU HAVE TO DRAW LINES")
			showinfo("user message","no lines are available!!!")
			return 
		self.line_create_button.config(state = DISABLED)
		self.clear_slate_button.config(state = DISABLED)
		self.line_sort_button.config(state = DISABLED)
		x = self.sorting_combo.get()
		self.time_delay = self.time_lapse_combo.get()
		if self.time_delay == "set delay":
			self.time_delay = .001
		else:
			self.time_delay = int(self.time_delay) / 1000
			
		if x == "bubble sort":
			bubble_sort.Bubble_sort(self)
		elif x == "quick sort":
			bubble_sort.Quick_sort(self,0,self.no_of_lines - 1)
		elif x == "merge sort":
			bubble_sort.Merge_sort(self,0,self.no_of_lines - 1)
		elif x == "insertion sort":
			bubble_sort.Insertion_sort(self)
		elif x == "radix sort":
			bubble_sort.Radix_sort(self)
		elif x == "selection sort":
			bubble_sort.Selection_sort(self)
		else:
			pass
		self.line_state = True
		self.sorted_state = True
		#print("LINE SORTED SUCCESSFULLY")
		showinfo("user message","lines sorted successfully!!!")
		self.line_create_button.config(state = NORMAL)
		self.clear_slate_button.config(state = NORMAL)
		self.line_sort_button.config(state = NORMAL)

window = MainWindow()

window.mainloop()

