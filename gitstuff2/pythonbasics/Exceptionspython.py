ItemInCart=0
#2 items will be added to cart

if ItemInCart !=2:     #raise Exception("Products cart count not matching")
   pass

assert(ItemInCart==0)   #assert() is a method which expects the condition to be true


#try catch method
#try, catch=except
try:
    with open('filelog.txt','r') as reader:
        reader.read()


except:
    print("Reached this block because failure in try block")


try:
    with open('filelog.txt','r') as reader:
        reader.read()


except Exception as e:
    print (e)

finally:
    print("clear all records")