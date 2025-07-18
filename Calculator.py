import math
import functools
import cmath

def calculator():
    print("===== Advanced Calculator =====")
    print("Choose an operation (type number or name):")
    options = {
        "1": "add", "2": "sub", "3": "multiple", "4": "divide", "5": "lcm",
        "6": "hcf", "7": "fact", "8": "marks", "9": "sqrt", "10": "cbrt",
        "11": "square", "12": "cube", "13": "complex", "14": "power",
        "15": "circle", "16": "rectangle", "17": "square_shape", "18": "table"
    }
    
    for num, name in options.items():
        print(f"{num}. {name}")

    choice = input("Enter operation number or name: ").strip().lower()
    op = options.get(choice, choice)  # allows both number or operation name

    if op in ['add', 'sub', 'multiple', 'divide']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if op == 'add':
            return f"Result: {num1 + num2}"
        elif op == 'sub':
            return f"Result: {num1 - num2}"
        elif op == 'multiple':
            return f"Result: {num1 * num2}"
        elif op == 'divide':
            return f"Result: {num1 / num2}" if num2 != 0 else "Error: Division by zero"

    elif op == 'lcm':
        nums = list(map(int, input("Enter numbers (space-separated): ").split()))
        lcm = functools.reduce(lambda a, b: abs(a * b) // math.gcd(a, b), nums)
        return f"LCM: {lcm}"

    elif op == 'hcf':
        nums = list(map(int, input("Enter numbers (space-separated): ").split()))
        hcf = functools.reduce(math.gcd, nums)
        return f"HCF: {hcf}"

    elif op == 'fact':
        num = int(input("Enter a non-negative integer: "))
        return f"Factorial: {math.factorial(num)}" if num >= 0 else "Error: Negative number"

    elif op == 'marks':
        n = int(input("Enter total number of subjects: "))
        marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(n)]
        total = sum(marks)
        percentage = total / (n * 100) * 100
        cgpa = percentage / 9.5
        print("Options: total / percentage / cgpa / sgpa / gpa")
        ask = input("What do you want to calculate? ").lower()
        if ask == "total":
            return f"Total Marks: {total} out of {n*100}"
        elif ask == "percentage":
            return f"Percentage: {percentage:.2f}%"
        elif ask == "cgpa":
            return f"CGPA: {cgpa:.2f}"
        elif ask in ['sgpa', 'gpa']:
            return f"{ask.upper()}: {cgpa:.2f}"
        else:
            return "Invalid marks option"

    elif op == 'sqrt':
        num = float(input("Enter number: "))
        return f"Square Root: {math.sqrt(num)}"

    elif op == 'cbrt':
        num = float(input("Enter number: "))
        return f"Cube Root: {num ** (1/3):.5f}"

    elif op == 'square':
        num = float(input("Enter number: "))
        return f"Square: {num ** 2}"

    elif op == 'cube':
        num = float(input("Enter number: "))
        return f"Cube: {num ** 3}"

    elif op == 'complex':
        a = complex(input("Enter first complex number (e.g. 3+4j): "))
        b = complex(input("Enter second complex number: "))
        op2 = input("Operation (+, -, *, /): ")
        if op2 == '+':
            return f"Result: {a + b}"
        elif op2 == '-':
            return f"Result: {a - b}"
        elif op2 == '*':
            return f"Result: {a * b}"
        elif op2 == '/':
            return f"Result: {a / b if b != 0 else 'Error: Division by zero'}"
        else:
            return "Invalid complex operation"

    elif op == 'power':
        base = float(input("Enter base: "))
        exp = float(input("Enter exponent: "))
        return f"{base}^{exp} = {pow(base, exp)}"

    elif op == 'circle':
        r = float(input("Enter radius: "))
        area = math.pi * r**2
        peri = 2 * math.pi * r
        return f"Area: {area:.2f}, Perimeter: {peri:.2f}"

    elif op == 'rectangle':
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        area = l * b
        peri = 2 * (l + b)
        return f"Area: {area}, Perimeter: {peri}"

    elif op == 'square_shape':
        s = float(input("Enter side length: "))
        return f"Area: {s**2}, Perimeter: {4*s}"

    elif op == 'table':
        n = int(input("Enter number: "))
        return "\n".join([f"{n} x {i} = {n*i}" for i in range(1, 11)])

    else:
        return "Invalid operation"


# 🔁 Run in loop until user chooses to exit
while True:
    print("\n" + "="*40)
    print(calculator())
    cont = input("\nDo you want to perform another operation? (yes/no): ").strip().lower()
    if cont not in ['yes', 'y']:
        print("Thank you for using the calculator!")
        break
