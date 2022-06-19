import os

com = '''\
python -c "from tkinter import Tk, PhotoImage, Toplevel, Frame, Label, Button; from os import system; \
t = Tk(); t.overrideredirect(True); Toplevel().attributes('-alpha', 0.25, '-fullscreen', True); \
img = PhotoImage(file='icon.png'); txt = 'Выключение или перезагрузка компьютера'; \
clr = '#6495ED'; w = '#fff'; l1 = ('Перезагрузка', 'Отмена', ' Выкл '); \
l2 = (lambda: f('echo reboot'), t.destroy, lambda: f('echo poweroff')); \
f = lambda a: system('echo Выполнено:') & system(a); fr = Frame(t, bg=w, bd=2); fr.pack(); \
Label(fr, text=txt, wraplength=120, bg=clr, fg=w, padx=20, pady=20, font='arial 14').grid(row=0, column=0); \
Label(fr, image=img, bg=clr).grid(row=0, column=1, columnspan=2, sticky='nswe'); \
[Button(fr, text=i, command=j).grid(row=1, column=c, sticky='ew') for c, (i, j) in enumerate(zip(l1, l2))]; \
t.eval('tk::PlaceWindow . center'); t.mainloop()"
'''

os.system(com)
