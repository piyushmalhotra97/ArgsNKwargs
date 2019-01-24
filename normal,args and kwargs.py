print("\n\n<<<-----ARGS and KWARGS------->>>")
def master(normal,*args,**kwargs):
    print("Normal")
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key,value)

lis = ["Piyush",21,225]
marklist = {"Piyush":100,"Whis":98,"Goku":95,"Vegeta":80}
print( master (*lis,**marklist))
