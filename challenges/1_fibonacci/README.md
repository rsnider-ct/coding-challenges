# The Fibonacci Sequence

The [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) is a series of numbers that follow the governing rule:

```
A fibonacci number is a number in the Fibonacci sequence that is the sum of the previous two numbers in the sequence
```

For example, the first few numbers of the Fibonacci sequence are:

```
1 - 1 - 2 - 3 - 5 - 8 - 13
```

As you can see, each number is the sum of the previous two numbers. 

## The Prompt

Write a program that takes a number _n_ as an input from the user, and returns the _nth_ number of the Fibonacci sequence. For example, if I entered `5` into your program, I should get back `5`. If i input `51` into your fibonacci calculator, I should get `20365011074`. 

Ideally you should write this fibonacci calculator as a _function_.

This program should also be able to tell if an input is not a valid number (in our case, we only want integers), and will tell the user they gave us bad input. It _should not_ crash when given faulty input. 