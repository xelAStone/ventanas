from tkinter import *
from io import open
from tkinter import filedialog
#-----funciones----#
variable=''
def limpiar():
	global variable
	texto.delete(1.0,'end')
	variable=''
def Abrir():
	try:
		global variable
		variable=filedialog.askopenfilenames(initialdir='/',filetypes=(('Archivos','.txt'),))
		if variable != '':
			archivo=open(variable,'r')
			contenido=archivo.read()
			texto.delete(1.0,'end')
			texto.insert('insert',contenido)
			archivo.close()
	except TypeError:
		pass
def Guardar():
	global variable
	if variable != '':
		contenido=texto.get(1.0,'end')
		archivo=open(variable,'w+')
		archivo.write(contenido)
		archivo.close()
	else:
		file=filedialog.asksaveasfile(title='Guardar', mode='w', defaultextension='.txt')
		if file is not None:
			variable=texto.get(1.0,'end')
			archivo=open(variable,'w+')
		else:
			variable=''
#----raiz y texto-----#
titulo='esta es un block de notas'
root=Tk()
root.geometry('450x500')
root.title(titulo)
root.config(bg='DarkOrange2')
texto=Text(root,)
texto.pack()
#-----botones-------#
boton=Button(root,text='Limpiar',command=limpiar)
boton.config(fg='orange',bg='black')
boton.pack(fill='x')
boton2=Button(root,text='Abrir',command=Abrir)
boton2.pack(fill='x')
boton2.config(fg='orange',bg='black')
boton3=Button(root,text='Guardar',command=Guardar)
boton3.pack(fill='x')
boton3.config(fg='orange',bg='black')
root.mainloop()
