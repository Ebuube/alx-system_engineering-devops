#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>


int infinite_while(void);


/**
 * main - a program that creates five (5) zombie processes
 *
 * Return: Always return 0
 */
int main(void)
{
	pid_t f_pid = 0;
	int count = 0;

	for (count = 0; count < 5; count++)
	{
		f_pid = fork();

		if (f_pid == -1)
		{
			/* error forking this process */
			exit(EXIT_FAILURE);
		}

		if (f_pid == 0)
		{
			/* child process */
			exit(EXIT_SUCCESS);
		}

		if (f_pid > 0)
		{
			/* parent process creates more children*/
			printf("Zombie process created, PID: %d\n", f_pid);
		}
	}

	infinite_while();

	return (EXIT_SUCCESS);
}

/**
 * infinite_while - infinitely sleep the proccess
 *
 * Return: Always return 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
