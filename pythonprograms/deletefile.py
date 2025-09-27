import os
try:
    filename = "dummyfile.txt"
    if os.path.exists(filename):
        os.remove(filename)
        print("file deleted")
    else:
        print("file is not found")
except Exception as err:
    print(err)

### write a program to delete all .py files from your current directory
try:
    files = os.listdir()
    for file in files:    
        if os.path.exists(file) and file.endswith(".docx"):  
            os.remove(file)
            print(file,"is deleted")
        else:
            print(file,"is not found")
except Exception as err:
    print(err)
