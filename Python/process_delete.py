#!C:\Users\hs\AppData\Local\Programs\Python\Python37\python.exe

import cgi
import os

form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove('data/'+pageId)

print("Location: index.py")
print()