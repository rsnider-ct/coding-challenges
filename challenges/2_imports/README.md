# Imports


### Introduction
Now that we got an intro to code itself, lets try something else. One of the most powerful features of code is its reusability. A lot of code is simply building blocks that we assemble into some process (or _algorithm_). 

For example, in the last challenge, we created a fibonacci calculator. That was as simple as breaking the project up into its required parts:

1. Figuring out how to calculate a fibonacci number based on its index
2. Wrapping that in a function that accepts an integer as an argument
3. Accepting an input from a user that would then be passed to the function (and sanity-checked that the user actually supplied an integer.)

and then compiling the parts into one complete script. We noticed something interesting there, however. There's a function already built called `input()`! That's handy, all we had to do was give it a string and assign it a variable and we could get all the lovely input from the user we wanted. 

### Work Smart not Hard
Engineers (and especially Software Engineers) benefit greatly from this thinking. Why write something twice? If we can abstract a process enough where it applies across a broad range of applications, we save ourselves both time and effort. 

This is something that makes programming languages so neat. They're _extensible_. Languages ship out of the box with a ton of great features, like our friend the `input()` function. This function is only the tip of the iceberg of a swath of helper functions designed to make your code cleaner and easier to work with. 

Moreover, if a language doesn't come shipped with some functionality, they offer tools to help you build and distribute custom code. In Python, this is called `pip`, and it'll be your best friend in building software using other people's libraries.

This unit covers importing code, both builtin and remote code, and shows you how to utilize the libraries effectively. Please go through each subdirectory of this prompt and follow along with the examples I've created. Let me know if you have any questions!