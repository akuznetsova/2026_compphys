---
exports:
  - format: pdf
    template: lapreprint-typst
    id: notes-1b
downloads:
  - id: notes-1b
    title: PDF notes
  - file: 1b_pythonintro.ipynb
    title: Notebook
jupyter:
  kernelspec:
    display_name: base
    language: python
    name: python3
---

# Brief Tour of Python
This lesson has been adapted from J.R. Johansson's Scientific Python Lectures. 
The latest version of this [IPython notebook](http://ipython.org/notebook.html) lecture is available at [http://github.com/jrjohansson/scientific-python-lectures](http://github.com/jrjohansson/scientific-python-lectures).
The other notebooks in this lecture series are indexed at [http://jrjohansson.github.io](http://jrjohansson.github.io).

## How to use this notebook
+ This notebook may be run and viewed directly online to be used as a reference for the course.
+ In class, it is recommended that you follow along and execute the code as we discuss the corresponding material. You can download a copy of the notebook
to your computer and make modifications for a copy of your own interactive lecture notes. 
+ Sections marked "In-Class Coding Exercises" are part of the [weekly in-class assignment](../in-class/1a_exercises.ipynb) due at the end of the week as an `.ipynb` file on HuskyCT.

## Why Python?
+ Very high-level language:
  - Provides many complex data-structures and ways to manipulate them: an *object-oriented language*
  - Your code is shorter than a comparable algorithm in a compiled language
  - Faster to develop, less time to debug.
  - “Interpreted”, no need to compile, can run straight from your script.
  - Automatic memory management, no need to allocate memory
  - Dynamically typed, no need to define variable types.

```{warning}
You can not have it all! Python's performance can be significantly slower than more low-level compiled languages (C, C++, Fortran) because it is an interpreted language.
```

+ Easy to prototype new tools
+ Cross-platform 
+ Extensible: can call C, Fortran, etc functions from within Python, which can be useful to optimize performance.
+ Very widely adopted in Physics and beyond (so you can use code from collaborators!)
+ Excellent documentation and resources
+ Free and open source 

+ Many powerful libraries to perform complex tasks
  - Parse structured input files
  - Interact with the operating system
  - Perform scientific computations
  - Make plots

If you're interested in how the concepts we are going over today transfer to C, there is an excellent [set of notes from Richard Fitzpatrick](https://farside.ph.utexas.edu/teaching/329/lectures/node8.html)

### SciPy: The Scientific Library Stack
<img width="888" height="364" alt="image" src="https://github.com/user-attachments/assets/8224e916-8636-4b92-bac5-3c59bb87e76e" />


## Ways to run Python code
People can develop and run python code as scripts or program files (ending in ```.py```) or interactively with notebooks (```.ipynb```). There are advantages to either method, depending on context. In this course, we will practice both. 

In class, we'll be using interactive jupyter notebooks to get instant feedback. 
These are good for debugging in real time and are a popular development environment. 
For problem sets, you will be asked to turn in scripts. (You are more than welcome to develop within a notebook and save your final output into a script)


### 1. Python Program Files

* Python code is usually stored in text files with the file ending "`.py`":

        myprogram.py

* Every line in a Python program file is assumed to be a Python statement, or part thereof. 

    * The only exception is comment lines, which start with the character `#` (optionally preceded by an arbitrary number of white-space characters, i.e., tabs or spaces). Comment lines are usually ignored by the Python interpreter.


* To run our Python program from the command line we use:

        $ python myprogram.py

* On UNIX systems it is common to define the path to the interpreter on the first line of the program (note that this is a comment line as far as the Python interpreter is concerned):

        #!/usr/bin/env python

  If we do, and if we additionally set the file script to be executable, we can run the program like this:

        $ myprogram.py


### 2. Jupyter notebooks

This file - an interactive or Jupyter notebook -  does not follow the standard pattern with Python code in a text file. Instead, a notebook is stored as a file in the [JSON](http://en.wikipedia.org/wiki/JSON) format. The advantage is that we can mix formatted text, Python code and code output. It requires a notebook server to run it though, and therefore isn't a stand-alone Python program as described above. Other than that, there is no difference between the Python code that goes into a program file or a notebook code cell.

**The name of notebook files ends with the "`.ipynb`" file extension**

You can start interactive jupyter servers through a variety of methods:
+ On the command line by typing
    ``` jupyter notebook ```
    or 
    ``` jupyter lab ```
+ Through a development environment such as VSCode by starting a jupyter kernel.
+ Through a graphical user interface (GUI) like Anaconda
+ Running a notebook on a cloud (remote) server like binder or Google colab. 

Notebook cells are executed each time the cell is run and store any objects you assign into memory. By default, like any script, notebooks only output the last values returned in a cell. If you want to see the output of multiple calls in one cell or script, you can use the built-in `print()` function. 



## Modules and Libraries

Most of the functionality in Python is provided by *modules*. The Python Standard Library is a large collection of modules that provides *cross-platform* implementations of common facilities such as access to the operating system, file I/O, string management, network communication, and much more.

**References**
 * The Python Language Reference: https://docs.python.org/3/reference/index.html
 * The Python Standard Library: https://docs.python.org/3/library/index.html

To use a module in a Python program it first has to be imported. A module can be imported using the `import` statement. For example, to import the module `math`, which contains many standard mathematical functions, we can do:

```{code-cell} python
import math

x = math.cos(2 * math.pi)

print(x)
```

```{note}
Notice how we have to call the functions with the prefix of the module name
```

We can make this easier on ourselves by:

```{code-cell} python
import math as m

x = m.cos(2 * m.pi)

print(x)
```

Alternatively, we can chose to import all symbols (functions and variables) in a module to the current namespace (so that we don't need to use the prefix "`math.`" every time we use something from the `math` module. 

This can be very convenient if you don't forsee any other libraries with similar functionality.

```{code-cell} python
from math import *

x = cos(2 * pi)

print(x)
```

```{warning}
In large programs that include many modules, it is often a good idea to keep the symbols from each module in their own namespaces, by using the `import math` pattern. This would elminate potentially confusing problems with name space collisions in which multiple modules have the same name function at which point, the interpreter would not know which one to use!
```

As a third alternative, we can also choose to import only a few selected methods from a module by explicitly listing which ones we want to import instead of using the wildcard character `*`:

```{code-cell} python
from math import cos, pi

x = cos(2 * pi)

print(x)
```

### Looking up module information


Once a module is imported, we can list the symbols it provides using the `dir` function:

```{code-cell} python
import math

print(dir(math))
```

And using the function `help` we can get a description of each function (almost .. not all functions have docstrings, as they are technically called, but the vast majority of functions are documented this way). You can also get access to function information in the python documentation.

In general, most docstrings tell you two important things:
1. Inputs: what to put in the function, which are required or which are optional (also called keyword arguments)
2. Returns: what the function outputs. i.e. if you assigned the function to a variable, what that variable would store.

If we do `help(math.log)`, we can see that the required input ```x``` is the value you want the log of (it does not have to be called ```x```) and the optional input (you can tell because of the square brackets) is the base of the logarithm for which the default is a natural log.

```{code-cell} python
help(math.log)
```

```{code-cell} python
print(log(10))
print(log(10,2))
```


We can also use the `help` function directly on modules: 

Try
```
 help(math) 
```


## Variables and types


### Names
Variable names in Python can contain alphanumerical characters `a-z`, `A-Z`, `0-9` and some special characters such as `_`. Normal variable names must start with a letter. 

By convention, variable names start with a lower-case letter, and Class names start with a capital letter. 

In addition, there are a number of Python keywords that cannot be used as variable names. These keywords are:

    and, as, assert, break, class, continue, def, del, elif, else, except, 
    exec, finally, for, from, global, if, import, in, is, lambda, not, or,
    pass, print, raise, return, try, while, with, yield

```{warning}
Be aware of the keyword `lambda`, which could easily be a natural variable name in a scientific program. But being a keyword, it cannot be used as a variable name.
```


### Assignment
The assignment operator in Python is `=`. Python is a dynamically typed language, so unlike C or Fortran, we do not need to specify the type of a variable when we create one.
Assigning a value to a new variable creates the variable:

```{code-cell} python
x = 1.0
my_variable = 12.2
print(x, my_variable)
```

You can also do multiple assignments in one line.

```{code-cell} python
x,y,z = 1.0, 2.0, 3.0

a = b = c = 1
```

Although not explicitly specified, a variable does have a type associated (implicitly) with it. The type is derived from the value that was assigned to it.

```{code-cell} python
type(x)
```

If we assign a new value to a variable, its type can change.

```{code-cell} python
x = 1
type(x)
```

If we try to use a variable that has not yet been defined we get a `NameError`:

```{code-cell} python
print(yy)
```

### Fundamental types
+ Boolean: True or False
+ Integers
+ Floats
+ Complex

```{code-cell} python
# integers
x = 1
type(x)
```

```{code-cell} python
# float
x = 1.0
type(x)
```

```{code-cell} python
# boolean
b1 = True
b2 = False

type(b1)
```

```{code-cell} python
# complex numbers: note the use of `j` to specify the imaginary part
x = 1.0 - 1.0j
print(type(x))
print(x)
print(x.real, x.imag)
```

#### Type utility functions
You cna check if a variable is of a certain type:

```{code-cell} python
x = 1.0

# check if the variable x is a float
print(type(x) is float)
# check if the variable x is an int
print(type(x) is int)
```

#### Type casting
You can transform a variable's type into another by typecasting. 

```{code-cell} python
x = 1.5

print(x, type(x))

x = int(x)

print(x, type(x))
```

```{code-cell} python
z = complex(x)

print(z, type(z))
```

```{code-cell} python
x = float(z)
```


## Operators and comparisons
Most operators and comparisons in Python work as one would expect:

### Arithmetic operators:
 `+`, `-`, `*`, `/`, `//` (integer division), `**` (power)



```{code-cell} python
1 + 2, 1 - 2, 1 * 2, 1 / 2
```

```{code-cell} python
1.0 + 2.0, 1.0 - 2.0, 1.0 * 2.0, 1.0 / 2.0
```

```{code-cell} python
# Integer division of float numbers
3.0 // 2.0
```

```{code-cell} python
# Note! The power operators in python isn't ^, but **
2**3
```

```{note} 
The `/` operator always performs a floating point division in Python 3.x.
This is not true in Python 2.x, where the result of `/` is always an integer if the operands are integers.
to be more specific, `1/2 = 0.5` (`float`) in Python 3.x, and `1/2 = 0` (`int`) in Python 2.x (but `1.0/2 = 0.5` in Python 2.x).
``` 



```{code-cell} python
import numpy as np

a = np.array([1,2,3,4])
b = np.array([2,4,6,8])

print(b//a+1)
print(b//(a+1))
print(1//a)
```

### Boolean Operators 
The boolean operators are spelled out as the words `and`, `not`, `or`. 

```{code-cell} python
True and True
```

```{code-cell} python
True and False
```

```{code-cell} python
not False
```

```{code-cell} python
True or False
```

### Comparison (logical) operators 
`>`, `<`, `>=` (greater or equal), `<=` (less or equal), `==` (equality), `is` (identical), `!=` (not equal to)

The result of these expressions is always "True" or "False"



```{code-cell} python
2 > 1, 2 < 1
```

```{code-cell} python
2 > 2, 2 < 2
```

```{code-cell} python
2 >= 2, 2 <= 2
```

```{code-cell} python
# equality
[1,2] == [1,2]
```

```{code-cell} python
# objects identical?
l1 = l2 = [1,2]

l1 is l2
```

## Compound types: Strings, Lists and Dictionaries
These types include a sequence of values that are indexed: assigned to a location in the sequence by some key or value. 


### Strings
Strings are the variable type that is used for storing text. 

```{code-cell} python
s = "Hello world"
type(s)
```

```{code-cell} python
# length of the string: the number of characters
len(s)
```

```{code-cell} python
# replace a substring in a string with something else
s2 = s.replace("world", "test")
print(s2)
```

We can index a character in a string using `[]`:

```{code-cell} python
s[1]
```

```{warning}
Especially for Matlab users: indexing in Python starts at 0!
The first element of any sequence is accessed by the 0th index.
``` 
We can extract a part of a string using the syntax `[start:stop]`, which extracts characters between index `start` and `stop` -1 (the character at index `stop` is not included):

```{code-cell} python
print(s)
print(s[0:5])
print(s[4:5])
```

If we omit either (or both) of `start` or `stop` from `[start:stop]`, the default is the beginning and the end of the string, respectively:

```{code-cell} python
print(s[:5]) # all but last 5 
print(s[6:]) # first 6
print(s[:])  # entire string
```

We can also define the step size using the syntax `[start:end:step]` (the default value for `step` is 1, as we saw above):

```{code-cell} python
print(s[::1]) # every character
print(s[::2]) # every other character
```

#### String formatting examples
Many ways to put print statements together for more informative messages. 

Formatting output values into strings allows you to decide the output precision.

You can read more about specific formatting use cases and examples here: https://pyformat.info/

```{code-cell} python
 # The comma-separated print statement concatenates strings with a space
print("str1", "str2", "str3") 
```

```{code-cell} python
# The print statement converts all arguments to strings
print("str1", 1.0, False, -1j)  
```

```{code-cell} python
# strings added with + are concatenated without space
print("str1" + "str2" + "str3") 
```

```{code-cell} python
# we can use C-style string formatting to input values into a string
print("value = %f meters" % 1.0)       
```

```{code-cell} python
# this formatting creates a string with a 2 digit float and a single digit decimal
s2 = "value1 = %.2f and value2 = %d" % (3.1415, 1.5)

print(s2)
```

```{code-cell} python
# alternative ("new"), more intuitive way of formatting a string 
s3 = 'value1 = {0}, value2 = {1}'.format(3.1415, 1.5)

# The brackets and characters within them (called format fields) are replaced 
# with the objects passed into the str.format() method.
print(s3)
```

```{code-cell} python
# and you can also specify the format as before
# this time a two digit float and 6 digit float
s4 = 'value1 = {0:.2f}, value2 = {1:.6f}'.format(3.1415, 1.5)
print(s4)
```

```{code-cell} python
# have a look at the many options to work with strings
dir(s)
```

### Lists
Lists are very similar to strings, except that each element can be of any type.

The syntax for creating lists in Python is `[...]`:

```{code-cell} python
l = [1, 'a', 1.0, 1-1j]

print(l)
print(type(l))

l = [1,2,3,4]

print(l)
print(type(l))
```

```{tip}
Notice how `type()` returns the type of the highest level object, not the types within!
```


We can use the same slicing techniques to manipulate lists as we could use on strings:

```{code-cell} python
print(l)
print(l[1:3])
print(l[::2])
```

```{warning} 
Reminder: Indexing starts at 0!
```

```{code-cell} python
print('The first element is: ' , l[0])
print('The last element is: {}'.format(l[-1]))
print('The fourth element is %i' % l[3])
print('A list of just the last two elements:', l[-2:])

```

Since lists are also a type, python lists can be inhomogeneous and arbitrarily nested:


```{code-cell} python
nested_list = [1, [2, [3, [4, [5]]]]]

nested_list
```

Lists play a very important role in Python. For example they are used in loops and other flow control structures (discussed below).   
There are a number of convenient functions for generating lists of various types, for example the `range` function.  

In Python 3, `range` generates an iterator, which can be converted to a list using `list(...)`.  
(It has no effect in python 2)

```{code-cell} python
start = 10
stop = 30
step = 2

print(range(start, stop, step))

print(list(range(start, stop, step)))
print(list(range(-10, 10)))

```

Create a list of the individual characters in a string by type-casting.

```{code-cell} python
s = 'Hello world'
s2 = list(s)

print(s2)
```

Lists may also be sorted (in this case, alphabetically)

```{code-cell} python
s2.sort()

print(s2)
```

#### List operations
Adding, inserting, modifying, and removing elements from lists

```{code-cell} python
# create a new empty list
l = []

# add an element using `append`
l.append("A")
l.append("d")
l.append("d")

print(l)
```

We can modify lists by assigning new values to elements in the list. In technical jargon, lists are *mutable*.

```{code-cell} python
l[1] = "p"
l[2] = "p"

print(l)

l[1:3] = ["d", "d"]

print(l)
```

Insert an element at an specific index using `insert`

```{code-cell} python
l.insert(0, "i")
l.insert(1, "n")
l.insert(2, "s")
l.insert(3, "e")
l.insert(4, "r")
l.insert(5, "t")

print(l)
```

Remove first element with specific value using 'remove'

```{code-cell} python
l.remove("A")

print(l)
```

Remove an element at a specific location using `del`:

```{code-cell} python
del l[7]
del l[6]

print(l)
```

```{warning}
Mutable structures can also be dangerous if you are not careful about assignments. Typically, we can copy values of a variable into a different variable and operations on the copy will not affect the original, EXCEPT if you have a mutable structure (list, dictionary, etc.)
```

```{code-cell} python
a = 1
b = a
b += 1 #adding 1 to the previous value of b
print("a =",a)
print("b =",b)
```

```{code-cell} python
l1 = [1,2,3,4]
l2 = l1
print(l1,l2)

l2[0] += 1
print("l1 =", l1)
print("l2 =", l2)
```

See `help(list)` for more details, or read the online documentation 


### Arrays 
With the numpy library, you can access operations for data structures called *arrays*.

Numpy has a large library of functions with custom operations on arrays.

```{code-cell} python
import numpy as np
```

You can convert between lists and arrays fairly simply:

```{code-cell} python
l1 = [1,2,3,4]
a1 = np.array(l1)
```

In general lists and arrays can look similarly. They are both indexed and sliced, but they do behave differently in some key ways:
Notably:
+ Arrays can be multiple dimensions, like matrices.
+ Arrays behave like vectors during multiplication, operations are elementwise, unlike lists.
+ Array operations are typically much faster than lists due to native vectorization in numpy.

```{code-cell} python
print(2*l1)
print(2*a1)
```

```{code-cell} python
print(l1 + [4])
print(a1 + 4)
```

### Tuples
Tuples are like lists, except that they cannot be modified once created, that is they are *immutable*. 

In Python, tuples are created using the syntax `(..., ..., ...)`, or even `..., ...`:

```{code-cell} python
point = (10, 20)

print(point, type(point))

point = 10, 20

print(point, type(point))
```

We can "unpack" a tuple by assigning it to a comma-separated list of variables. (This is nice to keep in mind as many library functions also return tuples)

```{code-cell} python
x, y = point

print("x =", x)
print("y =", y)
```

We can ignore a given value if not needed

```{code-cell} python
mytuple = (1,2,3)
x, _, y = mytuple
print("x =", x)
print("y =", y)
```

or a few

```{code-cell} python
mytuple = (1,2,3,4,5)
x, *_, y = mytuple
print("x =", x)
print("y =", y)
```

Because tuples are **immutable**, if we try to assign a new value to an element in a tuple we get an error:

```{code-cell} python
point[0] = 20
```

### Dictionaries
Dictionaries are also like lists, except that each element is a key-value pair and are defined with curly brackets. The standard syntax for dictionaries is `{key1 : value1, ...}`

```{note}
The (optional) trailing comma below doesn't really do anything
```

```{code-cell} python
params = {"parameter1" : 1.0,
          "parameter2" : 2.0,
          "parameter3" : 3.0,}

print(type(params))
print(params)
```

You can access a given value by indexing by it's original key:

```{code-cell} python
print( params["parameter1"] )
print("parameter2 = " + str(params["parameter2"]))
print("parameter3 = " + str(params["parameter3"]))
```

And reassign values or add new entries by key:

```{code-cell} python
params["parameter1"] = "A"
params["parameter2"] = "B"

# add a new entry
params["parameter4"] = "D"

print("parameter1 = " + str(params["parameter1"]))
print("parameter2 = " + str(params["parameter2"]))
print("parameter3 = " + str(params["parameter3"]))
print("parameter4 = " + str(params["parameter4"]))
```

## Control Flow
In Python, control blocks are created by a statement ending with a colon and followed by indented text. 
Indents are a vital part of how python parses control statements, so extra or not enough indents will change how python parses the code.

### Conditional statements: if, elif, else
The Python syntax for conditional execution of code uses the keywords `if`, `elif` (else if), `else`

```{code-cell} python
statement1 = False
statement2 = False

if statement1:
    print("statement1 is True")
    
elif statement2:
    print("statement2 is True")
    
else:
    print("statement1 and statement2 are False")
```

```{note}

Compare to the equivalent C code:
````{code-block} C
    if (statement1)
    {
        printf("statement1 is True\n");
    }
    else if (statement2)
    {
        printf("statement2 is True\n");
    }
    else
    {
        printf("statement1 and statement2 are False\n");
    }
````
In C, blocks are defined by the enclosing curly brakets `{` and `}`. And the level of indentation (white space before the code statements) does not matter (completely optional). 

But in Python, the extent of a code block is defined by the indentation level (usually a tab or say four white spaces). This means that we have to be careful to indent our code correctly, or else we will get syntax errors. 
```



#### If statement examples:

```{code-cell} python
statement1 = statement2 = True

if statement1:
    if statement2:
        print("both statement1 and statement2 are True")
```

```{code-cell} python
# Bad indentation!
if statement1:
    if statement2:
    print("both statement1 and statement2 are True")  # this line is not properly indented
```

```{code-cell} python
statement1 = False 

if statement1:
    print("printed if statement1 is True")
    
    print("still inside the if block")
```

```{code-cell} python
if statement1:
    print("printed if statement1 is True")
    
print("now outside the if block")
```

```{code-cell} python
a = 2.
b = 3.
if a > 0:
    result = b/a
    print('result =',result)
else:
    print('WARNING: a = ' + str(a))
```

### Loops

In Python, loops can be programmed in a number of different ways. The most common is the `for` loop, which is used together with iterable objects, such as lists.



#### `for` loops

```{code-cell} python
for x in [1,2,3]:
    print(x)
```

The `for` loop iterates over the elements of the supplied list, and executes the containing block once for each element. Any kind of list can be used in the `for` loop.

 For example, using `range`:

```{note}
`range(4)` does not include 4 ! range is not inclusive of the stop point.
```


```{code-cell} python
for x in range(4): # by default range start at 0
    print(x)

for x in range(-3,3):
    print(x)
```

Notably, you can iterate over the indices of a list by making a range that matches the length of the list or just iterate over the values of the list:

```{code-cell} python
word_list = ["scientific", "computing", "with", "python"]

for i in range(len(word_list)):
    print(word_list[i])

for word in word_list:
    print(word)
```

Or keep track of both automatically using `enumerate`:

```{code-cell} python
for i, word in enumerate(word_list):
    print(i, word)

for idx, x in enumerate(range(-3,3)):
 print(idx, x)
```

You can look at dictionary contents in a few different ways, including looping over the items.

```{code-cell} python
print('Entire dictionary', params)
print('Tuples of paired keys and values:', params.items())
print('Iterating over keys and values:')
for key, value in params.items():
    print(key + " = " + str(value))
print('Iterating over keys')
for this_key in params.keys():
    print(this_key, params[this_key])
```

#### List comprehension
Creating lists using one line `for` loops. 
List comprehension is a convenient and compact way to create lists from iterative operations.

```{code-cell} python
print("Squares of all numbers between 0 and 4")
l1 = [x**2 for x in range(0,5)] 
print(l1)

print("Squares of all even numbers between 0 and 4")
l2 = [x**2 for x in range(0,5) if x%2==0]
print(l2)
```

#### `while` loops
`while` loops will iterate as long as the condition is true.

Here, we iterate for as long as i is less than 5. In this case, each loop increases the value of i by 1. 

```{code-cell} python
i = 0

while i < 5:
    print(i)
    
    i = i + 1
    
print("done")
```

```{note}
The  `print("done")` statement is not part of the `while` loop body because of the difference in indentation, so it can tell you that you've exited the loop. 
```


```{warning}
If your iterator never reaches the condition, the program will loop infinitely. For example (don't run this block):

````{code-block} python
i = 0
while i < 5:
    print(i)
    
    i = i - 1
    
print("done")
````

```


You can control loop iterations or exits with `pass` or `break`, which you can invoke with conditions.


For example, let's say I have a mixed type list and want to perform operations on only the numbers.


```{code-cell} python
mylist = ["jenny", 8, "i",6, "got", 7, 5, "your",3,  0, "number", 9]
jennys_number = []

for val in mylist:
    if type(val) is not str:
        jennys_number.append(val)
    else:
        pass 

print(jennys_number)
```

Now let's say I know that beyond a certain value, there are no numbers I want (so I want to stop my loop!)

```{code-cell} python
mylist = ["jenny", 8, "i",6, "got", 7, 5, "your",3,  0, "number", 9, "JENNY!", "DO", "NOT", 'change',"your", 867,5309,'number!']
jennys_number = []

for val in mylist:
    if type(val) is not str:
        jennys_number.append(val)
    else:
        pass 
    if val == "JENNY!":
        break

print(jennys_number)
```

## Functions

A function in Python is defined using the keyword `def`, followed by a function name, a signature within parentheses `()`, and a colon `:`. The following code, with one additional level of indentation, is the function body. Like in a control block, indendation determines when your function ends. 

Functions must be defined before they are used and do not run until they are called. 

```{code-cell} python
def func0():   
    print("test")
```

```{code-cell} python
func0()
```

Optional, but highly recommended, we can define a so called "docstring", which is a description of the functions purpose and behaivor. The docstring should follow directly after the function definition, before the code in the function body surrounded by triple quotes.

Doc strings are what python returns for functions when `help` is called. 

```{code-cell} python
def func1(s):
    """
    Input: 's', a string
    Print 's' and tell us how many characters it has    
    """
    
    print(s + " has " + str(len(s)) + " characters")

help(func1)

func1("test")
```

Functions that return a value use the `return` keyword, which can be assigned to a variable like any other values.

```{code-cell} python
def square(x):
    """
    Return the square of x.
    """
    return x ** 2

y = square(4)
print(y)
```

We can return multiple values from a function using tuples (see above):

```{code-cell} python
def powers(x):
    """
    Return the square, cube, and fourth power of x.
    """
    return x ** 2, x ** 3, x ** 4
```

```{code-cell} python
powers(3)
```

```{code-cell} python
x2, x3, x4 = powers(3)

print(x3)
```

<h2><span class="fa fa-flash"></span> In-Class Coding Exercise</h2>

```{embed} #icc_1-1
```


### Function arguments: args and kwargs
In a definition of a function, we can require inputs (args: arguments) or specify default values (optional kwargs: optional keyword arguments).

```{code-cell} python
def myfunc(x, p=2, debug=False):
    if debug:
        print("evaluating myfunc for x = " + str(x) + " using exponent p = " + str(p))
    return x**p
```

Here both `p` and `debug` are kwargs. 

For example, if we don't provide a value of the keyword arguments when calling the the function `myfunc` it defaults to the value provided in the function definition.

```{code-cell} python
myfunc(5)
```

```{code-cell} python
myfunc(5, debug=True)
```

If we explicitly list the name of the arguments in the function call, including the required arguments, the arguments do not need to come in the same order as in the function definition, but we always have to provide at least the required "positional" argument.

```{code-cell} python
myfunc(p=3, debug=True, x=7)

myfunc()
```

Sometimes you might wish to write a function in which you don't initially know how many arguments the user will pass. In this case, you can use the special form `*args` and `**kwargs` to catch all arguments that are passed. Here is an example:

```{code-cell} python
def catch_all(*args, **kwargs):
    print("args =", args)
    print("kwargs = ", kwargs)

catch_all(1, 2, 3, a=4, b=5)
```

Here it is not the names args and kwargs that are important, but the * characters preceding them. args and kwargs are just the variable names often used by convention, short for "arguments" and "keyword arguments". The operative difference is the asterisk characters: 
+ a single `*` before a variable means "expand this sequence"
+ a double `**` before a variable means "expand this dictionary"

In fact, this syntax can be used not only with the function definition, but with the function call as well!

```{code-cell} python
inputs = (1, 2, 3)
keywords = {'pi': 3.14}

catch_all(*inputs, **keywords)
```

You can use kwargs to control how your function behaves overall, depending on what inputs are used. This is typically referred to as using a "flag". In the example below, the "add" keyword is a "flag" that controls the output of the function, adding the value of the "add" keyword to the computation.

```{code-cell} python
def f3(x, p=2, **kwargs):
    print(kwargs.keys(), kwargs.values())
    if 'add' in kwargs.keys():
        return x**p + kwargs['add']
    else:
        return x**p
    
print(f3(2))
print(f3(2,add=6))
print(f3(2,add=6,ktest='somethingelse'))
```

### `lambda` function: the unnamed function

In Python we can also create unnamed functions, using the `lambda` keyword. 
These are used as one line (often temporary) functions

```{code-cell} python
f1 = lambda x: x**2
    
# is equivalent to 

def f2(x):
    return x**2

f1(2), f2(2)
```

Like a normal function defined with def, lambda functions support all the different ways of passing arguments.

```{code-cell} python
f1 = lambda x, p=2: x**p
    
# is equivalent to 

def f2(x, p=2):
    return x**p


f1(2,p=3), f2(2,p=3)
```

This technique is useful for example when we want to pass a simple function as an argument to another function, like in the `map` function, a built-in python function which "maps" a set of iterator values into a function that takes a single input.

```{code-cell} python
for i in map(lambda x: x**2, range(-3,4)):
    print(i)

# in python 3 we can use `list(...)` to convert the iterator to an explicit list
list(map(lambda x: x**2, range(-3,4)))
```

<h2><span class="fa fa-flash"></span> In-Class Coding Exercise</h2>

```{embed} #icc_1-2
```


## Classes

Classes are the key features of object-oriented programming (OOP). You may notice that everything we've discussed (variables, lists, dictionaries, tuples, etc.) are all types of objects that behave according to their own set of rules and have operations that can be used on them. 


A class is a structure for representing a custom object alongside the operations that can be performed on the object. 

In Python, a class can contain *attributes* (variables) and *methods* (functions).

A class is defined almost like a function, but using the `class` keyword, and the class definition usually contains a number of class method definitions (a function in a class).

There are a few rules for classes:

* Each class method should have an argument `self` as its first argument. Within the class, you can use `self` to reference the object. 

* Some class method names have special meaning, for example:

    * `__init__`: The name of the method that is invoked when the object is first created (usually by being called).
    * `__str__` : A method that is invoked when a simple string representation of the class is needed, as for example when printed.
    * There are many more, see http://docs.python.org/2/reference/datamodel.html#special-method-names


```{code-cell} python
class Point:
    """
    Simple class for representing a point in a Cartesian coordinate system.
    input: x , y coordinates for the point.
    """
    
    def __init__(self, x, y):
        """
        Create a new Point at x, y.
        """
        self.x = x #assigns the x attribute
        self.y = y #assigns the y attribute
        
    def translate(self, dx, dy):
        """
        Translate the point by dx and dy in the x and y direction.
        """
        self.x += dx #re-assigns the x attribute
        self.y += dy #re-assigns the y attribute
        
    def __str__(self):
        return("Point at [%f, %f]" % (self.x, self.y))
```

To create a new instance of a class (or initialize a new class object), you call the class by it's name and use the arguments in the `__init__` command:

```{code-cell} python
p1 = Point(0, 0) # this will invoke the __init__ method in the Point class

print(p1)         # this will invoke the __str__ method

# access the data stored in p1 by asking for the attributes:
print('x = ' + str(p1.x))
print('y = ' + str(p1.y))
```

To invoke a class method of the class instance `Point`:

```{code-cell} python
p2 = Point(1, 1)

p1.translate(0.25, 1.5)

print(p1)
print(p2)
```

```{note}
Calling class methods can modify the state of that particular class instance, but does not affect other class instances or any global variables.


That is one of the nice things about object-oriented design: code such as functions and related variables are grouped as separate and independent entities. 
What happens within a function or class operates in the ** local scope ** and is removed from memory unless assigned to an attribute or returned.
```


```{code-cell} python
help(Point)

```

## Modules

One of the tenets of good programming is to figure out how to reuse code and avoid repetition.

The idea is to write functions and classes with a well-defined purpose and scope, and reuse these instead of repeating similar code in different parts of a program. This is called modular programming. The result is usually that readability and maintainability of a program is greatly improved. What this means in practice is that our programs have fewer bugs, are easier to extend and debug/troubleshoot. 

Python supports modular programming at different levels:
+ Functions and classes are examples of tools for low-level modular programming that occurs within a single program.
+ Python modules are a higher-level modular programming construct, where we can collect related variables, functions and classes in a python script and is made accessible to other programs using an `import` statement.  

Consider the following example: the file `mymodule.py` contains simple example implementations of a variable, function and a class.

```{tip}
Note below we use the `%%writefile` command: this is not Python but rather an IPython "magic" command which will save the content of the cell into a file named by its parameter (`mymodule.py`)

You can also load the contents of any python script into a notebook cell directly using the magic `%load` command, but this behaves differently from the module architecture which we are exploring here.
```

```{code-cell} python
%%writefile mymodule.py
"""
Example of a python module. Contains a variable called my_variable,
a function called my_function, and a class called MyClass.
"""

my_variable = 0

def my_function():
    """
    Example function
    """
    return my_variable
    
class MyClass:
    """
    Example class.
    """

    def __init__(self):
        self.variable = my_variable
        
    def set_variable(self, new_value):
        """
        Set self.variable to a new value
        """
        self.variable = new_value
        
    def get_variable(self):
        return self.variable
```

We can import the module `mymodule` into our Python program using `import`. By default, Python will look for the module in the current directory of your file and then in the PYTHONPATH. 

(It is typically good practice to put all the imports at the top of your code.)


```{code-cell} python
import mymodule

print(mymodule.my_variable)
mymodule.my_function()

my_class = mymodule.MyClass() 
my_class.set_variable(10)

my_class.get_variable()
```

```{warning}
If we make changes to the code in `mymodule.py`, we need to reload it. Usually through restarting your kernel or with custom reload.
```

```{code-cell} python
#reload(mymodule)  works only in python 2

import imp   # in python3
imp.reload(mymodule)
```

```{code-cell} python
help(mymodule)
```

## Errors and Exceptions
In Python errors are managed with a special language construct called "Exceptions". When errors occur exceptions can be raised, which interrupts the normal program flow. 


### Runtime Errors

If you've done any coding in Python, you've likely come across some common runtime errors:
+ NameError
+ TypeError
+ ZeroDivisionError
+ IndexError


```{code-cell} python
# if you try to reference an undefined variable
print(Q)
```

```{code-cell} python
# if you try an operation that's not defined:
1 + 'abc'
```

```{code-cell} python
# trying to compute a mathematically ill-defined result:
2 / 0
```

```{code-cell} python
# trying to access a sequence element that doesn't exist:
L = [1, 2, 3]
L[1000]
```

### Raising your own Errors
You can generate your own exception using the `raise` statement which takes an argument that must be an instance of the class `BaseException` or a class derived from it (https://docs.python.org/3/library/exceptions.html). 

```{code-cell} python
raise Exception("description of the error")
```

```{code-cell} python
raise ValueError("parameter must be non-zero")
```

A typical use of exceptions is to abort functions when some error condition occurs, for example:
```
    def my_function(arguments):
    
        if not verify(arguments):
            raise Exception("Invalid arguments")
        
        # rest of the code goes here
```


To gracefully catch errors that are generated by functions and class methods, or by the Python interpreter itself, use the `try` and  `except` statements:
```
    try:
        # normal code goes here
    except:
        # code for error handling goes here
        # this code is not executed unless the code
        # above generated an error
```
For example:

```{code-cell} python
try:
    print("test")
    # generate an error: the variable test is not defined here
    print(test)
except:
    print("Caught an exception")
```

To get information about the error, we can access the `Exception` class instance that describes the exception by using for example:
`except Exception as e:`

```{code-cell} python
try:
    print("test")
    # generate an error: the variable test is not defined
    print(test)
except Exception as e:
    print("Caught an exception: " + str(e))
```

Let's say we're trying to create a perfect division function that can deal with anything! We want a function that won't give us an undefined value when we divide by 0, which would ordinarily spawn a `ZeroDivisionError`

```{code-cell} python
def safe_divide(a, b):
    try:
        return a / b
    except:
        return 1E100
    
print(safe_divide(2,0))
```

There is a subtle problem with this code, though: what happens when another type of exception comes up?

 For example, this is probably not the behavior we intended:

```{code-cell} python
safe_divide (1, '2')
```

Dividing an integer and a string raises a TypeError, which our over-zealous code caught and assumed was a ZeroDivisionError! For this reason, it's nearly always a better idea to catch exceptions explicitly. We're now catching zero-division errors only, and letting all other errors pass through un-modified.

```{code-cell} python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 1E100
    
safe_divide(2, 0)
safe_divide (1, '2')
```

## Further reading


* http://www.python.org - The official web page of the Python programming language.
* http://www.python.org/dev/peps/pep-0008 - Style guide for Python programming. Highly recommended. 
* http://www.greenteapress.com/thinkpython/ - A free book on Python programming.
