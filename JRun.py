import os, sys
os.system('git pull')
try:
    __import__("FKING").FKING()
except Exception as e:
    exit(str(e))
