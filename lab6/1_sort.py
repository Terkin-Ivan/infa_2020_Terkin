from tkinter import *
root=Tk() #создание
e=Entry(root, width=40)
b=Button(root, text="Преобразователь")
l=Label(root, bg='white', fg='black', width=40)
e.pack()
b.pack()
l.pack()

def strSortList(event):
    s=e.get()
    s=s.split()
    s.sort()
    l['text']=' '.join(s) #вернуть значения s через пробел
#вызов свяжем с событием
b.bind('<Button-1>', strSortList)
root.mainloop()
