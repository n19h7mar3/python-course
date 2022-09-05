# Functions reference

> Functions in python are used to implement logic that you want to execute repeatedly at different places in your code.

- A function is a **block of code** which only **runs when it is called**
- You can **pass data** into a function, known as **parameters**/**arguments**
- A function can **return data** as a result

## Creating a function
- In python, a function is defined using the `def` keyword
```python
def my_function():   # <-- This line is called the `function header`
    print("Hello from a function")
```

## Calling a function
- To **run the code** inside a function, you need to **call** it
  - A function is **called using** the **function name** followed by **parenthesis**
```python
def my_function():
    print("Hello from a function")

my_function()   # <-- Function call
```

## Arguments
- **Data** can be **passed into functions** as **arguments**.
>
- Arguments are **specified** after the function name, **inside the parenthesis**
  - You can **add as many arguments** as you want, just **separate** them with a **comma**.
>
The following example has a function with **one argument** (fname)
  - When the function is called, we **pass along** a **first name**, which is used inside the function to **print the full name**
```python
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")     # <-- will print "Emil Refsnes"
my_function("Linus")    # <-- will print "Linus Refsnes"
my_function("Tobias")   # <-- will print "Tobias Refsnes"
```

## Parameters vs. Arguments
- The terms `parameter` and `argument` refer to the same thing: **data that is passed into a function**

For the sake of being precise; from a function's perspective:
  - An `parameter` is the **variable listed inside the parentheses** in the function header
  - An `argument` is the **value** that is **sent to the function** when it is **called**


## Number of Arguments
- By default, a **function** must be **called with** the **correct number of arguments**

  - So if your function **expects 2 arguments**, you have to **call the function with 2 arguments**, not more, not less.
  - If you **try** to call the function with **1 or 3 arguments**, you will get an **error**


## Default Arguments
- These arguments **fallback** to **default values** if **no explicit values are passed** to these arguments from the function call.
  - If a value for them is passed in the function call, they will use it.
    - If not, they will use their default value.

- Syntax for default arguments: `argumentName = defaultValue`

```python
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()            # <-- Uses default "Norway"
my_function("Brazil")
```

## Keyword Arguments
> Before we learn about keyword arguments, lets learn about **positional arguments**

- **Positional arguments** are values passed into a function **based on the order** in which the **parameters were listed** in the **function header**
  - Here, the **order is especially important** as values passed into these functions are **assigned to corresponding parameters based on their position**

```python
def my_function(name, age):
    print("My name is " + name + " and I am " + str(age) + " years old.")
    
my_function("James", 18)   # <-- correct order
#              |      |
#              |      |---> 18 assigned to `age`
#              |
#              |---> "James" assigned to `name`


my_function(18, "James")   # <-- wrong order
#            |     |
#            |     |---> "James" assigned to `age`
#            |
#            |---> 18 assigned to `name`

```

#### Keyword arguments use `keys` instead of `position`
```python
def my_function(name, age):
    print("My name is " + name + " and I am " + str(age) + " years old.")
    
my_function(name="James", age=18)  # positions of arguments don't matter

my_function(age=18, name="James")  # positions of arguments don't matter

```

Syntax: `argumentName = value`

Note: The syntax for **keyword arguments** and **default arguments** is pretty much the same.
  - The difference being that **default arguments** are **used** in the **function header**
  - Whereas **keyword arguments** are **used** in the **function call**
  - And they **serve totally different purposes**, even though they have the **same syntax**

## Returning data
- To return data from a function, use the `return` keyword

```python
def my_function(fname):
    full_name = fname + " Refsnes"
    return full_name

my_function("Emil")     # <-- will return "Emil Refsnes", but will do nothing with it.
```

```python
def my_function(fname):
    return fname + " Refsnes"   # <-- can also be written like this (no need to create a new variable)
```

- Return values can be assigned to variables, or printed.

```python
def my_function(fname):
    return fname + " Refsnes"

some_name = my_function("Emil")     # <-- will return "Emil Refsnes", and will assign it to some_name
```

```python
def my_function(fname):
    return fname + " Refsnes"

print(my_function("Emil"))     # <-- will return "Emil Refsnes", and will print it
```

```python
some_variable = input('enter something')  # the return value from `input()` is assigned to `some_variable`
```

## Arbitrary arguments: `*args` and `**kwargs`
- Suppose you have to following function that **takes two arguments** and **returns their sum**:

```python
def my_sum(a, b):
    return a + b
```

- This function works fine, but it’s **limited to only two arguments**.
  - What if you need to **sum a varying number of arguments**, where the number of arguments passed is only **determined at runtime**?

### The solution: `*args`
- When we want to **pass an arbitrary number of arguments** to a function, we use `*args`
- This way, we can pass 3, 4, 2, 6 or 10: **basically any number of arguments** to the same function.
>
- All the arguments passed will be saved in a variable called `args`
  - This variable is a list, where each item is an argument

```python
def my_sum(*args):
  total = 0
  
  for x in args:
      total = total + x
  
  return total

my_sum(1, 2)                         # \
my_sum(1, 55, 22)                    #  >-- all these will work
my_sum(34, 0, 323, 442, 844, 5454)   # /
```

## **kwargs
- The same concept as `*args`, but instead it works with **keyword arguments** (hence the name **kw**args)
  - ``kwargs`` will be an dictonary, with keys as the name of the arguments, and values as the values for the arguements
