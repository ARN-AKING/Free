import os

 

if __name__ == "__FKING__":

 

   try:

 

       os.system("git pull")
 

       __import__("FKING").makedirectory()

 

   except Exception as e: 

 

       exit(str(e))
