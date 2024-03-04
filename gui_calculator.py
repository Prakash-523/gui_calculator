import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_backspace():
    current = entry.get()
    if current:
        entry.delete(len(current) - 1, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


window = tk.Tk()
window.title("Simple Calculator")

window.configure(bg='#00ffff')

entry = tk.Entry(window, width=30, borderwidth=5, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('.', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('⌫', 5, 1), ('C', 5, 2), ('%', 5, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(window, text=text, padx=20, pady=10, bg="#ff9500", fg="#ffffff", font=('Arial', 20), command=calculate)
    elif text == 'C':
        button = tk.Button(window, text=text, padx=20, pady=10, bg="#ff3b30", fg="#ffffff", font=('Arial', 20), command=button_clear)
    elif text == '⌫':
        button = tk.Button(window, text=text, padx=10, pady=10, bg="#4cd964", fg="#ffffff", font=('Arial', 20), command=button_backspace)
    else:
        button = tk.Button(window, text=text, padx=20, pady=10, bg="#dcdcdc", font=('Arial', 20), command=lambda t=text:button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

window.mainloop()
