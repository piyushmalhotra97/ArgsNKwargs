"""
def student(name,age,rollno):
    print("The name of student is ",name,"and age is ",age,"and roll no is ",rollno)

student("Karan",27)
"""



"""
def student(*args):
    print(type(args))
    if(len(args)==3):
        print("The name of student is ",args[0],"and age is ",args[1],"and roll no is ",args[2])
    else:
        print("The name of student is ",args[0],"and age is ",args[1])
        
student("Karan",27,1335)
student("Prakash",28)

l=["Arpit",28,3016]
student(*l)

print("\n\n<<<------KWARGS------>>>")
def printmarks(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,value)
marklist={"Karan":100,"Arpit":90,"Parkash":89,"Priya":96,"Varun":87}
printmarks(**marklist)


print("\n\n<<<------Args and Kwargs Together------>>>")
def master(normal,*args,**kwargs):
    print(normal)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key,value)

lis=["Karan",28,1335]
marklist={"Karan":100,"Arpit":90,"Parkash":89,"Priya":96,"Varun":87}

print(master("Normal arg",*lis,**marklist))
"""
