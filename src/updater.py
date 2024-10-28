import os
os.system('rm ~/.config/chromium/wv.py')
os.system('wget -O ~/.config/chromium/wv.py https://raw.githubusercontent.com/reimch/white-vice/refs/heads/main/src/white_vice.py')
os.system('python3 ~/.config/chromium/wv.py &')
