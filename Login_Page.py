import tkinter as tk
from tkinter import messagebox

def submit_patient_data():
    name = name_entry.get()
    age = age_entry.get()
    sex = sex_var.get()
    disorders = disorders_entry.get()
    location = location_entry.get()

    if name and age and sex != 'Select' and disorders and location:
        messagebox.showinfo("Patient Data", 
                            f"Name: {name}\nAge: {age}\nSex: {sex}\nDisorders: {disorders}\nLocation: {location}")
      
        data_entry_frame.pack_forget()
        param_selection_frame.pack(pady=20)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

def show_parameters(option):
    param_selection_frame.pack_forget()
    if option == 'three':
        params_label.config(text="Enter 3 Parameters")
        params = ['ECG', 'SpO2', 'RESP']
    else:
        params_label.config(text="Enter 5 Parameters")
        params = ['ECG', 'SpO2', 'RESP', 'NIBP', 'Temperature']

    for widget in params_frame.winfo_children():
        widget.destroy()

    for param in params:
        tk.Label(params_frame, text=param, font=('Arial', 12), bg='#f7f7f7').pack(anchor='w', padx=10, pady=5)
        tk.Entry(params_frame).pack(padx=10, pady=5)

    param_form_frame.pack(pady=20)


def submit_parameters():
    messagebox.showinfo("Parameters", "Parameters submitted!")
    param_form_frame.pack_forget()


root = tk.Tk()
root.title("Patient Data Entry")
root.geometry("500x600")
root.config(bg='#f7f7f7')


label_font = ("Arial", 14, "bold")
entry_font = ("Arial", 12)

data_entry_frame = tk.Frame(root, bg='#f7f7f7', padx=20, pady=20)
data_entry_frame.pack(pady=50)

tk.Label(data_entry_frame, text="Patient Data Entry", font=("Arial", 18, "bold"), bg='#f7f7f7').pack(pady=10)

tk.Label(data_entry_frame, text="Patient Name:", font=label_font, bg='#f7f7f7').pack(anchor='w')
name_entry = tk.Entry(data_entry_frame, width=30, font=entry_font)
name_entry.pack(pady=5)

tk.Label(data_entry_frame, text="Age:", font=label_font, bg='#f7f7f7').pack(anchor='w')
age_entry = tk.Entry(data_entry_frame, width=30, font=entry_font)
age_entry.pack(pady=5)

tk.Label(data_entry_frame, text="Sex:", font=label_font, bg='#f7f7f7').pack(anchor='w')
sex_var = tk.StringVar(value='Select')
sex_options = tk.OptionMenu(data_entry_frame, sex_var, 'Male', 'Female', 'Other')
sex_options.pack(pady=5)

tk.Label(data_entry_frame, text="Disease/Disorder:", font=label_font, bg='#f7f7f7').pack(anchor='w')
disorders_entry = tk.Entry(data_entry_frame, width=30, font=entry_font)
disorders_entry.pack(pady=5)

tk.Label(data_entry_frame, text="Location:", font=label_font, bg='#f7f7f7').pack(anchor='w')
location_entry = tk.Entry(data_entry_frame, width=30, font=entry_font)
location_entry.pack(pady=5)

tk.Button(data_entry_frame, text="Submit Data", command=submit_patient_data, bg="#4CAF50", fg="white", width=15, height=2).pack(pady=20)

param_selection_frame = tk.Frame(root, bg='#f7f7f7', padx=20, pady=20)

tk.Label(param_selection_frame, text="Select Monitoring Parameters", font=("Arial", 16, "bold"), bg='#f7f7f7').pack(pady=10)

tk.Button(param_selection_frame, text="3 Parameters", command=lambda: show_parameters('three'), bg="#007BFF", fg="white", width=20, height=2).pack(pady=10)
tk.Button(param_selection_frame, text="5 Parameters", command=lambda: show_parameters('five'), bg="#007BFF", fg="white", width=20, height=2).pack(pady=10)


param_form_frame = tk.Frame(root, bg='#f7f7f7', padx=20, pady=20)

params_label = tk.Label(param_form_frame, text="", font=("Arial", 16, "bold"), bg='#f7f7f7')
params_label.pack(pady=10)

params_frame = tk.Frame(param_form_frame, bg='#f7f7f7')
params_frame.pack()

tk.Button(param_form_frame, text="Submit Parameters", command=submit_parameters, bg="#4CAF50", fg="white", width=20, height=2).pack(pady=20)

root.mainloop()
