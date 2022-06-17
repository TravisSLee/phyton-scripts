import os

def head(filepath,read_lines):
    f = open(filepath, "r")
    num_lines = sum(1 for line in open(filepath))
    if read_lines > num_lines:
        print("Sorry you entered " + str(read_lines) + " which is greater than the file you want to read that has " + str(num_lines) +" lines.")
    else:    
        for x in range(read_lines):
            print(f.readline()) 
    f.close()    
    
head("flatland.txt",5000)


def new_file(input_1, input_2, input_3):
    
    if os.path.exists(input_1):
        print("The file exists.")
        os.remove(input_1)
        print("The file was deleted.")
        f = open(input_1, "w")
        print("The file was created")
    else:
        f = open(input_1, "w")
        print("The file was created")
    data = data2 = ""
  
    # Reading data from file1
    with open(input_2) as fp:
        data = fp.read()

    # Reading data from file2
    with open(input_3) as fp:
        data2 = fp.read()

    # Merging 2 files
    # To add the data of file2
    # from next line
    data += "\n"
    data += data2    
    f.write(data)
    f.close()
    
    f = open(input_1, "r")
    print(f.read())

  
new_file( "reading.txt", "flatland.txt", "flatland01.txt")

f = open(read, "r")
print(f.read())  
