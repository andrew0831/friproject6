import tkinter as tk

# Main window
root = tk.Tk()
root.title("Calculator")

# Entry box
entry_box = tk.Entry(root, width=20, borderwidth=0, state="disabled", disabledforeground="black", disabledbackground="white")
entry_box.pack(pady=10)

# Button definitions
button_definitions = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+')
]

# Buttons
for row in button_definitions:
    button_frame = tk.Frame(root)
    button_frame.pack()
    for button_text in row:
        button = tk.Button(button_frame, text=button_text, padx=20, pady=10, font=("Arial", 12), command=lambda bt=button_text:(bt))
        button.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
