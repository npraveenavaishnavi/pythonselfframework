#how to read text file content using python
#read all the contents of file
#read n number of characters by passing parameters

file = open('test.txt')

#print(file.read(7))                     print(file.read()) is used to read the file

#print(file.readline())                   #file.readline() is used to read the entire line
#print(file.readline())


#print line by line using readline method is (line = file.readline())
#while line!="":
#   print(line)
#   line = file.readline()


#one more way to print the content using (file.readlines())

#values['apple','ball','cat','dog','deer','egg']

for line in file.readlines():
    print(line)

file.close()


