class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return a / b
    
    def save_history(self, filename):
        file = open(filename, "w")
        for item in self.history:
            file.write(item + "\n")
        file.close()
    
    def __len__(self):
        return len(self.history)
    
    def __str__(self):
        return f"Calculator: {len(self.history)} operations"

calc = Calculator()

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show History")
    print("6. Save History")
    print("q. Quit")
    
    choice = input("Choose: ")
    
    if choice == "q":
        print("Goodbye!")
        break
    
    if choice == "5":
        if len(calc) == 0:
            print("History is empty!")
        else:
            for item in calc.history:
                print(item)
        continue
    
    if choice == "6":
        calc.save_history("history.txt")
        print("History saved!")
        continue
    
    if choice in ["1", "2", "3", "4"]:
        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
        except ValueError:
            print("Please enter numbers only!")
            continue
        
        try:
            if choice == "1":
                result = calc.add(a, b)
                op = "+"
            elif choice == "2":
                result = calc.subtract(a, b)
                op = "-"
            elif choice == "3":
                result = calc.multiply(a, b)
                op = "*"
            elif choice == "4":
                result = calc.divide(a, b)
                op = "/"
            
            record = f"{a} {op} {b} = {result}"
            calc.history.append(record)
            print(f"Result: {result}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
    else:
        print("Invalid choice!")
