import tkinter as tk

your_name = "JOHN_LESTER_OROLA"
your_section = "BSIT 2B"
root = tk.Tk()
root.title("OOP")
root.geometry("500x400")
root.configure(bg ="red")

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text=f"OOP LA29 {your_name} {your_section}")
label.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()
