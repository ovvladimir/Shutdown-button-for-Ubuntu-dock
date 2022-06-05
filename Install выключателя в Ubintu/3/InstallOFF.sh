#!/bin/bash

# Установка выключателя в Dock

# Каталог иконки
pdir=/temp/bin
# Каталог программы
ddir=~/.local/share/applications

dn_poff=POWEROFF.desktop
fn_poff="${ddir}/$dn_poff"
cat > "${fn_poff}" <<EOL

[Desktop Entry]
Icon=${pdir}/u_poff.png
Name=Выкл
Terminal=false
Type=Application
Exec=gnome-session-quit --power-off
EOL

chmod +x "${fn_poff}"

dconf write /org/gnome/shell/favorite-apps \
"['firefox.desktop', 'gnome-control-center.desktop', \
'org.gnome.Nautilus.desktop', 'org.gnome.Terminal.desktop', \
'shutdown-for-dock.desktop', 'POWEROFF.desktop']"