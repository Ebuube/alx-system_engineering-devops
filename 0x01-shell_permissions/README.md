The file script that switches the current user to the user betty.


The file 1-who_am_i, prints the effective username of the current user.

The file 2-groups prints all the groups the current user is part of.

The file 3-new_owner changes the owner of the file hello to the user betty.

The file 4-emtpy creates an empty file called hello.

The file 5-execute  adds execute permission to the owner of the file hello.

The file 6-multiple_permissions adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.

The file 7-everybody adds execution permission to the owner, the group owner and the other users, to the file hello.

The file 8-James_Bond  sets the permission to the file hello as follows:
	Owner: no permission at all

	Group: no permission at all

	Other users: all the permissions

The file 9-John_Doe sets the mode of the file hello to this:
	-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello

The file 10-mirror_permission sets the mode of the file hello the same as olleh’s mode.

	The file hello will be in the working directory
	The file olleh will be in the working directory

The file 11-directories_permissions adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.

The file 12-directory_permissions creates a directory called my_dir with permissions 751 in the working directory.

The file 13-change_group changes the group owner to school for the file hello.


