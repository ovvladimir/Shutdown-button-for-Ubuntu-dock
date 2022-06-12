# python3 ~/Downloads/main.py
# sudo apt install python3-tk
import os
import ast

dock_add = "pOFF.desktop"
current_folder = os.path.dirname(os.path.abspath(__file__))
path = "/home/user1/.local/share/applications"
p_file = os.path.join(path, dock_add)
icon = os.path.join(current_folder, "poff.png")
os.system("cp " + icon + " " + path)
icon = os.path.join(path, "poff.png")
# icon = "system-shutdown"
# Toplevel().attributes('-alpha', 0.25, '-fullscreen', True); \

com = '''\
python3 -c "from tkinter import Tk, PhotoImage, Label, Button, EW, NS; import os; t = Tk(); t.overrideredirect(True); \
img = PhotoImage(file='/home/user1/.local/share/applications/poff.png'); \
txt = 'Выключение или перезагрузка П-166М и компьютера'; clr='#6495ED'; \
f = lambda a: os.system('killall -s SIGINT P166MClient; killall -s SIGINT P166MPlan; sleep 1; killall python3 && {}'.format(a)); \
Label(t, text=txt, wraplength=120, bg=clr, padx=20, font='arial 12').grid(row=0, column=0, sticky=NS); \
Label(t, image=img, bg=clr).grid(row=0, column=1, columnspan=2, sticky=EW); \
l1 = ('Перезагрузка', 'Отмена', ' Выкл '); l2 = (lambda: f('reboot'), t.destroy, lambda: f('poweroff')); \
[Button(t, text=i, command=j).grid(row=1, column=c, sticky=EW) for c, (i, j) in enumerate(zip(l1, l2))]; \
t.eval('tk::PlaceWindow . center'); t.mainloop()"
'''

text = '''\
[Desktop Entry]
Icon={}
Name=Выкл
Terminal=false
Type=Application
# Exec=gnome-session-quit --power-off
Exec={}'''.format(icon, com)

with open(p_file, "w") as f:
    f.write(text)

# os.system("chmod +x " + p_file)

with open("/etc/issue.net", "r") as f:
    ver = f.read()

if "Ubuntu 18.04" in ver or "Ubuntu 20.04" in ver or "Ubuntu 22.04" in ver:
    result = os.popen("dconf read /org/gnome/shell/favorite-apps").read()
    result = ast.literal_eval(result)  # eval
    result.pop(result.index(dock_add)) if dock_add in result else result.append(dock_add)
    os.system("dconf write /org/gnome/shell/favorite-apps " + '"' + repr(result) + '"')
elif "Ubuntu 16.04" in ver:
    dock_add = "application://" + dock_add
    result = os.popen("gsettings get com.canonical.Unity.Launcher favorites").read()
    result = ast.literal_eval(result)  # eval
    result.pop(result.index(dock_add)) if dock_add in result else result.append(dock_add)
    os.system("gsettings set com.canonical.Unity.Launcher favorites " + '"' + repr(result) + '"')
