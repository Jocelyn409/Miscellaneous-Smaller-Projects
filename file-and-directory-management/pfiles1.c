#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <time.h>
#include <string.h>
#include <unistd.h>

int main() {
    int sum = 0;
    int random, wrfile, size;
    int array_random[100];
    char name[16], number[3];
    srand(time(NULL));
    
    // Calculate sum and populate array with random numbers.
    for (int x = 0; x <= 99; x++) {
        random = rand() % 100;
        array_random[x] = random;
        sum = sum + random;
    }
    
    sprintf(name, "numbers_%d.txt", sum); // Create string for file name and put it into the "name" string.
    
    if ((wrfile = open(name, O_WRONLY | O_CREAT)) == -1) {
        return -1;
    }
    
    // Write to file.
    for(int x = 0; x <= 99; x++) {
        sprintf(number, "%d\n", array_random[x]);
        size = write(wrfile, number, strlen(number));
    }
  
    close(wrfile);
    return 0;
}
