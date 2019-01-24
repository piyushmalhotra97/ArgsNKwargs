def student(*args):
    print(type(args)) #tuple
    print(len(args))
    if (len(args)==3):
         print("The name of student is",args[0],",age is",args[1],"and roll no. is",args[2])
    if (len(args)==2):
        print("The name of student is",args[0],",age is",args[1])
    if (len(args)==1):    
        print("The name of student is",args[0])
        
student("Piyush",21,225)
student("Piyush",21)
student("Piyush")

#Another way using lists

l=["Arpit",45,2435]
student(*l)
