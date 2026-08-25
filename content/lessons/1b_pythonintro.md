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
```{image} https://github.com/user-attachments/assets/8224e916-8636-4b92-bac5-3c59bb87e76e
:alt: SciPy stack
:width: 600 px
:align: center
```

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
