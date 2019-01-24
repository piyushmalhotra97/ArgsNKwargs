print("\n\n<<<-----KWARGS------->>>")
def printmarks(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,value)
marklist={"Piyush":100,"Whis":98,"Goku":95,"Vegeta":80}
printmarks(**marklist)
    
