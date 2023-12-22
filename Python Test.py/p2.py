#The function is basically a block of code that performs a specific task and can be used in different parts of the program.

def add(x, y): # x, y = PARAMETERS
  
  sum = x + y
  return sum

a = 10
b = 20
sum1 = add(a, b) # a, b = ARGUMENTS 
print (sum1)

p = 40
q = 50
sum2 = add(p, q) # p, q = ARGUMENTS 
print(sum2)


'''
IMPORTANT POINTS TO REMEMBER

-If the function is not called, the function will be present but will not work
-This is why the execution of the program does not start from "def".
-Variables in arguments and parameters correspond to each other in order
-Variables' names in arguments are corresponding parameters do not have to be same
'''