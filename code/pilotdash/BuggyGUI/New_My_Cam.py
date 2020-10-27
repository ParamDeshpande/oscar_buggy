from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk

root = Tk() 
root.geometry('200x150') 

style = Style() 


# Will add style to every available button 
# even though we are not passing style 
# to every button widget. 
style.configure('TButton', font =
			('calibri', 10, 'bold', 'underline'), 
				foreground = 'red')

def Circle():
    print('Circle Selected')
    root.destroy()
    window = Tk()
    window.title('Circle View')
    window.geometry('500x250')
    ttk.Label(window, text = "Circular Cinematographic View",  
          background = 'green', foreground ="white",  
          font = ("Times New Roman", 15)).grid(row = 0, column = 1, padx = 10)
    ttk.Label(window, text = "Select the Object you want to detect: ", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
    n = StringVar()
    monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)
    monthchoosen['values'] = ('All',
                              'Ball',
                              'Person',
                              'Car',
                              'Box',
                              'Plane')
    monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()
    def Click1():
        val = tk.StringVar()
        val = n.get()
        print(val + " Selected")
        if val == "All":
            window.destroy()
            import dualplayer1
        if val == "Ball":
            window.destroy()
            import dualplayer2
        if val == "Person":
            window.destroy()
            import dualplayer3
    button = ttk.Button(window, text="Select", command=Click1)
    button.grid(column = 1, row = 7)
def Pan():
    print('Pan Selected')
    root.destroy()
    window = Tk()
    window.title('Pan View')
    window.geometry('500x250')
    ttk.Label(window, text = "Pan Cinematographic View",  
          background = 'green', foreground ="white",  
          font = ("Times New Roman", 15)).grid(row = 0, column = 1, padx = 10)
    ttk.Label(window, text = "Select the Object you want to detect: ", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
    n = tk.StringVar()
    monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)
    monthchoosen['values'] = ('Ball',
                              'Person',
                              'Car',
                              'Box',
                              'Plane')
    monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()
    def Click1():
        val = tk.StringVar()
        val = n.get()
        print(val)
    def Click2():
        window.destroy()
        window1 = Tk()
        window1.title('Object Selected')
    button = ttk.Button(window, text="Click Me!", command=Click1)
    button.grid(column = 1, row = 7)
    button1 = ttk.Button(window, text = "Quit!", command=Click2)
    button1.grid(column = 0, row = 7)
def Drive():
    print('Drive Selected')
    root.destroy()
    window = Tk()
    window.title('Drive View')
    window.geometry('500x250')
    ttk.Label(window, text = "Drive Cinematographic View",  
          background = 'green', foreground ="white",  
          font = ("Times New Roman", 15)).grid(row = 0, column = 1, padx = 10)
    ttk.Label(window, text = "Select the Object you want to detect: ", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
    n = tk.StringVar()
    monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)
    monthchoosen['values'] = ('Ball',
                              'Person',
                              'Car',
                              'Box',
                              'Plane')
    monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()
    def Click1():
        val = tk.StringVar()
        val = n.get()
        print(val)
    def Click2():
        window.destroy()
        window1 = Tk()
        window1.title('Object Selected')
    button = ttk.Button(window, text="Click Me!", command=Click1)
    button.grid(column = 1, row = 7)
    button1 = ttk.Button(window, text = "Quit", command=Click2)
    button1.grid(column = 0, row = 7)
# button 1 
btn1 = Button(root, text = 'Circle', 
				style = 'TButton', 
			command = Circle) 

btn1.grid(row = 0, column = 0, padx = 60) 

# button 2 
btn2 = Button(root, text = 'Pan', command = Pan) 
btn2.grid(row = 1, column = 0, pady = 10, padx = 60)
btn3 = Button(root, text = 'Drive', command = Drive) 
btn3.grid(row = 2, column = 0, pady = 10, padx = 60)

root.mainloop() 
