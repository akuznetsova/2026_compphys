```{exercise} Check-in Question
:label: ex_7-1
:nonumber:
How do you decide which ODE solver to use?
```

```{exercise} Check-in Question
:label: ex_7-2
:nonumber:
Let's say we start from a level surface, and after $t_1$ seconds the projectile lands back on the ground a distance $L$ away. What are our BC's for $x(t)$ and $y(t)$?
```

```{solution} ex_7-2
:label: sol_7-2
:nonumber:
:class: dropdown
Just checking if you're awake:
$$ x(0) = 0 \ x(t_1) = L \\
y(0) = 0 \ y(t_1) = 0 $$
```

```{exercise} Discussion Question
:label: ex_7-3
:nonumber:
For parametric $x$ and $y$, we could treat the solutions separately and iterate, performing the shooting method in $x$ and then in $y$. Or, we could perform the shooting for both $x$ and $y$ simultaneously. What are the advantages and disadvantages of both approaches here? Think about what the expensive steps here may be.
```