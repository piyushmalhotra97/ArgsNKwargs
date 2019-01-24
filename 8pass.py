from tkinter import *
action = ""
#create new window
window = Tk()

#name window
window.title("ITRONIX SOLUTION")
#configure window
window.configure(background="#a1dbcd")
#window sized
window.geometry("250x200")

#creates label then uses ut
lbl = Label(window, text="Welcome to Itronix Solution", bg="#a1dbcd")

#pack label
lbl.pack()

#create username
lbl_username = Label(window, text="Username", bg="#a1dbcd")
ent_username = Entry(window)

#pack username
lbl_username.pack()
ent_username.pack()

#attempting to get the ent_username info to store
username = ent_username.get()



#basic enter for password
lbl_password = Label(window, text="Password", bg="#a1dbcd")
ent_password = Entry(window)

#attempting to get the ent_password info to store
password = ent_password.get()

#pack password
lbl_password.pack()
ent_password.pack()

#def to check if username and password is valid
def question():
    username = ent_username.get() # Get value here
    password = ent_password.get() # Get value here
    if username == "itronix" and password=="solution":
        print("Access Granted")
        window.destroy()
        window1 = Tk()
        window1.mainloop()
    else:
        print("Invalid Username and Password")

#will make the sign up button and will call question on click
btn = Button(window, text="Sign In", command=question)

#pack buttons
btn.pack()

#draw window
window.mainloop()
