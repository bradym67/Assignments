import os

#Gets directory from user. Only continues is directory is valid.
filePath = ''
while os.path.isdir(filePath) is False:
    filePath = input('Please enter the directory you would like your file to be: ')
    if os.path.isdir(filePath):
        print('Requested directory exists.')
    else:
        print('Requested directory does not exist.')

#Gets file name from user and automatically adds the file extension for the user.
fileName = input('Please enter the desired name of your file (DO NOT PUT A FILE EXTENSION): ')
fileName = fileName + '.txt'

#Creates a complete path from user input
completePath = filePath + '/' + fileName

#Displays complete path to the user.
print(f"The requested file will be located in and saved as:\n {completePath}")

#Gathers information from the user to save to their file.
name = input('Please enter your full name: ')
name = name.title()
address = input('Please enter your address: ')
address = address.title()
phoneNumber = input('Please enter your phone number: ')
userInfo = (name + ', ' + address + ', ' + phoneNumber)

#Writes the user information into the file.
with open(completePath, 'w') as file_object:
    file_object.write(userInfo)

#Displays back to the user what has been saved.
with open(completePath, 'r') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(f"The saved file contains the following:\n {line}")