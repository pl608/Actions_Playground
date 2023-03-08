import os
for dir,dirs,files in os.walk('.'):
  for x in files:
    print(dir+"/"+x)
