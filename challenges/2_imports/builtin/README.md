# Importing Built-in functions

Welcome! Here we will be practicing a very simple operation -- importing builtin code. If you can run `python` in your terminal, you have these libraries already set up and ready to go. 

To start, let's put this readme on the side and open the file `random_number.py`. This is going to be a very simple project, I just want us to write a snippet of code that takes a random item from a list and prints it out. Simple, right? But how do we get a random number?

I'm not sure how cavalier you are, but I don't want to write an algorithm to generate a random number just to pick from 5 words in a list. Sounds like a bit of overkill. Thankfully, Python to the rescue! Python has a built-in library `random` which will suit our needs perfectly!

So, before we instantiate the list, lets add a new snippet:

```import random```

This will tell the Python interpreter that we want to use the `random` set of functions in our code. Python will then try to find `random` in its list of built-in functions. It's there! No surprises yet. But how do we use this?

Well, if you remember the Fibonacci challenge, to call a function we simply called the fibonacci function we wrote followed by a set of parentheses:

```fibonacci(x)```

Thanks to our import statement above, we can do the exact same thing to generate a random number. At a very high level, Python essentially just added all the random number functions, and assigned them a name, `random`. `random` is now a _group_ of functions.

So, how do we generate a random number between 1 and 5? Well, lets look at the [Python Docs](https://docs.python.org/2/library/random.html). Well, thats a lot to go through so I'll give you a little nudge in the right direction -- check out the Examples all the way at the bottom. One of the examples reads:

```>>> random.randint(1, 10)  # Integer from 1 to 10, endpoints included```

Wow! They've already written a function that generates a random number _between two endpoints_. That's the power of extensibility.

So, we know our endpoints here. 0 and 4. Now, if anyone is scratching their heads about that, a `list` is a collection of objects with an `index` assigned to each. Such as we count one, two, three, four, five objects there, a computer will count zero, one, two, three, four. _Computers are zero-based_, meaning they will count starting at zero.

So let's add that snippet to the example file. Below the list, add this statement

```python
random_index = random.randint(0,4)
```

This will give us a number between 0 and 4, perfect for retrieving a value from our array of 5 integers! Now, all we have to do is pass that random integer into the array accessor syntax and we'll get a random word.

To access an item in an array by its _index_, simply reference the array with a set of brackets after it. For example,

```python
random_word = list[random_index]
```

Sweet! All we have to do now is just print that variable, `random_word`. and boom! Try running this file a few times, and see what comes out!

Now that you have a basic understanding of how imports work, try removing the `import random` line, and see what happens. I don't want to spoil anything but it looks like Python can't find the function you want to use. Remember, if you ever need some basic functionality, there might already be a library out there to handle it! A quick Google search will give you all you need. 

## The Prompt

Great, you've made it this far! Now let's practice importing a few libraries and using them to make something cool. 

On every Unix system is a file, `/usr/share/dict/words`. This file contains all the words in the english dictionary. a quick word count of this directory shows there's about 235,886 words in this dictionary.

```bash
➜ cat /usr/share/dict/words | wc -l
  235886
```

For this challenge, I'd like you to make a file called `random_word_from_dict.py`, and use the random number library to pick a random word from this file. *Hint:* There's a python library out there for loading files into your code, some research will reveal the correct path there!

*BONUS POINTS:* If this wasn't hard enough, please update your script so I can supply a letter, and I'd like your random word generator to return a word that starts with said letter.