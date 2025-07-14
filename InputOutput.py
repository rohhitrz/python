name=input("Enter Your Name:")
print("hello ",name,"welcome");

#take multiple input in python

x,y=input("Enter two values: ").split();
x=int(x)
y=int(y)
print(f"the number of boys {x}")
print(f"the number of girls {y}")

# as we have seen split method, lets discuss that too

words="one,two,three"
print(words.split(',')) #it splits on basis of seprator

#splits a string into list of strings


# Print Float/Decimal Number in Python
price=float(input("Enter the price of rose:"))
print(price);

# Print Number in Python
n = int(input("How many roses?: "))
print(n)


# Find DataType of Input in Python

a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for":2, "Geeks":3}


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

#Output Formatting


#using sep paramater
print("X","Y","Z",sep="")
print("rohit","gmail.com",sep="@")
print(12,9,2004,sep="-")

#using end parameter

print("Welcome ", end = ' ')
print("Home", end= '\n')

for i in range(5):
    print(i, end=", ")

#using f-string

name="Rohit"
age=24
print(f"my name is {name} age is {age}")


#: Using % Operator
num = int(input("Enter a value: "))

add = num + 5

# Output
print("The sum is ", add)