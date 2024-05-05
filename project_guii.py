from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

import mysql.connector
from mysql.connector import Error

connect = mysql.connector.connect( host='localhost', password="", user='root', database='l')
cursor = connect.cursor()

# Set up the main window
root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
size = str(width) + 'x' + str(height)
root.geometry(size)


root.title("Check Eligibility")
  

background_image = Image.open("/Users/macbookpro/Desktop/NIIT/Gui/monie.jpg")
resize_image = background_image.resize((width, height))
background_photo = ImageTk.PhotoImage(image=resize_image)
background_label = Label(root, image=background_photo)
background_label.pack()



def check_eligibility():
        try:
            age = int(age_spinbox.get())
            income = float(income_entry.get())
            amount_to_borrow = float(amount_entry.get())
            if age >= 18 and income >= 30000 and amount_to_borrow >= 30000:
                root.withdraw()
                open_repayment_window(root)
            else:
                messagebox.showwarning("Eligibility",
                                       "Sorry, you do not meet the eligibility criteria. Your income should be greater than 30,000 as well as amount to borrow")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for income and amount to borrow.")


# Eligibility check frame
eligible_frame = Frame(root, padx=5, pady=5, bg=root['bg'])
eligible_frame.place(relx=0.5, rely=0.5, anchor='center')

# Age label and spinbox
age_label = Label(eligible_frame, text="Age:", width=20)
age_label.pack()
age_spinbox = Spinbox(eligible_frame, from_=18, to=100, width=30)
age_spinbox.pack()

# Income label and entry
income_label = Label(eligible_frame, text="Monthly Income (₦):", width=20)
income_label.pack()
income_entry = Entry(eligible_frame, width=30)
income_entry.pack()

# Amount to borrow label and entry
amount_label = Label(eligible_frame, text="Amount to Borrow (₦):", width=20)
amount_label.pack()
amount_entry = Entry(eligible_frame, width=30)
amount_entry.pack()

# Check eligibility button
check_button = Button(eligible_frame, text="Check Eligibility", width=20, command=check_eligibility)
check_button.pack()

    # Add padding to all child widgets within the frame
for child in eligible_frame.winfo_children():
    child.pack_configure(pady=5)


# Functions to open and resize child windows
def open_repayment_window(root):
    repayment_window = Toplevel()
    repayment_window.title("Terms and Conditions")
      # Set window size to full screen
    # Terms and conditions content (replace with actual terms)
    try:
        background_image = Image.open("/Users/macbookpro/Desktop/NIIT/Gui/monie.jpg")
        resize_image = background_image.resize((width, height))
        background_photo = ImageTk.PhotoImage(image=resize_image)
        background_label = Label(root, image=background_photo)
        background_label.place(relwidth=1, relheight=1)
    except FileNotFoundError:
        print("Background image not found. Window will have default background.")

    content_text = """TERMS AND CONDITIONS 
        These Terms and Conditions apply to and regulate the provision of financial services provided by Loanify, a digital microfinance bank that is licensed by the Central Bank of Nigeria (CBN) which provides financial services
    via its flagship mobile app – Loanify™️ to the Customer herein.
    These Terms and Conditions constitute Loanify’s offerings and set out the terms governing this Agreement.

    By registering for a Loanify Account or using any of the services provided on the Loanify App, you agree to comply with all of the terms and conditions in this user agreement.
    You also agree to comply with the following additional policies that apply to you:

    * Privacy Policy
    * Acceptable Use Policy
    * Consent to Receive Electronic Disclosures (E-Sign Disclosure and Consent)

    We may revise this user agreement and any of the policies listed above from time to time.
    The revised version will be effective at the time we post it, unless otherwise noted.

    By continuing to use our services after any changes to this user agreement become effective, you agree to abide and be bound by those changes.
    If you do not agree to these terms and conditions, please do not proceed and exit the application immediately.
    Please be informed that on notice to you, we can terminate your relationship with us if we believe that you have violated any of these terms."""
    content_label = Label(repayment_window, text=content_text, justify="center", wraplength=550)
    content_label.pack(side="top", fill="both", expand= "True")

    proceed_button = Button(repayment_window, text="Agree",
                            command=lambda: open_applicant_details_window(repayment_window))
    proceed_button.pack(pady=(0, 1))


