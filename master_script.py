### This python script executes all the python files in this direct in order to print out a list of member names

import os
import print_member_list
import my_name_is



file_list = os.listdir()
print(file_list)

for files in file_list:

    print(files)
#    import files
