import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create a basic GUI window
root = tk.Tk()
root.geometry("400x500")
root.title("Calculator")

# Create an Entry widget to display the input and results
entry = tk.Entry(root, font="lucida 20 bold")
entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

# Create buttons for the calculator
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

i = 0
for button in buttons:
    btn = tk.Button(button_frame, text=button, font="lucida 15 bold")
    btn.grid(row=i // 4, column=i % 4, padx=5, pady=5)
    btn.bind("<Button-1>", on_click)
    i += 1

root.mainloop()