def open_bank_details_window(parent_window):
    bank_details_window = Toplevel(parent_window)
    bank_details_window.title("Bank Account Details")
    bank_details_window.geometry('600x400')  # Set window size to full screen
    # Widget positioning
    label_width = 100
    entry_width = 200
    row_spacing = 40
    column_spacing = 10
    top_padding = 50
    left_padding = 50
    try:
        background_image = Image.open("background.jpeg")
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = Label(root, image=background_photo)
        background_label.place(relwidth=1, relheight=1)
    except FileNotFoundError:
        print("Background image not found. Window will have default background.")

    

    # Content frame
    content_frame = Frame(bank_details_window)
    content_frame.pack(fill='both', expand=True, anchor='center')
    # eligible_frame = Frame(root, padx=5, pady=5, bg=root['bg'])
    # eligible_frame.place(relx=0.5, rely=0.5, anchor='center')
    # Positioning widgets using place
    Label(content_frame, text="Bank Name:").place(x=left_padding, y=top_padding, width=label_width, height=25)
    bank_name_combobox = ttk.Combobox(content_frame, values=[
        "Access Bank", "Access Diamond Bank", "EcoBank Nigeria", "Fidelity Bank",
        "First Bank of Nigeria", "First City Monument Bank (FCMB)", "Guaranty Trust Bank (GTB)",
        "Heritage Bank", "Jaiz Bank", "Keystone Bank", "Kuda Microfinance Bank", "Monie point",
        "Opay", "Palmpay Limited", "Polaris Bank", "Providus Bank", "Stanbic IBTC Bank",
        "Sterling Bank", "Union Bank of Nigeria", "United Bank for Africa (UBA)", "Unity Bank"
    ], width=17)
    bank_name_combobox.place(x=left_padding + label_width + column_spacing, y=top_padding, width=entry_width, height=25)

    Label(content_frame, text="Account Number:").place(x=left_padding, y=top_padding + row_spacing, width=label_width,
                                                       height=25)
    account_number_entry = Entry(content_frame, width=20)
    account_number_entry.place(x=left_padding + label_width + column_spacing, y=top_padding + row_spacing,
                               width=entry_width, height=25)

    Label(content_frame, text="Account Name:").place(x=left_padding, y=top_padding + 2 * row_spacing, width=label_width,
                                                     height=25)
    account_name_entry = Entry(content_frame, width=20)
    account_name_entry.place(x=left_padding + label_width + column_spacing, y=top_padding + 2 * row_spacing,
                             width=entry_width, height=25)

    submit_button = Button(content_frame, text="Submit",
                           command=lambda: validate_bank_details(bank_name_combobox.get(), account_number_entry.get(),
                                                                 account_name_entry.get()))
    submit_button.place(x=left_padding + label_width + column_spacing, y=top_padding + 3 * row_spacing, width=80,
                        height=30)


def validate_bank_details(bank_name, account_number, account_name):
    if bank_name and len(account_number) == 10 and account_name:
        messagebox.showinfo("Success",
                            "Your account has successfully been credited. Kindly check your bank app. Please repay your loan on or before the due date to avoid further embarrassment.")
        parent_window.destroy()
    else:
        messagebox.showerror("Error", "Please provide your correct bank details to proceed.")


def parent_window():
    pass


def validate_applicant_details(full_name, address, state, mobileNo, id_number, employment_status, business):
    try:
        if all([full_name, address, state, employment_status, business]) and len(mobileNo) == 11 and len(
                id_number) == 11:
            open_bank_details_window(parent_window())
        else:
            messagebox.showerror("Error", "All informations must be filled completely, Phone number and id number must equal the right digit(11).")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for mobileNo and idnumber.")

