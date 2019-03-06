# Coding Challenges Cheatsheet

This file is intended to be a quick-reference for certain commands and processes related to this repository. This is not a full-featured info section on Bash, Python, or Git, if something isn't covered here please check out their documentation!

### Basic Shell (Bash) commands

#### Change Directory
```bash
cd path/to/directory
```
The `cd` command will change your current working directory (defined by the variable $PWD) to some other directory. The example above uses a relative path, when an absolute path is set from the root of the Hard Drive.

Remember too that `~` is a special character and represents your home directory! if your project is in the directory /Users/r/projects/coding-challenges, its functionally identical to saying `cd ~/projects/coding-challenges`.

#### Print something to the command line
```bash
echo $PWD
```
`echo` is a helpful command as it prints something to the command line. the variable `$PWD` above represents your current working directory, represented by an absolute path. so, if you're in your home directory, the value of `$PWD` would be `/Home/your-name`.

#### Get your current working directory
```bash
pwd
```
The `pwd` command does the same thing outlined in the blurb above, it simply prints your current working directory to the command line. Helpful to figure out where you are on a system

#### Print the contents of a file to the command line
```bash
cat file.py
```

The `cat` command prints the contents of a file to the commmand line. easily coupled with `grep` to find certain things in a file!

Example:
```bash
cat file.py | grep library-name
```
This example will find all instances of `library-name` in that file and print them to the command line.

#### Remove a file
```bash
rm path/to/file.py
```
This command will effectively delete a file from disk. Be careful! It gets deleted for good, does not send the file to the recycle bin. 

If a file is being fussy (or you want to delete an entire directory), add the -rf flag to the command.

```bash
rm -rf path/to/directory
```

#### Make a directory
```bash
mkdir path/to/dir
```

This command will make a directory at the specified path. Need to make multiple folders in a row? Say you only have the `path/` dir above and you wanted to make both `to/` and `dir/`. You can simply add the `-p` flag!

```bash
mkdir -p path/to/dir
```

#### Touch (create) a file
```bash
touch path/to/file
```
Touch is an interesting command. If a file already exists, it will do nothing (this isn't totally true, but will be for the purposes of this repo). But if it doesn't, it will create a file

### Basic Python commands

#### Run a Python file
```bash
python path/to/file.py
```

This will run the file specified at that path through the python interpreter, and execute your code. If you run `python` without a path,

#### Run the interactive Python interpreter
```bash
python
```
this will start the interactive Python interpreter. to exit this, simply type CTRL + D.

### Basic Git Commands

#### Clone a repository
```bash
git clone https://github.com/rsnider-ct/coding-challenges.git
```
This will read the remote codebase at the URL and download a local copy to your computer. This will also set up all the tracking information you would need to pull and push code to the repository.

#### Update my local project with the latest changes from the remote
```bash
git pull origin <branch-name>
```

This will read the latest information from the specified branch (default is `master`), and will update that same local branch with new information

#### Create a new branch to work off of
```bash
git checkout -b new-branch-name
```

This will create a copy of the current branch you're on (make sure you `git pull` first!) and start a new branch as an offshoot of that. Here you can safely make changes to code without changing anything on the master branch. 

#### Add new files to Git
```bash
git add path/to/file.py path/to/other/file.py
```

This command will add the specified files to version control and will tell git to start tracking them as part of the repository.

#### Commit code to a branch
```bash
git commit -m "my cool commit message"
```
This command will prepare your code to be committed to the current branch you are on. NOTE! This will commit _all_ outstanding changes, which might not be intended. To commit certain files, just specify them

```bash
git commit path/to/file.py path/to/other/file.py -m "my cool commit message"
```

#### Push code to a branch
```bash
git push origin my-branch
```
This will take that commit you just made and push it to the remote branch for tracking. From here your code is safe in Git and you are free to continue making changes (or switch branches!) 

One thing to note, is that sometimes there isn't a branch on the remote server to track your current local one. To push code to a `new` branch in the remote repository, simply type 

```bash
git push -u origin my-branch
```

that `-u` flag will tell git that there needs to be a new branch created on the remote. It will create it and tell you all about it.