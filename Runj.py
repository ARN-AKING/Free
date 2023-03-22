import os, platform
os.system('git pull')
import requests
os.system("xdg-open https://github.com/AryanHack907")
bit = platform.architecture()[0]
if bit == '64bit':
    from FKING import FKING
    FKING()