import tkinter as tk
class Calculator:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator App")
        self.root.geometry("400x500")
        
        # Create an entry field
        self.entry = tk.Entry(self.root, width=30, font=("Arial", 16), borderwidth=5, relief="ridge")
        self.entry.pack(pady=20)
        
        # create buttons using a loop
        self.create_buttons()
        self.root.mainloop()
        
        
    def create_buttons(self):
        button_texts = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", "c", "=", "+"]
        ]
        
        for row in button_texts:
            frame = tk.Frame(self.root)
            frame.pack()
            for text in row:
                button = tk.Button(frame, text=text, font=("Arial", 14), padx=20, pady=10, command=lambda t=text: self.on_button_click(t))
                button.pack(side=tk.LEFT, padx=5, pady=5)
    def on_button_click (self,char):
        if char== "c":
            self.entry.delete(0, tk.END)    
        elif char == "=":
            try:
                result=eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
            else:
                self.entry.insert(tk.END, char)
                
        
        def addition(self):
            pass
        
        def subtraction(self):
            pass
        
        def multiplication(self):
            pass
        
        def division(self):
            pass
        
        def sine(self):
            pass
        
        def cosine(self):
            pass
        
        def tangent(self):
            pass
        
        def arcsine(self):
            pass
        
        def arccos(self):
            pass
        
        def arctan(self):
            pass
        
        def square(self):
            pass
        
        def squareroot(self):
            pass
        
        def get_result(self):
            pass
        
app = Calculator()
app.root.mainloop()