from tkinter import *
from PIL import Image,ImageTk

#window-setup
root = Tk()
root.title("FORM")
root.geometry("380x450")

#BG-Image-Set Up
bg = Image.open("C:\\Users\\abijit\\Desktop\\BgImage2.jpg")  # Make sure the file name matches exactly
bg = bg.resize((380, 450))      # Resize to match the window size
bg_img = ImageTk.PhotoImage(bg)

Label(root, image=bg_img).place(x=0, y=0, relwidth=1, relheight=1)


#heading-form
label = Label(root, 
              text='User Portal',
              font=('calibri',10,'bold'),
              background='#34D9AD',
              padx=0,
              pady=0,
              relief=GROOVE,
              fg='black',
)
label.pack()

#restart-button
def delete_all():

    id.delete(0, END)
    name.delete(0, END)
    email.delete(0, END)
    college.delete(0, END)
    dept.delete(0, END)
    address.delete(0, END)
    
#submit-buton
def submit():

    id_=id.get()
    name_=name.get()
    email_=email.get()
    college_=college.get()
    dept_= dept.get()
    address_= address.get()

    with open ('form.text','w') as f:

        f.write(f"ID = {id_}\n")
        f.write(f"Name = {name_}\n")
        f.write(f"Email = {email_}\n")
        f.write(f"College = {college_}\n")
        f.write(f"Dept = {dept_}\n")
        f.write(f"Address = {address_}\n")
#id     
id = Entry(root,
             background='white',
             font=('arial',10,'italic'),
             width=30,
             bg="#57C785",
             border=2,
            )
id.insert(0,'          Enter ID')             
id.place(y=50,x=50)

def delete_id():

    id.delete(0, END)

button_id = Button(root,
                     text='Delete',
                     font=('arial',10,'bold'),
                     fg='white',
                     background='#0D612E',
                     command=delete_id,
                     activeforeground='white',
                     activebackground='green',
                    )
button_id.place(y=75,x=50)

#name
name = Entry(root,
             background='white',
             font=('arial',10,'italic'),
             width=30,
             bg="#57C785",
             border=2,
            )
name.insert(0,'          Enter name')             
name.place(y=110,x=50)

def delete_name():

    name.delete(0, END)

button_name = Button(root,
                     text='Delete',
                     font=('arial',10,'bold'),
                     fg='white',
                     background='#0D612E',
                     command=delete_name,
                     activeforeground='white',
                     activebackground='green',
                     )
button_name.place(y=135,x=50)

#email
email = Entry(root,              
               background='white',
             font=('arial',10,'italic'),
             width=30,
             bg="#57C785",
             border=2,
            )
email.insert(0,'          Enter email')
email.place(y=170,x=50)

def delete_email():

    email.delete(0, END)

button_email = Button(root,
                      text='Delete',
                     font=('arial',10,'bold'),
                     fg='white',
                     background='#0D612E',
                     command=delete_email,
                     activeforeground='white',
                     activebackground='green',
                    )
button_email.place(y=195,x=50)

#college
college = Entry(root,
             background='white',
             font=('arial',10,'italic'),
             width=30,
             bg="#57C785",
             border=2,
            )
college.insert(0, '          Enter college')
college.place(y=230,x=50)

def delete_college():

    college.delete(0, END)

button_college = Button(root,
                        text='Delete',
                     font=('arial',10,'bold'),
                     fg='white',
                     background='#0D612E',
                     command=delete_college,
                     activeforeground='white',
                     activebackground='green',
                        )
button_college.place(y=255,x=50)

#dept
dept = Entry(root,
             background='white',
             font=('arial',10,'italic'),
             width=30,
             bg="#57C785",
             border=2,
            )
dept.insert(0,'          Enter dept')
dept.place(y=290,x=50)

def delete_dept():

    dept.delete(0, END)

button_dept = Button(root,
                     text='Delete',
                     font=('arial',10,'bold'),
                     fg='white',
                     background='#0D612E',
                     command=delete_dept,
                     activeforeground='white',
                     activebackground='green',
                    )  
button_dept.place(y=315,x=50)  

#address
address = Entry(root,
            background='white',
            font=('arial',10,'italic'),
            width=30,
            bg="#57C785",
             border=2,
            )

address.insert(0,'          Enter address')
address.place(y=350,x=50)

def delete_address():

    address.delete(0, END)

button_address = Button(root,
                    text='Delete',
                    font=('arial',10,'bold'),
                    fg='white',
                    background='#0D612E',
                    command=delete_address,
                    activeforeground='white',
                    activebackground='green',
                    )
button_address.place(y=375,x=50)

#submit
submit_button = Button(root,
                    text='SUBMIT',
                    font=('arial',10,'bold'),
                    fg='black',
                    background='white',
                    command=submit,
                    activebackground='orange',
                    )
submit_button.place(y=420,x=130)

#restart
restart = Button(root,
                 text='RESTART',
                    font=('arial',10,'bold'),
                    fg='black',
                    background='white',
                    command=delete_all,
                    activebackground='orange',
                )
restart.place(x=200,y=420)

root.config(background="#898EB3")
root.mainloop()