import tkinter as tk
from tkinter import messagebox
import cmath

class ComplexCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Pro Complex Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.equation = ""
        self.display_var = tk.StringVar()

        self._build_ui()

    def _build_ui(self):
        # Display Screen
        display = tk.Entry(self.root, textvariable=self.display_var, font=("Arial", 24), 
                          bd=10, insertwidth=4, bg="#2c3e50", fg="white", justify='right')
        display.pack(fill="both", expand=True)

        # Button Layout
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '(',
            '1', '2', '3', '-', ')',
            '0', '.', 'j', '+', '=',
            'sin', 'cos', 'sqrt', 'log'
        ]

        grid = tk.Frame(self.root)
        grid.pack(fill="both", expand=True)

        row, col = 0, 0
        for btn in buttons:
            action = lambda x=btn: self._on_click(x)
            tk.Button(grid, text=btn, width=5, height=2, font=("Arial", 14),
                      command=action).grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 4:
                col = 0
                row += 1
        
        for i in range(5):
            grid.grid_columnconfigure(i, weight=1)
        for i in range(5):
            grid.grid_rowconfigure(i, weight=1)

    def _on_click(self, char):
        if char == '=':
            self._calculate()
        elif char == 'C':
            self.equation = ""
            self.display_var.set("")
        elif char in ['sin', 'cos', 'sqrt', 'log']:
            self._handle_math(char)
        else:
            self.equation += str(char)
            self.display_var.set(self.equation)

    def _calculate(self):
        try:
            # Python uses 'j' for imaginary numbers (e.g., 2+3j)
            # We evaluate the string as a Python expression
            result = eval(self.equation, {"__builtins__": None}, cmath.__dict__)
            self.display_var.set(result)
            self.equation = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            self.equation = ""

    def _handle_math(self, func):
        try:
            val = complex(eval(self.equation))
            if func == 'sin': res = cmath.sin(val)
            elif func == 'cos': res = cmath.cos(val)
            elif func == 'sqrt': res = cmath.sqrt(val)
            elif func == 'log': res = cmath.log(val)
            
            self.display_var.set(res)
            self.equation = str(res)
        except:
            messagebox.showerror("Error", "Input needed before function")

if __name__ == "__main__":
    root = tk.Tk()
    ComplexCalculator(root)
    root.mainloop()