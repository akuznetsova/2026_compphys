```{exercise} Check-in Question
:label: ex_5-1
:nonumber:
Using a given row, $k$, we want to eliminate the $kth$ term of all other rows using forward elimination. 
Let's try to come up with a *pseudo-code* for how to put what we just did algorithmically.
```

```{solution} ex_5-1
:label: sol_5-1
:class: dropdown
We will loop through every row but the last.   
    Within this loop, the current row is the kth row.
        For that row, we will loop through all subsequent rows $j = [k+1 \ldots N]$ and:
            + define a coefficient $$f_{j} = \frac{a_{j,k}}{a_{k,k}}$$
            + subtract $f_{j} \times \{ \mathrm{row}~k \}$ from the row $j$
            + subtract $f_{j} \times v_j$ from the corresponding row of $v_j$
```

```{exercise} Check-in Question
:label: ex_5-2
:nonumber:

Line by line, read through the code and come up with a comment for what each line is doing in the code.
```

```{exercise} Check-in Question
:label: ex_5-3
:nonumber:

Can you think of a way to find and address this problem in the code?
```

```{solution} ex_5-3
:label: sol_5-3
:class: dropdown

If the diagonal term of a row is zero, you can swap it with a different row. This is called **pivoting**.

In practice, since we are constantly transforming subsequent rows in the matrix, we should always be checking for the conditions to pivot before we use a row to transform any other row. 
```

```{exercise} Check-in Question
:label: ex_5-4
:nonumber:
In Newman 6.3.5, you can see that for Newton Raphson, where the next iteration is given by:
$$x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}$$

by Taylor expanding around the root $x^*$, for which $f(x^*) = 0$:
$$ f(x^*) = f(x) + (x^* - x_i) f'(x_i) + \frac{1}{2} (x^* - x_i)^2 f''(x_i) + ... $$

You can derive the error at iteration $i$, $ \epsilon_i = x^* - x_i$, will decrease quadratically at the next iteration:
$$\epsilon_{i+1} = -\frac{f''(x_i)}{2 f'(x_i)} \epsilon_i^2$$

Why is it that we can for most practical purposes estimate the error in terms of the difference between iterations?
$$\epsilon_i \approx x_{i+1} - x_i$$
```

