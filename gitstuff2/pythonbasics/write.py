#another way to open the text file is with open('test.txt') as reader: or as writer:
#read the files and store all the lines in list
#reverse the list
#write the list back to the file

with open('test.txt' ,'r') as reader:
    content = reader.readlines()    #['apple', 'ball', 'cat','dog','deer']
    reversed(content)               #['deer','dog','cat','ball','apple']
    with open('test.txt' ,'w') as writer:
        for line in reversed(content):
            writer.write(line)