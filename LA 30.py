import tkinter as tk

root = tk.Tk()
root.title("OOP")
root.geometry("500x400")
root.configure(bg ="red")

frame = tk.Frame(root)
frame.pack(pady=20)

anime_title = "Dandadan"
def display_text():
    global anime_title
    print(f"My favorite anime is {anime_title} ")
    

button = tk.Button(frame, text=f"Press it", command=display_text)
button.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()