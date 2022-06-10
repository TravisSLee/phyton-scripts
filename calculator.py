import re
import sys 

input_arr=[0,1]

class SimpleCalculator:
    
    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)
        
    def add(self):
        first = self.num1
        second = self.num2
        sum = first + second
        print("The sum of these two numbers are " + str(sum) + ".")
    
    def subtract(self):
        first = self.num1
        second = self.num2
        sum = first - second
        print("The sum of these two numbers are " + str(sum) + ".")
        
    def multiply(self):
        first = self.num1
        second = self.num2
        product = first * second
        print("The product of these two numbers are " + str(product) + ".")
        
    def divide(self):
        first = self.num1
        second = self.num2
        product = first / second
        print("The product of these two numbers are " + str(product) + ".")
        
def ask_for_nums():
    good_input = False
    print("Please select two numbers.")
    for i in input_arr:
        
        while good_input == False:
            ipt = input("Chose a number or type exit: ")
            
            if ipt.lower() == "exit":
                sys.exit("You are exiting. Goodbye!") 
            elif re.search("[a-zA-Z]", ipt):  
                print("That's not an int!")
            else:
                input_arr[i] = int(ipt)
                break

    return input_arr

def ask_for_op(obj):
    good_input = False
    
    while good_input == False:
        usr_input = input("What do you want to do? +, -, x, /, or exit? ")
        if usr_input == "+":
            obj.add()
            break
        elif usr_input == "-":
            obj.subtract()
            break
        elif usr_input == "x":
            obj.multiply()
            break
        elif usr_input == "/":
            obj.divide()
            break
        elif usr_input.lower() == "exit":
            sys.exit("You are exiting. Goodbye!")
        else:
            print("I'm sorry. I don't understand. Please try again.")
            
ask_for_nums()

one, two = input_arr

c = SimpleCalculator(one, two)

ask_for_op(c)
