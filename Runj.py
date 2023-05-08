import os, platform
os.system('xdg-open https://chat.whatsapp.com/KZk9MHGy8YwJjEg8OpZjm9')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from FKING import FKING
    FKING()
