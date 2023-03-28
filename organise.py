import os,shutil

from_dir='C:/Users/SAMARTH/Documents/New folder'
filelist=os.listdir(from_dir)
print(filelist)
for file in filelist : 
    name,ext=os.path.splitext(file)
    if ext=="":
        continue
    if ext in [".doc",".docx"]:
        if os.path.exists(from_dir+'/documents'):
            src=from_dir+'/'+file
            dest=from_dir+"/documents/"+file
            shutil.move(src,dest) 
        else:
            os.mkdir(from_dir+"/documents")
            src=from_dir+'/'+file
            dest=from_dir+"/documents/"+file
            shutil.move(src,dest) 