def open_applicant_details_window(previous_window):
    previous_window.destroy()
    details_window = Toplevel(root)
    details_window.title("Applicant Details")
    details_window.geometry('600x400')  # Set window size to full screen
    # This frame holds all content



    # background_image = Image.open("was.jpeg")
    # background_photo = ImageTk.PhotoImage(background_image)
    # background_label = Label(root, image=background_photo)
    # background_label.place(relwidth=1, relheight=1)
    # img=PhotoImage(file='was.jpeg')
    # Label(details_window, image=img, border=0, bg='white').place(x=50,y=90)

    content_frame = Frame(details_window, padx=20, pady=30)
    content_frame.pack(fill='both', expand=True)

    # Calculate positions for widgets
    label_width = 100
    entry_width = 200
    vertical_padding = 30
    horizontal_padding = 20
    row_height = 35

    # instruction = '''
    #   Please fill out the following form to apply for a loan. \nEnsure all required fields are completed accurately.
    #   '''
    content_text = "KINDLY FILL IN YOUR CORRECT BANK DETAILS"

    # Title
    Label(content_frame, text="Title:").place(x=30, y=5)
    ttk.Combobox(content_frame, values=["Mr", "Mrs", "Miss"], width=17).place(x=120, y=5)

    # Full Name
    Label(content_frame, text="Full Name:").place(x=30, y=1 * row_height + vertical_padding)
    full_name_entry = Entry(content_frame, width=30)
    full_name_entry.place(x=120, y=1 * row_height + vertical_padding)

    # Address
    Label(content_frame, text="Address:").place(x=30, y=2 * row_height + vertical_padding * 2)
    address_entry = Entry(content_frame, width=30)
    address_entry.place(x=120, y=2 * row_height + vertical_padding * 2)

    # State
    Label(content_frame, text="State:").place(x=30, y=3 * row_height + vertical_padding * 3)
    state_combobox = ttk.Combobox(content_frame, values=["Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi",
                                                         "Bayelsa", "Benue", "Borno", "Cross River", "Delta",
                                                         "Ebonyi", "Edo", "Ekiti", "Enugu", "Gombe",
                                                         "Imo", "Jigawa", "Kaduna", "Kano", "Katsina",
                                                         "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa",
                                                         "Niger", "Ogun", "Ondo", "Osun", "Oyo",
                                                         "Plateau", "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara",
                                                         "Federal Capital Territory"], width=17)
    state_combobox.place(x=120, y=3 * row_height + vertical_padding * 3)

    # Mobile No
    Label(content_frame, text="Mobile No:").place(x=30, y=4 * row_height + vertical_padding * 4)
    mobileNo_entry = Entry(content_frame, width=30)
    mobileNo_entry.place(x=120, y=4 * row_height + vertical_padding * 4)

    # ID Number / NIN
    Label(content_frame, text="I.D Number / Nin:").place(x=30, y=5 * row_height + vertical_padding * 5)
    id_number_entry = Entry(content_frame, width=30)
    id_number_entry.place(x=130, y=5 * row_height + vertical_padding * 5)

    # Employment Details
    Label(content_frame, text="Employment Status:").place(x=30, y=6 * row_height + vertical_padding * 6)
    employment_status_combobox = ttk.Combobox(content_frame, values=["Employed", "Self-employed", "Unemployed"],
                                              width=17)
    employment_status_combobox.place(x=140, y=6 * row_height + vertical_padding * 6)

    # Business / Job Title
    Label(content_frame, text="Business / Job Title:").place(x=30, y=7 * row_height + vertical_padding * 7)
    business_entry = Entry(content_frame, width=30)
    business_entry.place(x=140, y=7 * row_height + vertical_padding * 7)

    # Apply Button
    submit_button = Button(content_frame, text="Apply", command=lambda: validate_applicant_details(
        full_name_entry.get(),
        address_entry.get(),
        state_combobox.get(),
        mobileNo_entry.get(),
        id_number_entry.get(),
        employment_status_combobox.get(),
        business_entry.get()))
    submit_button.place(x=120, y=8 * row_height + vertical_padding * 8)
    previous_window.destroy()

root.mainloop()