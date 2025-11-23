curl -O https://dl.suckless.org/tools/dmenu-5.2.tar.gz
tar -xzf dmenu-5.2.tar.gz

cd dmenu-5.2
patch -p1 < ../dmenu-5.2-diff 
sudo make clean install