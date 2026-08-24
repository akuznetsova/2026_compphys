---
downloads:
  - file: 1a_exercises.ipynb
    title: Notebook
---
# Week 1: In-Class Exercises
Due: noon Friday Sept. 4th on HuskyCT  
Submit with filename: `w1_[LASTNAME].ipynb`


```{exercise} Prime Factors
:label: icc_1-1
:number: 1

Suppose we have an integer `n` and we want to know its prime factors. The prime factors can be calculated easily by dividing repeatedly by all integers from `2` up to `n` checking to see if the remainder is zero. 

Recall that the remainder after division can be calculated in Python using the modulo operation `%`, and that the integer division operation `//` ensures that the result returned is another integer (otherwise the standard division operator returns a float).

1. Write a function that takes the number `n` as argument and returns a list of its prime factors. Note that this list should contain repeated factors to reflect how many times they occur in the input number.

2. Validate your function by writing some code that tests if you can get back the input number `n` by multiplying all of its factors together.

3. Note that when you input a prime number, the only factor is itself. Write a script using your function to come up with a list of all the primes up to 10000.

```

```{code-cell} python
def factors(n):
    """
    Input: n, an integer
    Return: a list of factors of n
    """
    #### write your function here
    return

test_list = factors(17556)

# write your test here

primes = []

# write script to get primes
print(primes)
```

```{exercise} List Comprehending
:label: icc_1-2
:number: 2

Create the same list as the output of:


`list(map(lambda x: x**2, range(-3,4)))`


 above using a list comprehension
```

```{code-cell} python
# your_list = 
# print(your_list)
```

## Synthesis Question
*Discuss the following prompt in a new markdown cell below:*

Q: From this week's lesson: what is one concept you are comfortable/familiar with and one concept you maybe haven't encountered or applied before? 



