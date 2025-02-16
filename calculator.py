import tkinter as tk
import re  # Import regex to detect the last number

class Calculator:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator App")
        self.root.geometry("400x500")
        self.operator = "" #does the inner calculation
        self.field_text = tk.StringVar() #string variable in entry box
        self.display_text = "" #displays differently to the user

        self.entry = tk.Entry(self.root, textvariable=self.field_text, width=30, font=("Arial", 16), borderwidth=5, relief="ridge")
        self.entry.grid(row=1, column=1, columnspan=5)
        
        self.button_1 = tk.Button(self.root, text="1", command=lambda: self.add_to_field(1), width=5, font=('Arial', 15))
        self.button_1.grid(row=4, column=1)
        
        self.button_2 = tk.Button(self.root, text="2", command=lambda: self.add_to_field(2), width=5, font=('Arial', 15))
        self.button_2.grid(row=4, column=2)
        
        self.button_3 = tk.Button(self.root, text="3", command=lambda: self.add_to_field(3), width=5, font=('Arial', 15))
        self.button_3.grid(row=4, column=3)
        
        self.button_4 = tk.Button(self.root, text="4", command=lambda: self.add_to_field(4), width=5, font=('Arial', 15))
        self.button_4.grid(row=3, column=1)
        
        self.button_5 = tk.Button(self.root, text="5", command=lambda: self.add_to_field(5), width=5, font=('Arial', 15))
        self.button_5.grid(row=3, column=2)
        
        self.button_6 = tk.Button(self.root, text="6", command=lambda: self.add_to_field(6), width=5, font=('Arial', 15))
        self.button_6.grid(row=3, column=3)
        
        self.button_7 = tk.Button(self.root, text="7", command=lambda: self.add_to_field(7), width=5, font=('Arial', 15))
        self.button_7.grid(row=2, column=1)
        
        self.button_8 = tk.Button(self.root, text="8", command=lambda: self.add_to_field(8), width=5, font=('Arial', 15))
        self.button_8.grid(row=2, column=2)
        
        self.button_9 = tk.Button(self.root, text="9", command=lambda: self.add_to_field(9), width=5, font=('Arial', 15))
        self.button_9.grid(row=2, column=3)
        
        self.button_0 = tk.Button(self.root, text="0", command=lambda: self.add_to_field(0), width=5, font=('Arial', 15))
        self.button_0.grid(row=5, column=1)
        
        self.button_plus = tk.Button(self.root, text="+", command=lambda: self.add_to_field('+'), width=5, font=('Arial', 15))
        self.button_plus.grid(row=4, column=4)
        
        self.button_minus = tk.Button(self.root, text="-", command=lambda: self.add_to_field('-'), width=5, font=('Arial', 15))
        self.button_minus.grid(row=5, column=4)
        
        self.button_multiply = tk.Button(self.root, text="*", command=lambda: self.add_to_field('*'), width=5, font=('Arial', 15))
        self.button_multiply.grid(row=3, column=4)
        
        self.button_divide = tk.Button(self.root, text="/", command=lambda: self.add_to_field('/'), width=5, font=('Arial', 15))
        self.button_divide.grid(row=2, column=4)
        
        self.button_dot = tk.Button(self.root, text=".", command=lambda: self.add_to_field('.'), width=5, font=('Arial', 15))
        self.button_dot.grid(row=5, column=2)
        
        self.button_open_paranthesis = tk.Button(self.root, text="(", command=lambda: self.add_to_field('('), width=5, font=('Arial', 15))
        self.button_open_paranthesis.grid(row=6, column=1)
        
        self.button_close_paranthesis = tk.Button(self.root, text=")", command=lambda: self.add_to_field(')'), width=5, font=('Arial', 15))
        self.button_close_paranthesis.grid(row=6, column=2)
        
        self.button_clear = tk.Button(self.root, text="Clear", command=lambda: self.clear(), width=5, font=('Arial', 15))
        self.button_clear.grid(row=5, column=3)
        
        self.button_equals = tk.Button(self.root, text="=", command=lambda: self.calculate(), width=5, font=('Arial', 15))
        self.button_equals.grid(row=6, column=4)
        
        self.button_square = tk.Button(self.root, text="x²", command=lambda: self.add_to_field("**2"), width=5, font=('Arial', 15))
        self.button_square.grid(row=7, column=4)
        
        self.button_squareroot = tk.Button(self.root, text="√x", command=lambda: self.add_to_field("**0.5"), width=5, font=('Arial', 15))
        self.button_squareroot.grid(row=8, column=4)
        
        # self.button_sin = tk.Button(self.root, text="sin", command=self.CalculateSin(), width=5, font=('Arial', 15))
        # self.button_sin.grid(row=7, column=1)
        
        # self.button_cos = tk.Button(self.root, text="cos", command=self.CalculateCos(), width=5, font=('Arial', 15))
        # self.button_cos.grid(row=7, column=2)
        
        # self.button_tan = tk.Button(self.root, text="tan", command=self.CalculateTan(), width=5, font=('Arial', 15))
        # self.button_tan.grid(row=7, column=3)
        
        # self.button_arcsin = tk.Button(self.root, text="arcsin", command=lambda: self.add_to_field("arcsin("), width=5, font=('Arial', 15))
        # self.button_arcsin.grid(row=8, column=1)
        
        # self.button_arccos = tk.Button(self.root, text="arccos", command=lambda: self.add_to_field("arccos("), width=5, font=('Arial', 15))
        # self.button_arccos.grid(row=8, column=2)
        
        # self.button_arctan = tk.Button(self.root, text="arctan", command=lambda: self.add_to_field("arctan("), width=5, font=('Arial', 15))
        # self.button_arctan.grid(row=8, column=3)

    def add_to_field(self, char):
        if char == "**0.5":
            #uses regex library to look for patterns in self.operator. This is a pattern that looks
            #for bracketed expressions or the last number if it is called in a bracketed expression.
            match = re.search(r"(\([^()]*\)|\d+\.?\d*)\s*$", self.operator) #looks for the last number or bracketed expression
            #if finds a number or bracketed expression, puts the sqrt sign before it
            if match:
                last_number = match.group(1) #gets the last number or bracketed expression
                self.operator = self.operator[: -len(last_number)] + f"({last_number})**0.5" #puts the **0.5 to the end of the last number or brackets
                self.display_text = self.display_text[: -len(last_number)] + f"√{last_number}" #displays the squareroot sign before the last number or expression
            else: #displays it normally if no brackets are written
                self.operator = f"({self.operator})**0.5"
                self.display_text = f"√({self.display_text})"
    
        elif char == "**2":
            match = re.search(r"(\([^()]*\)|\d+\.?\d*)\s*$", self.operator) #looks for brackets and last number again
            
            if match: #if it finds brackets
                last_number = match.group(1) #groups the brackets
                self.operator = self.operator[: -len(last_number)] + f"({last_number})**2"
                self.display_text = self.display_text[: -len(last_number)] + f"{last_number}²"
            else:
                self.operator = f"{self.operator}**2"
                self.display_text = f"{self.display_text}²"
                
        elif char == "(":
            self.operator += "("
            self.display_text += "("
        
        elif char == ")":
            self.operator += ")"
            self.display_text += ")"
        
        else:
            self.operator += str(char) #adds them to string and display if they are normal operators
            self.display_text += str(char)
    
        self.field_text.set(self.display_text) #displays text
        
    def CalculateSin(self):
        pass
    
    def CalculateCos(self):
        pass
    
    def CalculateTan(self):
        pass

    def calculate(self):
        try:
            temp = str(eval(self.operator))  #evaluates the final string
            self.field_text.set(temp)  
            self.operator = temp  
            self.display_text = temp  #sets everything to the result
        except Exception:
            self.field_text.set("Error") #displays error if evaluation fails
            self.operator = ""
            self.display_text = "" #clears strings
            
    def clear(self):
        self.operator = "" #clears strings and entry fields if clear button is pressed
        self.display_text =""
        self.field_text.set(self.display_text)
        
    
    
    

app = Calculator()
app.root.mainloop()