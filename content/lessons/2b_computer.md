# Talking to the Computer
> "Computers are incredibly fast, accurate and stupid. On the other hand, a well trained operator as compared with a computer is incredibly slow, inaccurate and brilliant."
-- [not Albert Einstein](https://www.techdirt.com/2021/09/29/misquoting-einstein-is-fast-stupid-not-accurate/)

You interact with your computer by providing an input which signals the computer to perform a set of tasks. Most of our day to day operations include pointing and clicking, which provides input through a graphical user interface (GUI). When we do this, we often don't know the extent of what's happening "under the hood" as the button doesn't show us every single task that is executed when we press it. 

When you write code, you have a more direct line to the computer. You're still not speaking it's native language, but the computer will translate the syntax of your programming language into it's own low-level directives -- also known as compiling -- that correspond to each operation. No more. No less.
**With programming, there is a direct relationship between what the code says and what the computer does.** 

While this is not a computer science or engineering class, by virtue or writing programs, you are writing instructions to your computer. We don't need to write in assembly language, but we still *do* need to understand what the computer can and can not do, in order to successfully talk to it. 

## The Command Line
We will be talking to our computer on the command line (also known as a terminal or shell). Shells have their own languages (bash, tsc, zsh, etc.) which talk to your computer. 
We will be doing a little bit of command line interfacing, for a more dedicated tutorial, check out this free resource by [Software Carpentry](https://swcarpentry.github.io/shell-novice/index.html).

```{note}
For this exercise, we are going to use a unix based shell. 
* If you have a unix-based operating system (Linux, Mac) on your laptop, all you will have to do is open up a terminal window.
* If you have a Windows machine, please make sure you have the Windows Subsystem for Linux installed and enabled on your machine. There is a walkthrough [here](https://learn.microsoft.com/en-us/windows/wsl/install) to get started.
* If you have a Windows machine and are running a Linux VM, I'd love to know who you are and what your deal is, but otherwise you'll want to be on Linux for this. 
```

## Getting to know the Computer
Your computer is a physical object, it's operations are bounded by it's hardware. 

The basic operations a computer performs are:
### Storing information (Memory)
All information on a computer is encoded into binary (0 or 1) - a signal or switch that is on or off. A single 0 or 1 is a *bit* and 8 bits make up a *byte*: the base unit of memory or storage. A byte can store $2^8$ or $256$ possible values which can be encoded to represent a number or a letter. Each file when opened on your computer is *physically* encoded by the number of "on" or " off" switches in memory that represent all the information in it and about it (the metadata). The CPU or processor is what does the shuffling around of information. Each processor is typically attached to some RAM (random access memory), which is where your computer keeps information while it's working on it. (This is much easier than trying to [read it off a hard disk each time](https://pages.cs.wisc.edu/~remzi/OSTEP/file-disks.pdf)). Each time you open a file, assign a variable, or make an array, your computer makes space for it in the RAM and assigns to an on or off switch. When your files are written to your file system, that is when it is written onto a hard disk by a literal actuator on an arm that magnetically signals to a specific position on the disk. 

Since we are human beings, and human beings think in hierarchies, we interface with information stored on our computer through a hierarchical **filesystem**
One of the most basic and fundamental things we can do on the command line is navigate our filesystem. 

```{exercise} Navigate your Filesystem
:label: ex_1
Open up your terminal. Get your bearings.
`ls -al` will *list all* the current files in whatever file directory you are in. 

What file directory are you in?
`pwd` gets the path of your *present working directory*. The path is basically like an address. 

Get to the top-most level directory in your path!
`cd [PATH]` will *change directory` to whatever path you write.

What are the directories within? Can you find your way back home and check out the scenery (contents of other folders) along the way?

If you get lost, `cd` will always take you home (literally to your home directory, also known as `~`)
```

You will have noticed some resemblance to the files and folders in your Explorer or Finder application -- because those applications are simply GUIs for navigating the filesystem. It can be a lot faster to zip through on the command line, especially if you know exactly where you need to go. 

```{exercise} Make some memories
:label: ex_2
Make sure you're back home. Let's keep things tidy and start off by making a directory. 

`mkdir [PATH]` will *make a directory* at the path you provide. You can use always use './' as a shorthand for where you currently are so you don't have to type the full path. This is called using a *relative path*. Or you can just type the name of file or directory you want and the shell will assume it will put it in your current location.

Check that it's there by asking it to list all the things inside!
Then, let's use your navigating skills to get inside the directory you created. 

There's nothing in there right now. Let's write a little message:
`echo 'hi there' > [PATH] ` will repeat the string you put in and *pipe* it into a file at the path you put. 

`cat [PATH]` will tell you the entire contents of the file at the path. 

How many bytes are in our file? Well, let's pull out `ls -al` again! The number to the left of the modified date, tells us our file size in bytes. 
```

So, why is 'hi there' 9 bytes? And how many times could you write 'hi there' in a single file before filling up a 200 GB hard drive?

```{note}
The now standardized manufacturer's definition states that 1GB=$10^9$ bytes, which has resulted in some [controversy](https://en.wikipedia.org/wiki/Gigabyte) along the way.
```


### Performing Operations (CPUs)
Your computer stores representations of information and it can perform logical operations with those numbers (addition, subtraction, multiplication, division etc.) If you know how a calculator works, you know how a computer works. 
How fast or powerful a computer is at doing operations is it's processing speed - this is how fast it can access information it's stored in memory, shuffle it around, and re-assign it to a new value (in practice, this can depend on both the amount of processors and the space it has in RAM)
Processing power is measured in units of [FLOPS](https://en.wikipedia.org/wiki/Floating_point_operations_per_second): *floating point operations per second*, literally how quickly it can add numbers. 

Each program a computer runs is essentially a list of operations on some information performed in some sequence. 

```{exercise} What is my computer up to right now?
:label: ex_3
Let's ask it! 

Run the command `top` in your terminal to get a list of what programs your computer is running. 

Note: `ctrl+c` will let you escape any running command to return to the command line.
```


## Setting Up your Environment
The absolute simplest interaction we can have with python is running python straight from our command line in the *python shell* (just type `python` in your terminal). The python shell is a program that interprets our python commands into the computer's native assembly on the fly, translating our commands into the access and shuffling around of bytes.

In navigating our filesystem, you might have noticed that we had to be specific about our path when using commands. Because information has a physical location, represented by it's path in our file system, the computer has to know how to find the information (the program it has to run, the data it has to manipulate, etc.). 

### The Shell Environment
There is a set of things the computer knows about by default. These describe the *environment*. The bash (or zsh on Mac) shell, like python, can store information assigned to variables. The default variables it stores are called environment variables. (They typically have a `$` in front.)

For example, when you run `python` from the command line, there isn't any file called python in the folder you are at. This is because there are a set of places your computer looks for programs to find them. The list of path locations it can look for a variable is stored in the `PATH` variable. 

You can ask your computer where it looks with `echo $PATH`.

For example, when you install a python distribution, it links the location of it's modules, packages, default settings, etc. and add them to your environment variable. So when you use a program like a ipython notebook, it uses that information to know where your numpy module is so you can call `import numpy` without having to be in a folder with `numpy.py` in it. 

You can see where your applications live according to your computer, for example: `which python` will tell you the path of the python distribution your computer is using right now. 

You can alter your environment in a file (typically your `.bashrc` or `.zshrc` for Mac) that your shell reads and executes whenever it starts up. 

For example, you can add to the list in your `PATH` or define nicknames for commands or paths. When you build programs from source (i.e. compile an executable rather than download an installer from the web) you will often have to manually append your `PATH` variable, as well as know the paths of any external libraries the program will need to access. 

```{exercise} Find you default configuration file
:label: ex_4

Your shell `*rc` file is located in your home directory. However, it has a `.` in front of it, meaning it is a hidden file. 
You can see all files when you use `ls - al` including hidden files. So go find it right now. 

You'll want to open it up. You can open and edit files with command line editors:
I will demonstrate using `vim [PATH]` , which have their own [commands](https://www.atmos.albany.edu/daes/atmclasses/atm350/vi_cheat_sheet.pdf). 

Let's practice altering our shell environments by setting up an `alias`, a shorthand nickname for commands you might execute often. Some [example aliases](https://www.thorsten-hans.com/5-types-of-zsh-aliases/). 

Save and quit. The first time you make changes, to put them into effect you'll need to 'source .bashrc` 
```

### The Python Environment
Just like the shell environment, you can also set up a python environment which specifically deals with which python distributions and packages you have accesst to. This is typically done within environment managers. 
For example, Anaconda is a commonly used python environment manager. If you type in `which python` you should see anaconda somewhere in the path, if anaconda is managing your python environment. 
Anaconda also lets you set up different environments and switch between them. This is especially handy if you have projects that use different versions of python or external libraries that only work because with specific library versions that may be different than the ones that you have by default. 

### The Integrated Development Environment (IDE)
When it comes to how you typically develop (write) and work with programs, most developers use an [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment). 

There are many types and styles of IDEs, some more complicated or more helpful than others, depending on what kind of code you are writing and your personal preferences.

Some example IDEs are:
+ Jupyter Lab/Notebook Servers
+ VSCode
+ Spyder
+ PyCharm 

I typically use VSCode, because I can edit notebooks and scripts, code in multiple languages, often make use of the integrated terminal panel, and edit code on other computers over a network (e.g. HPC, other workstations, etc.)

If you don't already have a preferred IDE, I recommend trying out one or two at least during this course.  










