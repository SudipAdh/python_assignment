# WAP to read a file , but if it doesn't exist create one by handling the error when it says file not found.

try:
    open("temp_file.txt","r")
except:
    print("File does not exists")
else:
    file=open("temp_file.txt","r")
    print(file.read())
