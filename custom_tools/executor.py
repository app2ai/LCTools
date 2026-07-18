from add_tool import add
from mutltipy_tool import multiply

a = int(input("Enter number A: "))
b = int(input("Enter number B: "))

_dict = {'a':a, 'b':b}

addition = add.invoke(_dict)
multiplication = multiply.invoke(_dict) 
print("Answer:")
print("Add: ", addition)
print("Multiply: ", multiplication)
