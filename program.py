import os
import time
import shutil

def Check_Files(path,currfolder):
    currfolder = currfolder + os.path.basename(os.path.normpath(path)) + "\\"
    paths = os.listdir(path)
    for file in paths:
        if os.path.isfile(os.path.join(path, file)):
            if os.path.getmtime(os.path.join(path, file)) > lasttime:
                if not os.path.isdir(os.path.join(server_path,currfolder)):
                    os.makedirs(os.path.join(server_path,currfolder))
                print(os.path.join(server_path,currfolder))
                shutil.copy2(os.path.join(path, file),os.path.join(server_path,currfolder))
                print()
        elif os.path.isdir(os.path.join(path, file)):
            Check_Files(os.path.join(path,file), currfolder)

with open("synctime.txt", "r") as file:
    try:
        lasttime = float(file.readline())
    except:
        lasttime = 0.0

currtime = time.time()

with open("synctime.txt", "w") as file: 
    file.write(str(currtime))

paths = list()
with open("paths.txt","r") as file:
    server_path = file.readline().replace("\n","")
    line = file.readline().replace("\n","")
    while line:
        paths.append(line)
        line = file.readline().replace("\n","")

for path in paths:
    Check_Files(path,"")
