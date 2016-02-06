#!/bin/bash
path=$(pwd)

echo "[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=VEST
GenericName=VEST
Comment=Application de visualisation des équipements sportifs toulousains
Icon=$path/vesp_ico.png
Exec='$path/main.py'
Terminal=true
StartupNotify=true
Categories='Application'" > /home/$USER/Bureau/VEST.desktop

echo "[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=VEST
GenericName=VEST
Comment=Application de visualisation des équipements sportifs toulousains
Icon=$path/vesp_ico.png
Exec='$path/main.py'
Terminal=false
StartupNotify=true
Categories='Application'" | sudo tee /usr/share/applications/VEST.desktop


chmod +x $path/main.py
chmod +x /home/$USER/Bureau/VEST.desktop
sudo chmod +x /usr/share/applications/VEST.desktop
chown $USER /home/$USER/Bureau/VEST.desktop

sudo apt-get install python3-PyQt4 -y
sudo apt-get install python3-pip -y
sudo pip3 install xlrd
sudo pip3 install pygeocoder

echo "done"
