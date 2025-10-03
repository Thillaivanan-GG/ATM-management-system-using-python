import tkinter as tk
from tkinter import messagebox, simpledialog
users = {"1234567890": ["1111", 10000], "Thillaivanan G G": ["7777", 5000]}

class ATM:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM")
        self.root.geometry("400x400")
        self.current_account = None
        self.pin_frame = tk.Frame(self.root)
        self.pin_frame.pack(pady=30)
        self.pin_label = tk.Label(self.pin_frame, text="Enter PIN:", font=("Arial", 14))
        self.pin_label.grid(row=0, column=0, padx=10, pady=10)
        self.pin_entry = tk.Entry(self.pin_frame, font=("Arial", 14), show="*")
        self.pin_entry.grid(row=0, column=1, padx=10, pady=10)
        self.pin_button = tk.Button(self.pin_frame, text="Submit", font=("Arial", 12), command=self.authenticate_pin)
        self.pin_button.grid(row=1, columnspan=2, pady=10)
    def authenticate_pin(self):
        pin = self.pin_entry.get()
        for account, data in users.items():
            if data[0] == pin:
                self.current_account = account
                self.pin_frame.pack_forget()  
                self.create_atm_ui()  
                messagebox.showinfo("Login Successful", f"Welcome back, User {account}!")
                return
        self.create_new_user()
    def create_new_user(self):
        new_account = simpledialog.askstring("New Account", "Enter your new account number:")       
        if new_account in users:
            messagebox.showerror("Account Exists", "Account number already exists. Please try another.")
            return
        new_pin = simpledialog.askstring("Set PIN", "Enter a 4-digit PIN:")       
        if len(new_pin) != 4 or not new_pin.isdigit():
            messagebox.showerror("Invalid PIN", "PIN must be a 4-digit number. Please try again.")
            return           
        users[new_account] = [new_pin, 0]
        self.current_account = new_account
        self.pin_frame.pack_forget()  
        self.create_atm_ui() 
        messagebox.showinfo("Welcome", f"Welcome to the ATM, New User {new_account}!")        
    def create_atm_ui(self):       
        self.atm_frame = tk.Frame(self.root)
        self.atm_frame.pack(pady=30)
        self.balance_label = tk.Label(self.atm_frame, text="Balance: ₹0.00", font=("Arial", 14))
        self.balance_label.pack(pady=10)
        self.balance_button = tk.Button(self.atm_frame, text="Check Balance", width=20, command=self.check_balance)
        self.balance_button.pack(pady=5)
        self.deposit_button = tk.Button(self.atm_frame, text="Deposit", width=20, command=self.deposit)
        self.deposit_button.pack(pady=5)
        self.withdraw_button = tk.Button(self.atm_frame, text="Withdraw", width=20, command=self.withdraw)
        self.withdraw_button.pack(pady=5)
        self.logout_button = tk.Button(self.atm_frame, text="Logout", width=20, command=self.logout)
        self.logout_button.pack(pady=10)
    def check_balance(self):
        balance = users[self.current_account][1]
        self.balance_label.config(text=f"Balance: ₹{balance:.2f}")
        messagebox.showinfo("Balance Inquiry", f"Your current balance is: ₹{balance:.2f}")
    def deposit(self):
        amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:", minvalue=1)
        if amount:
            users[self.current_account][1] += amount
            self.check_balance()
            messagebox.showinfo("Deposit", f"₹{amount} deposited successfully.")
    def withdraw(self):
        amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:", minvalue=1)
        if amount:
            if amount <= users[self.current_account][1]:
                users[self.current_account][1] -= amount
                self.check_balance()
                messagebox.showinfo("Withdraw", f"₹{amount} withdrawn successfully.")
            else:
                messagebox.showerror("Insufficient Balance", "You do not have sufficient balance to withdraw this amount.")
    
    def logout(self):
        self.current_account = None
        self.atm_frame.pack_forget()
        self.pin_frame.pack(pady=30)
if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()
