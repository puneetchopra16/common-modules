#Question 1


import datetime 
date=datetime.datetime.now()
print(date.day)

#Question 2



import webbrowser as web
web.open("https://www.google.com")


#Question 3



import os
os.chdir("F:\directory")
path =  os.getcwd()
filenames = os.listdir(path)
i=1
print(filenames)

for filename in filenames:
    os.rename(filename,str(i)+'.jpg')
    i=i+1


