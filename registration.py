from tkinter import*


root=Tk()
root.geometry("500x300")
def getvals():
    print("Accepted")
Label (root,text="Python Registration Form",font="ar 15 bold").grid(row=0,column=3)

name=Label(root,text="Name")
gender=Label(root,text="gender")
Idnumber=Label(root,text="Idnumber")
BookName=Label(root,text="BookName")
paymentmode=Label(root,text="paymentmode")


name.grid(row=1,column=2)
Idnumber.grid(row=2,column=2)
gender.grid(row=3,column=2)
BookName.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

namevalue=StringVar
Idnumbervalue=StringVar
gendervalue=StringVar
BookNamevalue=StringVar
paymentmodevalue=StringVar
checkvalue=IntVar

nameentry =Entry(root,textvariable=namevalue)
Idnumberentry=Entry(root,textvariable=Idnumbervalue)
genderentry=Entry(root,textvariable=Idnumbervalue)
BookNameentry=Entry(root,textvariable=Idnumbervalue)
paymentmodeentry=Entry(root,textvariable=Idnumbervalue)

nameentry.grid(row=1,column=3)
Idnumberentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
BookNameentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

#creating checkbox
checkbtn=Checkbutton(text="remember me?",variable=checkvalue)
checkbtn.grid(row=6,column=3)
#sumcit button
Button(text="Submit",command=getvals).grid(row=7,column=3)
root.mainloop()