from tkinter import Tk, PhotoImage, Toplevel, Frame, Label, Button
from os import path
from subprocess import Popen, CREATE_NO_WINDOW

t = Tk()
t.overrideredirect(True)

img = PhotoImage(file=path.join(path.dirname(path.abspath(__file__)), 'icon.png'))
txt = 'Выключение или перезагрузка компьютера'
clr = '#6495ED'
w = '#fff'
l1 = ('Перезагрузка', 'Отмена', ' Выкл ')
l2 = (lambda: f('taskkill /im pythonw.exe & shutdown /r /t 0'), t.destroy,
      lambda: f('taskkill /im pythonw.exe & shutdown -s -t 0'))

f = (lambda a: Popen(a, shell=True, creationflags=CREATE_NO_WINDOW))  # f = (lambda a: system(a))

Toplevel().attributes('-alpha', 0.25, '-fullscreen', True)
fr = Frame(t, bg=w, bd=2)
fr.pack()
Label(fr, text=txt, wraplength=120, bg=clr, fg=w, padx=20, pady=20, font='arial 14').grid(row=0, column=0)
Label(fr, image=img, bg=clr).grid(row=0, column=1, columnspan=2, sticky='nswe')
[Button(fr, text=i, command=j).grid(row=1, column=c, sticky='ew') for c, (i, j) in enumerate(zip(l1, l2))]

t.eval('tk::PlaceWindow . center')
t.mainloop()
