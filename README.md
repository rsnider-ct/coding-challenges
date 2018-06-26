# Coding Challenges for Beginners!

This repository is a collection of problems of varying degrees of difficulty designed to help someone start out in their Software Engineering path. Each problem is designed to be self-contained, and will utilize various components and technologies as they progress.

## Cloning and Setting up the Repository

To Start, clone this repository to your local machine. This can be done as follows:

```bash
git clone https://github.com/rsnider-ct/coding-challenges.git
```

If you prefer to use SSH (a bit more complex to set up!) you can use the SSH version as well:

```bash
git clone git@github.com:rsnider-ct/coding-challenges.git
```

Once it is cloned to your local computer, we will need to create a new branch to serve as your `master` branch. simply run

```bash
git checkout -b <your name>-master && git push -u origin <your name>-master
```

This branch will serve as your primary, or `master` branch. We will use this branch as a base to compare and work against, in an effort to simulate what a software engineer would do in his day job. 

## Working with Challenges

Every problem has a README.md that I highly suggest you read before you work (it has the prompt in it, after all).

### Language Requirements

Personally, I believe any language would be more than enough for doing these challenges, so I will not enforce any one language to be used. That being said, I have some recommendations for your choice. If you are new to programming, I highly recommend using Python as your starting language (version 2.7 is preferable, but 3 would also be fine). Python offers a simple, yet powerful syntax that will help you spend more time learning the concepts of programming and less on syntatical "gotchas".  

## Setting up a problem for work

To submit code to the problemset, we will be using git's branching model. This will make it easy to track changes between problems, and can also be used to review code through GitHub's review system. Whenever you begin a coding challenge, create a new branch using the following command:

```bash
git checkout -b <your name>-<name of challenge>
```

For example, if you want to do challenge 1, named `fibonacci`, the command would look like this:

```bash
git checkout -b ryan-fibonacci
```

You are now free to work on the challenge and modify any files you see fit. When you are ready to submit code for any reason, be it completion or wanting a review, you can run the following workflow to submit.

## Submitting Challenges

At any point if you want to see what changes you have made, you can run 

```bash
git status
```

1) If there are any "Untracked Files" you would like to commit, run the following command listing all the new files:

```bash
git add <file1> <file2> <file3>...
```

This will take those files and tell git to start tracking their changes.

2) If there are files that are listed as "Changes to be committed" that you would like to add to this repository, you can run one of two commands:

```bash
git commit -a -m "your message in quotes"
```

This will simply add all of your changes to the commit, *BUT BE CAREFUL!* There are files you do NOT want committed to a repository, and without the proper configuration in place git will send those up too. Its a *much* smarter idea to simply list all the files you want committed manually like so:

```bash
git commit <file1> <file2> -m "your commit message in quotes"
```

Once those files are committed, they are ready for the push up to GitHub. Simply run

```bash
git push -u origin <branch-name>
```

and git will push all the staged files up to the remote (GitHub). From there, you can use the the GitHub UI to create a new Pull Request, which will show the differences in your code and allow for a smooth review before merging into your master branch.

One thing to note about the Pull Request UI: Suppose you wanted to merge the branch `ryan-fibonacci` into `ryan-master`. There are two branches you must specify as part of the PR: `base` and `compare`. `base` is the target branch you want to merge into. `compare` is the branch you want to merge. So, in our example, the `base` branch is `ryan-master`, and the `compare` branch is `ryan-fibonacci`.

## Other Notes

- Don't be afraid to ask questions! I'll do my best to reply as soon as possible with suggestions.
- Google is your best friend when faced with an impasse. Googling stack trace issues or other gotchas results in a fix probably 95% of the time. If you're faced with a problem someone has almost certainly faced it before you :). 
- Read and research as much as you can! This repository will by no means make you an "expert" programmer, practice makes you that. You can never spend too much time reading and learning about programming and the philosophy behind it. TBD I will start compiling a list of reading materials in this repository which can help guide you on your programming journey.
- Whatever you do, *DON'T GIVE UP!* Everyone has the ability to program, its not witchcraft. You're going to hit walls and impasses that might seem impossible at the time, but given enough time and thought you can solve any issue that may arise. *KNOW* that you can do it.