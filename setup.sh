#!/bin/bash
echo "entrez le chemin absolu du projet (ex : /home/fabien/Bureau/Projet-Python)"
read a

echo "entrez votre nom d'utilisateur (ex: fabien )"
read user

echo "#!/bin/bash
cd $a
python3 main.py" > $a/VEST

echo "[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=VEST
GenericName=VEST
Comment=Application de visualisation des équipements sportifs toulousains
Icon=$a/vesp_ico.png
Exec='$a/VEST'
Terminal=true
StartupNotify=true
Categories='Application'" > /home/$user/Bureau/VEST.desktop

echo "[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=VEST
GenericName=VEST
Comment=Application de visualisation des équipements sportifs toulousains
Icon=$a/vesp_ico.png
Exec='$a/VEST'
Terminal=true
StartupNotify=true
Categories='Application'" > /usr/share/applications/VEST.desktop

chmod +x $a/VEST
chmod +x /home/$user/Bureau/VEST.desktop
chmod +x /usr/share/applications/VEST.desktop
chown $user /home/$user/Bureau/VEST.desktop

echo "done"
