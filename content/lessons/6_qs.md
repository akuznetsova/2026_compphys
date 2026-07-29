```{exercise} Check-in Question
:label: ex_6-1
:nonumber:
For a single iteration over one timestep, we can see from the Taylor's expansion that the higher order truncated terms are second-order. 

However, for all intent and purposes, when we iterate $N$ times, Euler's method is considered a first-order method. Why?
```

```{solution} ex_6-1
:label: sol_6-1
:class: dropdown
As we integrate forward in time, the total error is the sum of each iteration's error:

$$\sum_{k=0}^{N-1} \frac{1}{2} h^2 \frac{d^2 x}{dt^2} = \frac{1}{2} h \sum_{k=0}^{N-1} h \frac{df}{dt} $$

Since $N = t/\Delta t \propto 1/h$, 
the total integration to time $t$ is $\mathcal{O}(h)$:

$$\frac{1}{2} h \sum_{k=0}^{N-1} h \frac{df}{dt}\approx \frac{1}{2} h \int_{a}^{b} \frac{df}{dt} \, dt = \frac{1}{2} h [ f(x(b), b) - f(x(a), a) ]$$
```

```{exercise} Check-in Question
:label: ex_6-2
:nonumber:

If the error in one step of size $h$ is:
$$\epsilon = C h^5 $$

What is the [Richardson Extrapolation error](./4a_integrals.ipynb) between the result for 1 step size of $2h$, $x_1$ and two steps of size $h$, $x_2$ ?
```


```{solution} ex_6-2
:label: sol_6-2
:class: dropdown
With one steps of $2h$:
$$x_1 = x(t+2h) +  C (2h)^5 $$

With two steps of $h$:
$$x_2 = x(t+2h) + 2 C h^5 $$


thus: $ x_1 - x_2 = 30 C h^5 $

such that our error is bounded by:

$$ \epsilon = \frac{1}{30} (x_1 - x_2) $$

```



