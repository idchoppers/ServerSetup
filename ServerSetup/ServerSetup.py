# Script made by idchoppers! 
import os
import requests
import subprocess
import shutil

# Define url and shorten download options
url = 'https://files.minecraftforge.net/maven/net/minecraftforge/forge/1.12.2-14.23.5.2854/forge-1.12.2-14.23.5.2854-installer.jar' 
r = requests.get(url, allow_redirects=True) 

open('oneman.jar', 'wb').write(r.content) # Download the installer

subprocess.call(['java', '-jar', 'oneman.jar', '--installServer']) # Run it without GUI and install
subprocess.call(['java', '-jar', 'minecraft_server.1.12.2.jar']) # Run the server to get the eula.txt and server.properties files

# Overwrite the eula file and make the eula accepted
e = open("eula.txt", "w")
e.write("eula=true")
e.close()

# Overwrite existing server.properties with the settings in data file
p = open("server.properties", "w")
p.write("")
p.close()
shutil.copyfile("data", "server.properties", follow_symlinks=True) 

# Make a BATCH file to launch server with settings
b = open("LaunchServer.bat", "a")
b.write("java -Xms2048m -Xmx12G -XX:PermSize=256m -jar forge-1.12.2-14.23.5.2854.jar .jar nogui\npause")
b.close()

# Make a BASH file to launch server with settings
s = open("LaunchServer.sh", "a")
s.write("#!/bin/bash\njava -Xms2048m -Xmx12G -XX:PermSize=256m -jar forge-1.12.2-14.23.5.2854.jar .jar nogui")
s.close()

# End of setup
print("\n[] Server has finished installing! []\n\n!!! Please review the -Xmx and -Xms settings in the LaunchServer.bat/sh file and change the amount of RAM used to launch the server if needed, the default is -Xmx12G -Xms2048m !!!\n\nIf you are using Windows, use the LaunchServer.bat file to launch the server.\nIf you are using Linux, use the LaunchServer.sh file to launch the server.")