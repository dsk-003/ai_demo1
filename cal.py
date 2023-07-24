"""
Calculator Program.
"""

def add(num1,num2):
	print("Addition of both number is:",num1+num2)

def sub(n1,n2):
	print("Subtraction of {} and {} is {}.".format(n1,n2,(n1-n2)))

if __name__ == "__main__":
	num1 = int(input("Enter Number 1:"))
	num2 = int(input("Enter Number 2:"))
	
	print("----Addition in process-----")
	# write below your addition function
	add(num1,num2)
	
	print("----Subtraction in process----")
	# write below subtraction function
	sub(num1,num2)
