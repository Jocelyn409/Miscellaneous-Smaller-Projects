#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <fcntl.h>
#include <ctype.h>
#include <unistd.h>
#include <sys/stat.h>

int main() {
    DIR *dir;
    struct dirent *entry;
    int rdfile;
    char *substr;
    char entrystr[17], new_num[2], buffer[1];
    
    // Open current directory
    if ((dir = opendir(".")) == NULL) {
        printf("Could not open directory .\n");
        exit(1);
    }
    
    // Read through directory
    while ((entry = readdir(dir)) != NULL) {
        int sum = 0;
        int length = 1;
        
        strcpy(entrystr, entry->d_name);
        substr = strstr(entrystr, "numbers_"); // Check to see if entrystr contains "numbers_".
        
        if(substr != NULL) {
            // Open file
            if ((rdfile = open(entrystr, O_RDONLY)) == -1) {
                fprintf(stderr, "Could not open file: %s\n", entrystr);
            }
            // Read from file
            while(length != 0 && length != -1) {
                if((length = read(rdfile, buffer, 1)) == -1) {
                    fprintf(stderr, "Could not read from file.\n");
                }
                else if(isspace(buffer[0]) == 0) {
                    strcat(new_num, buffer); // Add current char to new_num
                }
                else if(isspace(buffer[0]) != 0) {
                    new_num[2] = '\0'; // Limit string to 2 chars long to remove excess string due to a weird interaction between strcat() and buffer
                    sum = sum + atoi(new_num); // Add the 'integer' in the string to the sum
                    new_num[0] = '\0'; // Reset string
                }
            }
            printf("File name: %s\n", entry->d_name);
            printf("Sum: %d\n", sum);
            
            close(rdfile);
        }
    }
    
    closedir(dir);
    return 0;
}
