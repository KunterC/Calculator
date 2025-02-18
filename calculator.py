import tkinter as tk
import math
class Calculator:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator App")
        self.root.geometry("400x400")
        self.operator = "" #does the inner calculation
        self.field_text = tk.StringVar() #string variable in entry box
        self.display_text = "" #displays differently to the user

        self.entry = tk.Entry(self.root, textvariable=self.field_text, width=30, font=("Arial", 16), borderwidth=5, relief="ridge")
        self.entry.grid(row=1, column=1, columnspan=4)
        
        self.button_1 = tk.Button(self.root, text="1", command=lambda: self.add_to_field(1), width=5, bg="#FDFD96", font=('Arial', 15))
        self.button_1.grid(row=4, column=1)
        
        self.button_2 = tk.Button(self.root, text="2", command=lambda: self.add_to_field(2), width=5, bg="#FDFD96", font=('Arial', 15))
        self.button_2.grid(row=4, column=2)
        
        self.button_3 = tk.Button(self.root, text="3", command=lambda: self.add_to_field(3), width=5, bg="#FDFD96", font=('Arial', 15))
        self.button_3.grid(row=4, column=3)
        
        self.button_4 = tk.Button(self.root, text="4", command=lambda: self.add_to_field(4), width=5, bg="#FDFD96", font=('Arial', 15))
        self.button_4.grid(row=3, column=1)
        
        self.button_5 = tk.Button(self.root, text="5", command=lambda: self.add_to_field(5), width=5, bg="#FDFD96", font=('Arial', 15))
        self.button_5.grid(row=3, column=2)
        
        self.button_6 = tk.Button(self.root, text="6", command=lambda: self.add_to_field(6), width=5, bg="#FDFD96", font=('Arial', 15))
        self.button_6.grid(row=3, column=3)
        
        self.button_7 = tk.Button(self.root, text="7", command=lambda: self.add_to_field(7), width=5, bg="#FDFD96", font=('Arial', 15))
        self.button_7.grid(row=2, column=1)
        
        self.button_8 = tk.Button(self.root, text="8", command=lambda: self.add_to_field(8), width=5, bg="#FDFD96", font=('Arial', 15))
        self.button_8.grid(row=2, column=2)
        
        self.button_9 = tk.Button(self.root, text="9", command=lambda: self.add_to_field(9), width=5, bg="#FDFD96", font=('Arial', 15))
        self.button_9.grid(row=2, column=3)
        
        self.button_0 = tk.Button(self.root, text="0", command=lambda: self.add_to_field(0), width=5, bg="#FDFD96", font=('Arial', 15))
        self.button_0.grid(row=5, column=2)
        
        self.button_plus = tk.Button(self.root, text="+", command=lambda: self.add_to_field('+'), width=5, bg="#90EE90", font=('Arial', 15))
        self.button_plus.grid(row=4, column=4)
        
        self.button_minus = tk.Button(self.root, text="-", command=lambda: self.add_to_field('-'), width=5, bg="#90EE90", font=('Arial', 15))
        self.button_minus.grid(row=5, column=4)
        
        self.button_multiply = tk.Button(self.root, text="*", command=lambda: self.add_to_field('*'), width=5, bg="#90EE90", font=('Arial', 15))
        self.button_multiply.grid(row=3, column=4)
        
        self.button_divide = tk.Button(self.root, text="/", command=lambda: self.add_to_field('/'), width=5, bg="#90EE90", font=('Arial', 15))
        self.button_divide.grid(row=2, column=4)
        
        self.button_dot = tk.Button(self.root, text=".", command=lambda: self.add_to_field('.'), width=5, bg="#FFCCCB", font=('Arial', 15))
        self.button_dot.grid(row=5, column=1)
        
        self.button_open_paranthesis = tk.Button(self.root, text="(", command=lambda: self.add_to_field('('), width=5, bg="#FFCCCB", font=('Arial', 15))
        self.button_open_paranthesis.grid(row=6, column=1)
        
        self.button_close_paranthesis = tk.Button(self.root, text=")", command=lambda: self.add_to_field(')'), width=5, bg="#FFCCCB", font=('Arial', 15))
        self.button_close_paranthesis.grid(row=6, column=2)
        
        self.button_clear = tk.Button(self.root, text="Clear", command=lambda: self.clear(), width=5, bg="#FFCCCB", font=('Arial', 15))
        self.button_clear.grid(row=5, column=3)
        
        self.button_equals = tk.Button(self.root, text="=", command=lambda: self.calculate(), width=5, bg="#FFCCCB", font=('Arial', 15))
        self.button_equals.grid(row=6, column=3)
        
        self.button_square = tk.Button(self.root, text="x²", command=lambda: self.add_to_field("**2"), width=5, bg="#90EE90", font=('Arial', 15))
        self.button_square.grid(row=6, column=4)
        
        self.button_squareroot = tk.Button(self.root, text="√", command=lambda: self.add_to_field("**(1/2)"), width=5, bg="#90EE90", font=('Arial', 15))
        self.button_squareroot.grid(row=7, column=4)
        
        self.button_thirdroot = tk.Button(self.root, text="³√", command=lambda: self.add_to_field('**(1/3)'), width=5, bg="#90EE90", font=('Arial', 15))
        self.button_thirdroot.grid(row=8, column=4)
        
        self.button_power = tk.Button(self.root, text="^", command=lambda: self.add_to_field("**"), width=5, bg="#90EE90", font=('Arial', 15))
        self.button_power.grid(row=9, column=4)
        
        self.button_sin = tk.Button(self.root, text="sin", command=lambda: self.CalculateSin(), width=5, bg="light blue", font=('Arial', 15))
        self.button_sin.grid(row=7, column=1)
        
        self.button_cos = tk.Button(self.root, text="cos", command=lambda: self.CalculateCos(), width=5, bg="light blue", font=('Arial', 15))
        self.button_cos.grid(row=7, column=2)
        
        self.button_tan = tk.Button(self.root, text="tan", command=lambda: self.CalculateTan(), width=5, bg="light blue", font=('Arial', 15))
        self.button_tan.grid(row=7, column=3)
        
        self.button_cot = tk.Button(self.root, text="cot", command=lambda: self.CalculateCot(), width=5, bg="light blue", font=('Arial', 15))
        self.button_cot.grid(row=9, column=1)
        
        self.button_arccot = tk.Button(self.root, text="cot⁻¹", command=lambda: self.CalculateArccot(), width=5, bg="light blue", font=('Arial', 15))
        self.button_arccot.grid(row=9, column=2)
        
        self.button_arcsin = tk.Button(self.root, text="sin⁻¹", command=lambda: self.CalculateArcsin(), width=5, bg="light blue", font=('Arial', 15))
        self.button_arcsin.grid(row=8, column=1)
        
        self.button_arccos = tk.Button(self.root, text="cos⁻¹", command=lambda: self.CalculateArccos(), width=5, bg="light blue", font=('Arial', 15))
        self.button_arccos.grid(row=8, column=2)
        
        self.button_arctan = tk.Button(self.root, text="tan⁻¹", command=lambda: self.CalculateArctan(), width=5, bg="light blue", font=('Arial', 15))
        self.button_arctan.grid(row=8, column=3)
        
        self.button_factorial = tk.Button(self.root, text="!", command=lambda: self.CalculateFactorial(), width=5, bg="light blue", font=('Arial', 15))
        self.button_factorial.grid(row=9, column=3)

    def add_to_field(self, char):
        if not hasattr(self, "sqrt_stack"):
            self.sqrt_stack = []  #create list for square roots to keep track of if we're in a squareroot or not
        
        if not hasattr(self, "thrdroot_stack"):
            self.thrdroot_stack = []  #initialize the same list for third roots if it doesnt exist
    
        if char == "**(1/2)": #if squareroot is called
            self.display_text += "√(" #displays the squareroot symbol
            self.operator += "("  #adds opening bracket for the expression
            self.sqrt_stack.append(True)  #keeps track of the squareroot and increases track amount if nested
            
        elif char == "**(1/3)":  #if third root is calles
            self.display_text += "³√(" #display third root symbol
            self.operator += "("  #adds opening bracket
            self.thrdroot_stack.append(True)  #Tracks third root and how many there are
    
        elif char == ")": #when closing bracket is added
            self.display_text += ")"
            self.operator += ")"#adds it normally
            if self.sqrt_stack:  #checks if we're inside a square root
                self.operator += "**(1/2)"  #if we are, it adds **(1/2) to the end of the expression we want to squareroot
                self.sqrt_stack.pop() #pops the true out of the list. If nested, keeps adding and popping until no True statements left
            
            if self.thrdroot_stack:  #checks if we're inside a third root
                self.operator += "**(1/3)"  #adds the third root to the end of bracketed expression
                self.thrdroot_stack.pop() #removes the corresponding true value
                
        elif char == "**2":
            self.operator += "**2"
            self.display_text += "²"

        else:
            self.operator += str(char) #adds them to string and display if they are normal operators
            self.display_text += str(char)
            
        self.field_text.set(self.display_text) #displays text
        
    def CalculateSin(self):
        try: #change field texts to self.operator
            value = float(eval(self.operator)) #calculate result in operator 
            result = str(math.sin(math.radians(value))) #calculate sin in radians
            self.operator = result
            self.display_text = result
            self.field_text.set(self.display_text)
        except:
            self.field_text.set("Error")
    
    def CalculateCos(self):
        try: #change field texts to self.operator
            value = float(eval(self.operator)) #calculate result in operator
            result = str(math.cos(math.radians(value))) #calculate cos in radians
            self.operator = result
            self.display_text = result
            self.field_text.set(self.display_text)#evaluate when called but dont display it until = is hit
        except:
            self.field_text.set("Error")
    
    def CalculateTan(self):
        try: #change field texts to self.operator
            value = float(eval(self.operator)) #calculate result in operator
            result = str(math.tan(math.radians(value))) #calculate tan in radians
            self.operator = result
            self.display_text = result 
            self.field_text.set(self.display_text)
        except:
            self.field_text.set("Error")
            
    def CalculateCot(self):
        try:
            value = float(eval(self.operator)) #calculate result in operator
            result = str(1/math.tan(math.radians(value))) #get the reciprocal of the tan value in radians
            self.operator = result
            self.display_text = result 
            self.field_text.set(self.display_text)
        except:
            self.field_text.set("Error")   
            
    def CalculateArcsin(self):
        try: #change field texts to self.operator
            value = float(eval(self.operator)) #calculate result in operator
            result = str(math.degrees(math.asin(value))) #calculate arcsin of entered input
            self.operator = result
            self.display_text = result 
            self.field_text.set(self.display_text)
        except:
            self.field_text.set("Error")
    
    def CalculateArccos(self):
        try: #change field texts to self.operator
            value = float(eval(self.operator)) #calculate result in operator
            result = str(math.degrees(math.acos(value))) #calculate arccos of entered input in degrees
            self.operator = result
            self.display_text = result 
            self.field_text.set(self.display_text)
        except:
            self.field_text.set("Error")
    
    def CalculateArctan(self):
        try: #change field texts to self.operator
            value = float(eval(self.operator)) #calculate result in operator
            result = str(math.degrees(math.atan(value))) #calculate arctan of entered input in degrees
            self.operator = result
            self.display_text = result 
            self.field_text.set(self.display_text)
        except:
            self.field_text.set("Error")
            
    def CalculateArccot(self):
        try: #change field texts to self.operator
            value = float(eval(self.operator)) #calculate result in operator
            result = str(math.degrees(math.atan(1/value))) #calculate arctan of reciprocal value in degrees
            self.operator = result
            self.display_text = result 
            self.field_text.set(self.display_text)
        except:
            self.field_text.set("Error")
            
    def CalculateFactorial(self):
        try: #change field texts to self.operator
            value = int(eval(self.operator)) #calculate result in operator
            result = str(math.factorial(value)) #calculate arctan of reciprocal value in degrees
            self.operator = result
            self.display_text = result 
            self.field_text.set(self.display_text)
        except:
            self.field_text.set("Error")

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