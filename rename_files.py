import os
 

def rename_files():
    # 1 get file names
    file_list = os.listdir(r"C:\Users\C00440245\Documents\Saketh\Python\prank\prank")
    print(file_list)
    path = os.getcwd()
    print ('=',path)
    os.chdir(r"C:\Users\C00440245\Documents\Saketh\Python\prank\prank")
    print ('=',os.getcwd())
     

    #2 for each file rename file name
    for file_name in file_list:
      os.rename(file_name, file_name.translate("0123456789"))
    os.chdir(path)
    print ('=',os.getcwd())

rename_files()    
