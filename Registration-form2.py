#import tkinter
from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Student Registration")
root.geometry("1400x600")
root.configure(background="light blue")


def show():
   
    if (f_name.get()and l_name.get()and d_o_b.get() and add.get()and p_code.get()and contact.get()and e_mail.get())=="":
        messagebox.showerror("error","empmty entries Are Not Allowed")
    else:
        messagebox.showinfo("info","form is submitted")
        
        
def reset():
    r=messagebox.askyesnocancel("Reset","Do you want to fill the form again?")

def showmydata():
    print("Name- %s %s\nDOB- %s\nAddress- %s\nPin Code- %s \nContact- %s \nEmail- %s "%(f_name.get(),l_name.get(),d_o_b.get(), add.get(),p_code.get(),contact.get(),e_mail.get()) )

def end():
    e=messagebox.showinfo("Exit","To exit, close the window.")
    
def var_states():
    print("male:%d,\nfemale:%d"%(var1.get(),var2.get()))
    
form=Label(root, text="REGISTRATION FORM",font=("Bold",16),bg="blue", fg="white", width=20)
form.grid(column=1, row=0)

                
fname=Label(root, text="First Name",font=("Times New Roman",12),bg="light blue", fg="black", width=15)
fname.grid(column=0, row=1)

f_name=Entry(root, width=20)
f_name.grid(column=1, row=1)

lname=Label(root, text="Last Name",font=("Times New Roman",12),bg="light blue", fg="black", width=15)
lname.grid(column=0, row=2)

l_name=Entry(root, width=20)
l_name.grid(column=1, row=2)

dob=Label(root, text="DOB",font=("Times New Roman",12),bg="light blue", fg="black", width=15)
dob.grid(column=0,row=3)

d_o_b=Entry(root, width=20)
d_o_b.grid(column=1, row=3)

gender=Label(root, text="Gender-",font=("Times New Roman",12),bg="light blue", fg="black", width=15)
gender.grid(column=0,row=4)
var1=IntVar()
male=Radiobutton(root, text="Male",variable=var1, font=("Times New Roman",12),bg="light blue", fg="black", width=15)
male.grid(column=1, row=4)
var2=IntVar()

female=Radiobutton(root, text="Female",variable=var2, font=("Times New Roman",12),bg="light blue", fg="black", width=15)
female.grid(column=2, row=4)

Button(root,text="Show",command=var_states).grid(column=3,row=4)




course=Label(root, text="Course",font=("Times New Roman",12),bg="light blue", fg="black", width=15)
course.grid(column=0,row=5)

python=Radiobutton(root, text="Python",value=1, font=("Times New Roman",12),bg="light blue", fg="black")
python.grid(column=1, row=5)

django=Radiobutton(root, text="Django",value=2, font=("Times New Roman",12),bg="light blue", fg="black")
django.grid(column=2, row=5)

angular=Radiobutton(root, text="Angular",value=3, font=("Times New Roman",12),bg="light blue", fg="black")
angular.grid(column=3, row=5)

node=Radiobutton(root, text="Node",value=4, font=("Times New Roman",12),bg="light blue", fg="black")
node.grid(column=4, row=5)

javascript=Radiobutton(root, text="Javascript",value=5, font=("Times New Roman",12),bg="light blue", fg="black")
javascript.grid(column=5, row=5)

m_stack=Radiobutton(root, text="Mean Stack",value=6, font=("Times New Roman",12),bg="light blue", fg="black")
m_stack.grid(column=6, row=5)

f_stack=Radiobutton(root, text="Full Stack",value=7, font=("Times New Roman",12),bg="light blue", fg="black")
f_stack.grid(column=7, row=5)

w_dev=Radiobutton(root, text="Web Development",value=8, font=("Times New Roman",12),bg="light blue", fg="black")
w_dev.grid(column=7, row=5)
w_dev=Radiobutton(root, text="Web Desiginig",value=8, font=("Times New Roman",12),bg="light blue", fg="black")
w_dev.grid(column=8, row=5)

w_dev=Radiobutton(root, text="Django",value=8, font=("Times New Roman",12),bg="light blue", fg="black")
w_dev.grid(column=9, row=5)


hobbies=Label(root, text="Hobbies",font=("Times New Roman",12),bg="light blue", fg="black", width=15)
hobbies.grid(column=0, row=6)

state=BooleanVar()
state.set(False)

paint=Checkbutton(root, text="Painting",var=state, font=("Times New Roman",12), bg="light blue", fg="black")
paint.grid(column=1, row=6)

sing=Checkbutton(root, text="Singing",var=state, font=("Times New Roman",12), bg="light blue", fg="black")
sing.grid(column=2, row=6)

read=Checkbutton(root, text="Reading",var=state, font=("Times New Roman",12), bg="light blue", fg="black")
read.grid(column=2, row=6)

sport=Checkbutton(root, text="Sports",var=state, font=("Times New Roman",12), bg="light blue", fg="black")
sport.grid(column=3, row=6)

dance=Checkbutton(root, text="Dancing",var=state, font=("Times New Roman",12), bg="light blue", fg="black")
dance.grid(column=4, row=6)

archery1=Checkbutton(root, text="Archery",var=state, font=("Times New Roman",12), bg="light blue", fg="black")
archery1.grid(column=5, row=6)
archery2=Checkbutton(root, text="Archery",var=state, font=("Times New Roman",12), bg="light blue", fg="black")
archery2.grid(column=6, row=6)
archery3=Checkbutton(root, text="Archery",var=state, font=("Times New Roman",12), bg="light blue", fg="black")
archery3.grid(column=7, row=6)
archery4=Checkbutton(root, text="Archery",var=state, font=("Times New Roman",12), bg="light blue", fg="black")
archery4.grid(column=8, row=6)
archery5=Checkbutton(root, text="Archery",var=state, font=("Times New Roman",12), bg="light blue", fg="black")
archery5.grid(column=9, row=6)


address=Label(root, text="Address",font=("Times New Roman",12),bg="light blue", fg="black", width=15)
address.grid(column=0, row=7)

add=Entry(root, width=20)
add.grid(column=1, row=7)

pin=Label(root, text="Pincode",font=("Times New Roman",12),bg="light blue", fg="black", width=15)
pin.grid(column=0, row=8)

p_code=Entry(root, width=20)
p_code.grid(column=1, row=8)

phone=Label(root, text="Contact Number",font=("Times New Roman",12),bg="light blue", fg="black", width=15)
phone.grid(column=0, row=9)

contact=Entry(root, width=20)
contact.grid(column=1, row=9)


email=Label(root, text="E-mail Address",font=("Times New Roman",12),bg="light blue", fg="black", width=15)
email.grid(column=0, row=10)

e_mail=Entry(root, width=20)
e_mail.grid(column=1, row=10)


submit=Button(root, text="Submit",font=("Times New Roman",12),bg="blue", fg="white", width=15, command=show)
submit.grid(column=0,row=11)

reset=Button(root, text="Reset",font=("Times New Roman",12),bg="blue", fg="white", width=15, command=reset)
reset.grid(column=1,row=11)

show=Button(root, text="Show My Data",font=("Times New Roman",12),bg="blue", fg="white", width=15, command=showmydata)
show.grid(column=2,row=11)

cancel=Button(root, text="Cancel",font=("Times New Roman",12),bg="blue", fg="white", width=15, command=end)
cancel.grid(column=3,row=11)

















