from tkinter import *

class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("305x449")
        self.root.title("Calculator")
        self.frame = Frame(self.root, width=305, height=349)
        self.frame2 = Frame(self.root, width=327, height=100)
        self.frame.pack()
        self.frame2.pack()
        self.display_colour = "#f5f9fa"
        self.button_colour = "#f0f2f0"
        self.var = StringVar()
        self.action = ""
        self.run()

    def button(self):
        buttons = ["C", "%", "⌫", "/", "7", "8", "9", "x", "4", "5", "6", "-", "1", "2", "3", "+", "00", "0", ".", "="]
        i, j = 1, 0
        for a in buttons:
            keys = Button(self.frame2, text=f"{a}", width=4, height=1, bg=self.button_colour,
                          font=("Roboto", 22), borderwidth=0, command=lambda btn=a: self.keys_action(btn))
            keys.grid(row=i, column=j)
            j += 1
            if j == 4:
                i += 1
                j = 0

    def widgets(self):
        self.button()
        self.display = Label(self.frame, textvariable=self.var, width=305, height=5,
                             bg=self.display_colour,font=("Roboto", 20))
        self.display.pack()

    def keys_action(self, button):
        if button == "C":
            self.action = ""
        elif button == "⌫":
            self.action = self.action[:-1]
        elif button == "=":
            self.evaluate_expression()
        elif button == "%":
            self.calculate_percentage()
        elif button == "+":
            self.action += "+"
        elif button == "-":
            self.action += "-"
        elif button == "x":
            self.action += "*"
        elif button == "/":
            self.action += "/"
        else:
            self.action += button
        self.var.set(self.action)

    def evaluate_expression(self):
        try:
            result = eval(self.action)
            self.action = str(result)
        except ZeroDivisionError:
            self.action = "Cannot Divide by Zero"
        except SyntaxError:
            self.action = "Enter a Valid Input"

    def calculate_percentage(self):
        try:
            result = eval(self.action) / 100
            self.action = str(result)
        except SyntaxError:
            self.action = "Enter a Valid Input"

    def run(self):
        self.widgets()
        self.root.mainloop()

obj = Calculator()

