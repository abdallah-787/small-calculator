num1 = float(input('enter the first number: '))
operator = input('enter the operator: ')
num2 = float(input('enter the seconde number: '))
if operator == '+':
   print(num1 + num2)
elif operator == '-':
   print(num1 - num2)
elif operator == '*':
   print(num1 * num2)
elif operator == '/':
   print(num1 / num2)
else:
   print('please enter(+ , - , * , /)')
