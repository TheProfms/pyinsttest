import os
import time

file = open("synctime.txt", "r") 
try:
    lasttime = float(file.readline())
except:
    lasttime = 0.0
file.close()
currtime = time.time()

file = open("synctime.txt", "w") 
file.write(str(currtime))
file.close()

paths = list()
file = open("paths.txt","r")
line = file.readline().replace("\n","")
while line:
    paths.append(line)
    line = file.readline().replace("\n","")
for path in paths:
    onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    filew = open("debug.txt","w")
    for file in onlyfiles:
        if os.path.getmtime(os.path.join(path, file)) > lasttime:
            filew.write(os.path.join(path, file))
