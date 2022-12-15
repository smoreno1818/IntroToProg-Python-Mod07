# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# <YourName>,<1.1.2030>,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!


# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    fileObj = open(file_name, 'wb')
    pickle.dump(list_of_data, fileObj)
    fileObj.close()
    print("writing data to: "+file_name)

def read_data_from_file(file_name):
    fileObj = open(file_name, 'rb')
    data = pickle.load(fileObj)
    fileObj.close()
    print("Reading data from: " + file_name)
    return data


# Presentation ------------------------------------ #
# TODO: Get ID and NAME From user, then store it in a list object
user_id = input("what is your user id: ")
user_name = input("what is your user name: ")
user_info = user_id + ", " + user_name

lstCustomer.append(user_info)
print(lstCustomer)


# TODO: store the list object into a binary file
# https://pythonlobby.com/pickle-module-dump-and-load-in-binary-files-in-python/
# looking to save list in binary file

#this link has practical examples that explain loading a binary file with pickle or dumping into a binary file using pickle




file_name = "customerData.dat"
list_of_data = lstCustomer
save_data_to_file(file_name, list_of_data)


# TODO: Read the data from the file into a new list object and display the contents
data_loaded_from_binary_file = read_data_from_file(file_name)
print(data_loaded_from_binary_file)


#https://www.geeksforgeeks.org/python-exception-handling/
#Exception is made for code specifically that is likely to throw an error at runtime, but is valid syntax


try:
    z = 1000 / 0
    print(z)
except ZeroDivisionError:
    print("my zero division error")
print("done")