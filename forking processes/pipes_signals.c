#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>
#include <stdio.h>
#include <errno.h>

int pipe_ping[2];
int pipe_pong[2];

void signal_handler() {
    printf("Pong quitting");
    exit(0);
}

void ping() {
    int ping_value = 0, len;
    
    while(ping_value < 100) {
        printf("ping: %d\n", ping_value);
        ping_value++;
        
        write(pipe_ping[1], &ping_value, sizeof(ping_value));
        len = read(pipe_pong[0], &ping_value, 100);
    }
    exit(0);
}

void pong() {
    int pong_value = 0, len;
    
    signal(SIGUSR1, signal_handler);
    
    while(1) {
        len = read(pipe_ping[0], &pong_value, 100);
        printf("pong: %d\n", pong_value);
        pong_value++;
        write(pipe_pong[1], &pong_value, sizeof(pong_value));
    }
}

int main()
{
    pid_t child_ping, child_pong, child_wait;
    int child_status;
    
    pipe(pipe_ping);
    pipe(pipe_pong);
    
    if((child_ping = fork()) == 0) {
        ping();
    }
    else if((child_pong = fork()) == 0) {
        pong();
    }
    else {
        child_wait = wait(NULL);
        kill(child_pong, SIGUSR1);
    }
    return 0;
}
