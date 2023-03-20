import os
if __name__ == "__FKING__":
   try:
       os.system("git pull")
       __import__("FKING").FKING()
   except Exception as e:
       exit(str(e))
