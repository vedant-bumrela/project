first = "Vedant"
last = "Kumar"

age = 20

print(f"Hello {first} {last}, you are {age} years old.")
print("Hello " + first + " " + last + ", you are " + str(age) + " years old.")
print("Hello {} {}, you are {} years old.".format(first, last, age))
print("Hello %s %s, you are %d years old." % (first, last, age))
print("Hello {0} {1}, you are {2} years old.".format(first, last, age))