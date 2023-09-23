import tkinter as tk
from Calculator.ui import CalculatorUi

if __name__ == "__main__":
    root = tk.Tk()
    CalculatorUi(root, tk)
    root.mainloop()