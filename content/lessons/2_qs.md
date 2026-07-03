```{exercise} Check-in Question
:label: ex_2-1
:nonumber:

If I set up a plot with 2 rows of 3 columns, how do I get the axis of the 3rd column in the 2nd row?
You can always double-check by trying to plot on that axis!
```

```{exercise} Check-in Question
:label: ex_2-2
:nonumber:

How do you get the value of the "zeta" parameter for the 7th experiment from the `all_fits` dictionary? (You can check your guess with the value from the cell in the previous section.)
```

````{solution} ex_2-2
:label: sol_2-2
:class: dropdown

```{code-block} python
all_fits["zeta"][6]
```

````

```{exercise} Navigate your Filesystem
:label: ex_2-3
:nonumber:
Open up your terminal. Get your bearings.  
`ls -al` will *list all* the current files in whatever file directory you are in. 

What file directory are you in?  
`pwd` gets the path of your *present working directory*. The path is basically like an address. 

Get to the top-most level directory in your path!  
`cd [PATH]` will *change directory` to whatever path you write.

What are the directories within?   

Can you find your way back home and check out the scenery (contents of other folders) along the way?

If you get lost, `cd` will always take you home (literally to your home directory, also known as `~`)
```

```{exercise} Make some memories
:label: ex_2-4
:nonumber:

Make sure you're back home. Let's keep things tidy and start off by making a directory. 

`mkdir [PATH]` will *make a directory* at the path you provide. 

You can use always use './' as a shorthand for where you currently are so you don't have to type the full path. This is called using a *relative path*. Or you can just type the name of file or directory you want and the shell will assume it will put it in your current location.

Check that it's there by asking it to list all the things inside!

Then, let's use your navigating skills to get inside the directory you created. 

There's nothing in there right now. Let's write a little message:  
`echo 'hi there' > [PATH] ` will repeat the string you put in and *pipe* it into a file at the path you put. 

`cat [PATH]` will tell you the entire contents of the file at the path. 

How many bytes are in our file?   
Well, let's pull out `ls -al` again! The number to the left of the modified date, tells us our file size in bytes. 
```

```{solution} ex_2-4
:class: dropdown
:label: sol_2-4
So, why is 'hi there' 9 bytes?

And how many times could you write 'hi there' in a single file before filling up a 200 GB hard drive?
```

```{exercise} What is my computer up to right now?
:label: ex_2-5
:nonumber:

Let's ask it! 

Run the command `top` in your terminal to get a list of what programs your computer is running. 

**Note**: `ctrl+c` will let you escape any running command to return to the command line.
```

```{exercise} Find you default configuration file
:label: ex_2-6
:nonumber:

Your shell `*rc` file is located in your home directory. However, it has a `.` in front of it, meaning it is a hidden file. 

You can see all files when you use `ls - al` including hidden files. So go find it right now. 

You'll want to open it up. You can open and edit files with command line editors:  

I will demonstrate using `vim [PATH]` , which have their own [commands](https://www.atmos.albany.edu/daes/atmclasses/atm350/vi_cheat_sheet.pdf). 

Let's practice altering our shell environments by setting up an `alias`, a shorthand nickname for commands you might execute often. 
- Some [example aliases](https://www.thorsten-hans.com/5-types-of-zsh-aliases/). 

Save and quit. The first time you make changes, to put them into effect you'll need to 'source .bashrc` 
```