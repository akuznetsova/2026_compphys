```{exercise} Check-in Question
:label: ex_3-1
:nonumber:

Integers in Python start off as 64-bit. How many bytes would they take up?
```

````{solution} ex_3-1
:class: dropdown
:label: sol_3-1

$64/8 = 8$ bytes

````

```{exercise} Check-in Question
:label: ex_3-2
:nonumber:

The code above is also a demonstration of why you should never compare the equality of two floating point numbers as they would have to be within machine precision of one another to be treated as equal. 

What would be an alternative to the expression:
`a == b`?
```

````{solution} ex_3-2
:class: dropdown
:label: sol_3-2

For an absolute difference:
```{code-block} python
eps = 1e-5
abs(a-b) < eps
```

But this depends on the values of `a` and `b` 

A relative error is often more flexible:
```{code-block} python
eps = 1e-4
abs(a/b - 1.) < eps
```

would satisfy the condition for `a` and `b` within 0.01% of each other.
````

```{exercise} Check-in Question
:label: ex_3-3
:nonumber:
So, how can we get around this problem? Express $S(-24)$ in a more numerically tractable form, so we need to come up with an equivalent expression. 

*Hint*: play around with your function, for what useful values of $x$ is $S(x)$ reflective of our ground truth $e^x$?

```

````{solution} ex_3-3
:class: dropdown
:label: sol_3-3

$$e^(-24) = (e^-1)^{24}$$
Thus:
$$S(-24) = S(-1)^{24}$$
````

```{exercise} Try it out
:label: ex_3-4
:nonumber:

Play around with the code below to see how the error changes as you bring the numbers closer together. 
+ How close can $a$ and $b$ get before the relative error is on the order of $\sim 10\%$? 
+ How do you expect it to be related to the machine epsilon?
```