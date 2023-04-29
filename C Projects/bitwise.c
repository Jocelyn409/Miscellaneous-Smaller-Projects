#include <stdio.h>
#include <stdlib.h>

int bit_count_on(unsigned int input, int len) {

    int x, bitOn = 0, shift = 1;

        for (x = 1; x <= len; x++) {
            if ((shift & input) >= 1) {
                bitOn++;
            }
            shift <<= 1;
        }

    return bitOn;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Provide only one number as an argument.\n");
        return 1;
    }

    unsigned int input = strtol(argv[1], (char **)NULL, 10);
    int bitOn = 0, bitOff = 0, len = sizeof(input) * 8;

    bitOn = bit_count_on(input, len);
    bitOff = len - bitOn;
  
    printf("Your number was %d\n", input);
    printf("In %d, there are %d bits set to 0.\n", input, bitOff);
    printf("In %d, there are %d bits set to 1.\n", input, bitOn);

  return 0;
}
