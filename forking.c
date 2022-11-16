#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

int main(int argc, char *argv[]) {

    pid_t child_pid, child_pid_wait;
    int child_status;
    
    if((child_pid = fork()) == 0) {
        execvp(argv[1], argv+1); // argv+1 "ignores" the first element in the array
        fprintf(stderr, "Enter a valid program name!\n");
	      exit(1);
    }
    else {
        if (child_pid == (pid_t)(-1)) {
            fprintf(stderr, "\nFork failed.\n");
            exit(1);
        }
        else {
            child_pid_wait = wait(&child_status); // Wait for child
            fprintf(stderr, "\nChild's exit code was: %d", WEXITSTATUS(child_status));
        }
    }
    return 0;
}
