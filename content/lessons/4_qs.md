```{exercise} Check-in Question
:label: ex_4-1
:nonumber:

For a regularly spaced grid ($\Delta x$ is constant across the entire domain), the total integral for a left sum becomes:
$$I = \sum_{i=0}^{n-1} \Delta x f_i $$.

What is the corresponding expression for a right sum?
```

```{solution} ex_4-1
:label: sol_4-1
:class: dropdown

Notice that in the left sum, we stopped before $i=n$ for our sum, since the area of the rectangle between $x_{n-1}$ and $x_n$ has a height of $f_{n-1}$. 

Correspondingly, the first rectangle's height is $f_{1}$, which we could write either as:
$$I = \sum_{i=0}^{n-1} \Delta x f_{i+1} $$

or, equivalently:

$$I = \sum_{i=1}^{n} \Delta x f_{i} $$


```

```{exercise} Check-in Question
:label: ex_4-2
:nonumber:

How could you determine the maximum amount of $N$ appropriate for an integral?

Hint: Consider the plot of errors as a function of $h = \Delta x$ from last week.
```

```{exercise} Check-in Question
:label: ex_4-3
:nonumber:
Solve for the expression of the second derivative. What order scheme is this?
```

```{solution} ex_4-3
:label: sol_4-3
:class: dropdown

$$f^{\prime\prime}(x) = \frac{f(x+h) - 2 f(x) + f(x-h)}{h^2} + \mathcal{O}(h^2)$$

This scheme is second-order accurate.


```