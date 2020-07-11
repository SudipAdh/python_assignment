# WAP to make a function and pass a dictionary in the function and save the dictionary values by creating a csv file. But while creating a file do the same as above question , 1st read , if the file is found then append the dictionary and if not found , handle that error and create a new file.

import csv
def funct(dict):
    try:
        open("temp_file.txt","r")
    except:
        print("File does not exists but I will create it")
        file=open("temp_file.txt","w")
        file.close()
    finally:
        with open("temp_file.txt","a") as csv_file:
            array=[]
            for each in dict:
                array.append(each)
            writer=csv.DictWriter(csv_file,fieldnames=array)
            writer.writeheader()
            writer.writerow(dict)
        file=open("temp_file.txt","r")
        print(file.read()) 
        



name=input("Enter name: ")
roll_no=int(input("Enter roll number: "))
subject=input("Enter subject: ")

dict = { "name": name, "roll_no": roll_no, "subject": subject}
funct(dict)
