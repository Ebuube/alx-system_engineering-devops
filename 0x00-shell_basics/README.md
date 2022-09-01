The file 0-current_working_directory, is a script that prints the absolute path name of the current working directory.



The file 1-listit, displays the contents of your current directory.



The file 2-bring_me_home, changes the working directory to the user's home directory


The file 3-listfiles, displays the current directory's content in long format


The file 4-listmorefiles, displays current directory contents, including hidden files (starting with .). Use the long format.


The file 5-listfilesdigitonly, display current directory contents.

Long format

with user and group IDs displayed numerically

And hidden files (starting with .)


The file 6-firstdirectory, creates a directory named /tmp/my_first_directory/


The file 7-movethatfile, moves the file betty from /tmp/ to /tmp/my_dirst_directory/

The file 8-firstdelete, deletes the file /tmp/my_first_directory/betty.

The file 9-firstdirdeletion, deletes the directory /tmp/my_first+directory/


The file 10-back, changes the working directory to the previous one


The file 11-lists, lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.


The file 12-file_type prints the type of file iamafile is.


The file 13-symbolic_link, creates a symbolic link named _ls_ for /bin/ls

The file 14-copy_html, copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

The file 100-lets_move, moves all files beginning with an uppercase letter to the directory /tmp/u.


The file 101-clean_emacs,  deletes all files in the current working directory that end with the character ~.

The file 102-tree creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory.
You are only allowed to use two spaces (and lines) in your script, not more.


The file 103-commas, Write a command that lists all the files and directories of the current directory, separated by commas (,).
Directory names should end with a slash (/)

Files and directories starting with a dot (.) should be listed

The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning

Only digits and letters are used to sort; Digits should come first

You can assume that all the files we will test with will have at least one letter or one digit

The listing should end with a new line


The file school.mgc  can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.


