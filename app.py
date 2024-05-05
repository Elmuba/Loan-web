from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

import mysql.connector
from mysql.connector import Error

connect = mysql.connector.connect( host='localhost', password="", user='root', database='l')
cursor = connect.cursor()



window = Tk()

# window size       
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
size = str(width) + 'x' + str(height)
window.geometry(size)

sponge_image = Image.open("/Users/macbookpro/Desktop/NIIT/Gui/WhatsApp Image 2024-04-30 at 02.27.30.jpeg")
resize_image = sponge_image.resize((width, height))
sponge_photo = ImageTk.PhotoImage(image=resize_image)
sponge_label = Label(window, image=sponge_photo)

sponge_label.pack()

def borrow_loan():
    window.destroy()
    try:
        import project_guii
        login.destroy()
        monie.destroy()
    except ImportError as e:
        print(f"Failed to import project_guii: {e}")





def display_dashboard():
    dashboard()
def dashboard():
    dashboard = Frame(window, width=width, height=height, bg='white')
    dashboard.place(relx=0.5,rely=0.5, anchor="center")
    dashboard.propagate(flag=False)

    dashboard_widget = Frame(dashboard, width=width * 0.3, height=height, bg='blue', padx=20, pady=50)
    dashboard_widget.pack_propagate(flag=False)
    dashboard_widget.place(x=0, y=0)

    dashboarduser= Label(dashboard_widget, text="Welcome to Loanify", font=("Arial bold", 24, "bold"))
    dashboarduser.pack()

    Borrowloan = Button(dashboard_widget, text="Borrow Loan",command=borrow_loan)
    Borrowloan.pack()

    

    Checkloan_status = Button(dashboard_widget, text= "Check Loan Status")
    Checkloan_status.pack()



def login():
    login = Frame(window, width=400, height=500, bg="light blue")
    login.place(relx=0.5, rely=0.5, anchor='w')
    login.pack_propagate(flag=False)
    
    login_widget = Frame(login, bg=login['bg'], padx=20,pady=25)
    login_widget.place(relx=0.5, rely=0.5, anchor='center')

    loginuser= Label(login_widget, text= "Login", bg=login['bg'], font=("Arial bold", 42,"bold" ), padx=20, pady=25)
    loginuser.pack()

    loginemail = Label(login_widget, text= "Email", bg=login['bg'], padx=30, pady=20)
    loginemail.pack()

    loginemail_entry = Entry(login_widget)
    loginemail_entry.pack()

    loginpwd = Label(login_widget, text="Password", bg = login['bg'], padx=30, pady=20)
    loginpwd.pack()

    loginpwd_entry = Entry(login_widget, show="*")
    loginpwd_entry.pack()

    button= Button(login_widget, text= "Login", command=lambda: validate_login())
    button.pack()

    def validate_login():
        login_mail = loginemail_entry.get()
        login_pwd = loginpwd_entry.get()

        if not login_mail:
            messagebox.showerror('Mail Error', 'The email is invalid')
            return ''
        
        if not login_pwd:
            messagebox.showerror('Password Error', 'The password is invalid')
            return ''
        
        try:
            connect = mysql.connector.connect(host='localhost', password='', database='l', user='root')
            cursor = connect.cursor()

            get_user = '''
            SELECT * FROM loan_user
            WHERE email = %s AND password = %s
            '''
            login_entry_detail = (login_mail, login_pwd)

            cursor.execute(get_user, login_entry_detail)

            cur_user = cursor.fetchall()

            if not(cur_user):
                messagebox.showerror('Login Error', 'There is no existing user with this account')
                return ''
            
            connect.commit()
            messagebox.showinfo('Successful Login', ' you have logged in successfully')

            display_dashboard()

        except Error as e:
            messagebox.showerror('Connection Error', f'There is error connecting to the server: {e}')
       
        finally:
            if connect.is_connected():
                cursor.close()
                connect.close()


