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
