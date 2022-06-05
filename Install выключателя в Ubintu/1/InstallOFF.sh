#!/bin/bash

# DESC Установка выключателя

# Каталог программы
pdir=/temp/bin
ddir=$(xdg-user-dir DESKTOP)

dn_poff=POWEROFF.desktop
fn_poff="${ddir}/$dn_poff"
cat > "${fn_poff}" <<EOL

[Desktop Entry]
Exec=sh -c 'zenity --question --text="Выключить виртуальную машину ?" --ok-label="Да" --cancel-label="Нет" && (killall -s SIGINT P166MClient; killall -s SIGINT P166MPlan; sleep 1; poweroff)'
Icon=${pdir}/u_poff.png
Name=Выключение
StartupNotify=false
Terminal=false
Type=Application
EOL

chmod +x "${fn_poff}"