def monie():
    registration = Frame(window, width=400, height=500, bg='light blue')
    registration.place(relx=0.5, rely=0.5, anchor='w')
    registration.pack_propagate(flag=False)

    contain_widget = Frame(registration,  padx=20, pady=25,bg=registration['bg'])
    contain_widget.place(relx=0.5, rely=0.5, anchor='center')

    labeluser= Label(contain_widget, text= "Sign up",bg=registration['bg'],  font=("Arial Bold", 42, "bold") ,padx=20, pady=25)
    labeluser.pack()

    labelusername = Label(contain_widget, text= "username", bg=registration['bg'], padx=30, pady=20)
    labelusername.pack()

    username_entry =Entry(contain_widget)
    username_entry.pack()

    labelemail = Label(contain_widget, text="Email", bg=registration['bg'], padx=30, pady=20)
    labelemail.pack()

    labelemail_entry = Entry(contain_widget)
    labelemail_entry.pack()

    labelpassword = Label(contain_widget, text= "Password", bg=registration['bg'], padx=30, pady=20)
    labelpassword.pack()

    labelpassword_entry = Entry(contain_widget, show="*")
    labelpassword_entry.pack()

    button = Button(contain_widget, text="Submit", bg=registration['bg'], command=lambda: validate_reg())
    button.pack()

    buttonlog = Button(contain_widget, text="Already have an account, login", command=lambda: login())
    buttonlog.pack()



    def validate_reg():
        username = username_entry.get()
        email = labelemail_entry.get()
        pwd = labelpassword_entry.get()
        
        if username == "":
            messagebox.showerror(title="Error", message="Invalid username")
            return ''
        
        if email == "":
            messagebox.showerror(title= "Error", message="Invalid Email")
            return ''
        
        if pwd == "":
            messagebox.showerror(title= "Error", message="password Invalid")
            return ''
        
        try:
            # create table
            create_table = ('CREATE TABLE IF NOT EXISTS loan_user(id_key INT PRIMARY KEY AUTO_INCREMENT, user_name '
                            'TEXT, email TEXT, password TEXT)')
            cursor.execute(create_table)

            # check for existing user
            get_existing_user = '''
            SELECT * FROM loan_user
            where email = %s
            '''

            cursor.execute(get_existing_user, (email,))

            available_user = cursor.fetchall()

            if available_user:
                messagebox.showerror('Existing User', 'There is an existing user with this mail, try using another mail')
                return ''
            
            # insert new user
            insert_user = 'INSERT INTO loan_user(user_name, email, password) values(%s, %s, %s)'
            user_entry_detail = (username, email, pwd)

            cursor.execute(insert_user, user_entry_detail)
            connect.commit()

            messagebox.showinfo("success", "Signup Successful")

            login()

        except Error as e:
            messagebox.showerror('Connection Error', f'There is trouble connecting to the server: {e}')

        finally:
            if connect.is_connected():
                cursor.close()
                connect.close()
            
    
monie()
mainloop()







        # else:
        #     try:
        #         connect = mysql.connector.connect(host='localhost', user="root", password='')
        #         cursor = connect.cursor()
        #     except:
        #         messagebox.showerror('Error', 'Unable to Connect to Server')
        #         return
        #     try:
        #         Query= 'create database waveproject'
        #         cursor.execute(Query)
        #         Query= 'use waveproject'
        #         cursor.execute(Query)
        #         Query= 'CREATE TABLE IF NOT EXISTS reguser (id int auto_increment primary key, username TEXT not null, email TEXT not null, password varchar(20) not null)'
        #         cursor.execute(Query)

        #     except:
        #         cursor.execute('use waveproject')

        # #     checking if user exists
        #         Query= "select * from logs where Username=%s and Email=%s"
        #         cursor.execute(Query, (username.get(), email.get()))

        #         old = cursor.fetchall()

        #         if old != None:
        #             messagebox.showerror('Error', 'User already exists')
                    
        #         else:
        #             Query= 'insert into logs(username, email, password) values (%s,%s,%s,%s,%s)'
        #             cursor.execute(Query,(username.get(), email.get(),pwd.get()))
            
        #             connect.commit()
        #             connect.close()
        #             messagebox.showinfo('Success', "Registration is Successful")