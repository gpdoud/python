my_name = "Greg"
your_name = 'Walter'
another_name = "O'Brien"

instruction = """
This is a multi-line string
where the others are only single
line strings.
"""

print("My name is", my_name, ", and your name is ", your_name)

my_name = "Gregory"

print("My name is", my_name, ", and your name is ", your_name)

a = 5
b = 7
c = a * b
print(a, " x ", b, " = ", c)

print(instruction)

print("This is one line\nThis is a second line")

a_long_string = "kskidfjlsldkjas;fjdjf;sjdf;ajdsf"
substring = "djxf"
does_exist = substring in a_long_string
print(does_exist)

str1 = "Hello"
str2 = "World"
hello_world = str1 + ", " + str2
print(hello_world)

a_string_of_10_characters = "abcdefghij"
the_length_is = len(a_string_of_10_characters)
print("The string", a_string_of_10_characters, "is",the_length_is, "characcter")

