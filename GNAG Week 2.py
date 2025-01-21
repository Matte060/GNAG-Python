'''
GNAG Computer Science Week 2!

The Print Function!

The print function is essentially the computer's mouth, it tells the computer to show whatever we ask it to
Like we talked about last week, functions often require additional information.
The print function requires us to tell it what to print otherwise it does nothing
'''

# Ex:
print()
#
'''
The first thing everyone does when they begin a language is they print "Hello World"
When we print something we put it into between quotation (" ").
That tells the computer we want to print exactly that!
'''

# Ex:
print("Hello World")
# Hello World

'''
To run/execute the program we press the play button in the top right corner!

ACTIVITY:
Print anything you want, it can be your name, your favourite sport, your favourite colour, or even all 3!
Once you're done, try to help your friends around you!
'''

'''
VARIABLES!!! The most important part of programming!
Variables act as the computer's memory, they store information so we can use it later.

We save variables in python by adding them in our script.
We don't put them in between quotations because we're adding them to the memory of program.
'''

# Ex:
# This variable is called name and currently stores my name:
name = "Matteo"

#Question: What will happen when we run both of these lines of code?
print("name")
print(name)

''''
There are 5 kinds of Variables:
1. Characters: a single piece of visual information, the computer saves information on what it looks like.
               These are put in between quotations in order to distinguish them.
Ex: favLetter = "d" 

2. Strings: a collection of character variables, again visual information.
Ex: favWord = "Donkey"

3. Integers: a number, with no decimals. 
             These are saved as real information.
             This means the computer treats it like the number not just a collection of pixels
             We'll talk about math next week.
             We don't need to add quotations because the computer can recognize numbers without the quotations.
Ex: x = 4

4. Floats: a number with decimals.
Ex: x = 3.99

When we turn a float into a decimal, it will only take the whole number from the float.
'''
#Ex:
x = 3.99
print(int(x))


'''
5. Boolean Variables / True/False Variables: a variable with one of two values T/F
                                             you don't need to use quotations when defining as python recognizes
                                             True and False
Ex: fun = True


When we name variables we have to follow certain rules:
A variable name must start with a letter or the underscore character (Can only be one word)
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

For clarity it is also best to being a variable name with a lower case letter
'''

'''
Question: Which of the following are invalid variable names?
favSport = "Hockey"
name = "Matteo"
purple mansion = True
1number = 60
print = "My name is Matteo, my favourite sport is hockey, my favourite number is 60,
and I live in a purple mansion"
'''

'''
ACTIVITY:
Create a variable called name and assign it the value of your name
Print the variable name
Once you're done, try to help your friends around you!
'''

'''
Why we use variables?
Sometimes it's important to update the value of variable, but be careful, variables update throughout the file!
Sometimes we need multiple variable
Sometimes it's important to change information based on the person you're asking (We'll get to that soon)!
'''
# Ex:
# We're going to make a variable about me
# We'll start by making it nothing and update it as we go
matteo = False

# We'll first make it my age
matteo = 22
print("Matteo is ", matteo, " years old")

#Then we'll make it my favourite sport
matteo = "hockey"
print("Matteo really likes ", matteo)

#Finally we'll make it my favourite food
matteo = "hamburgers"
print("Matteo really likes ", matteo, " they're super yummy!")

#Question: What will show if I run:
print("Matteo is ", matteo, " years old, his favourite sport is ", matteo, " and his favourite food is", matteo)

