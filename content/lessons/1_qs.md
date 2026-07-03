```{exercise} Check-in Question
:label: ex_1-1
:enumerated: false
How many valid ways can you think of using the function above to calculate the natural log of 10?
```

````{solution} ex_1-1
:class: dropdown

```{code-block} python
log(10)
log(10,base=math.e)
log(10,math.e)
log(x=10)
log(x=10,base=math.e)
log(x=10,math.e)
```

````

```{exercise} Check-in Question
:label: ex_1-2
:enumerated: false
What is the assigned value of x?

`x = 1_000_000`

```

````{solution} ex_1-2
:class: dropdown

`1000000`

The underscore simply separates the digits. The underscore is an interesting convenience character. 
See https://www.datacamp.com/community/tutorials/role-underscore-python for many other uses of the underscore in Python.
````

```{exercise} Check-in Question
:label: ex_1-3
:enumerated: false
Suppose arrays `a` and `b` are defined as follows:

   `import numpy as np`
   
   `a = np.array([1,2,3,4])`
   
   `b = np.array([2,4,6,8])`

What will the computer print upon executing the following lines? (Try to work out the answer before trying it on the computer.)

`1) print(b//a+1)`

`2) print(b//(a+1))`

`3) print(1//a)`
```