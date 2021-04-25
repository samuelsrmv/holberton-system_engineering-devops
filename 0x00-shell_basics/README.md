# 0x00. Shell, basics

## Resources :books::bulb::rocket:
Read or watch:
* [What Is “The Shell”?](https://intranet.hbtn.io/rltoken/pn2_LGNuA1yFY7zy3CQmig)
* [Navigation](https://intranet.hbtn.io/rltoken/Hh8elGgCpj--6othR7S7GQ)
* [Looking Around](https://intranet.hbtn.io/rltoken/84xsZOempqy5I7ZkueeIsg)
* [A Guided Tour](https://intranet.hbtn.io/rltoken/Jp1c4V3hJiGBuVzYCtnQKw)
* [Manipulating Files](https://intranet.hbtn.io/rltoken/wFwFXKQmSpmxYyvHvCIC-Q)
* [Working With Commands](https://intranet.hbtn.io/rltoken/Aq3NVLBhgnQS6NYtHI8i4w)
* [Reading Man pages](https://intranet.hbtn.io/rltoken/RohkjGiQtMHgPfj0N_k1Bw)
* [Keyboard shortcuts for Bash](https://intranet.hbtn.io/rltoken/0HvJ2B_wSl6Oyshcn-OHrg)
* [LTS](https://wiki.ubuntu.com/LTS)
* [Shebang](https://intranet.hbtn.io/rltoken/ketzZf-802Fb-mSGkyPa4w)

---
## Learning Objectives :man_technologist:
What you should learn from this project:

* What does RTFM mean?
* What is a Shebang

---

### [0. Where am I?](./0-current_working_directory)
* Write a script that prints the absolute path name of the current working directory.


### [1. What’s in there?](./1-listit)
* Display the contents list of your current directory.


### [2. There is no place like home](./2-bring_me_home)
* Write a script that changes the working directory to the user’s home directory.


### [3. The long format](./3-listfiles)
* Display current directory contents in a long format


### [4. Hidden files](./4-listmorefiles)
* Display current directory contents, including hidden files (starting with .). Use the long format.


### [5. I love numbers](./5-listfilesdigitonly)
* Display current directory contents.


### [6. Welcome holberton](./6-firstdirectory)
* Create a script that creates a directory named holberton in the /tmp/ directory.


### [7. Betty in Holberton](./7-movethatfile)
* Move the file betty from /tmp/ to /tmp/holberton.


### [8. Bye bye Betty](./8-firstdelete)
* Delete the file betty.


### [9. Bye bye Holberton](./9-firstdirdeletion)
* Delete the directory holberton that is in the /tmp directory.


### [10. Back to the future](./10-back)
* Write a script that changes the working directory to the previous one.


### [11. Lists](./11-lists)
* Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.


### [12. File type](./12-file_type)
* Write a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.


### [13. We are symbols, and inhabit symbols](./13-symbolic_link)
* Create a symbolic link to /bin/ls, named __ls__.
The symbolic link should be created in the current working directory. 


### [14. Copy HTML files](./14-copy_html)
* Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.


### [15. Let’s move](./15-lets_move)
* Create a script that moves all files beginning with an uppercase letter to the directory /tmp/u.


### [16. Clean Emacs](./16-clean_emacs)
* Create a script that deletes all files in the current working directory that end with the character ~.


### [17. Tree](./17-tree)
* Create a script that creates the directories welcome/, welcome/to/ and welcome/to/holberton in the current directory.


### [18. Life is a series of commas, not periods](./18-commas)
* Write a command that lists all the files and directories of the current directory, separated by commas (,).


### [19. File type: Holberton](./holberton.mgc)
* Create a magic file holberton.mgc that can be used with the command file to detect Holberton data files. Holberton data files always contain the string HOLBERTON at offset 0.

---

## Author :writing_hand:
* **Samuel Martinez** - [samuelsrmv :octocat:](https://github.com/samuelsrmv)