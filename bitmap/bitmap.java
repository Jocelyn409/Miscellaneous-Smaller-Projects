import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.FileReader;
import java.util.Scanner;

public class Project2_Lahaise {

    public static void main(String[] args) throws FileNotFoundException {

        byte on, mask;
        int number, leftover, x, y;

        Scanner inFile = new Scanner(new FileReader(args[0]));
        PrintWriter outFile = new PrintWriter(args[1]);
        byte[] bitmap = new byte[1000000];


        while(inFile.hasNextInt()) {
            number = inFile.nextInt() - 2000000;
            leftover = number % 8; // Gets the bit position.

            switch (leftover) {
                case 0:
                    on = (byte) 128;
                    break;
                case 1:
                    on = 64;
                    break;
                case 2:
                    on = 32;
                    break;
                case 3:
                    on = 16;
                    break;
                case 4:
                    on = 8;
                    break;
                case 5:
                    on = 4;
                    break;
                case 6:
                    on = 2;
                    break;
                case 7:
                    on = 1;
                    break;
                default:
                    on = 0;
            }

            bitmap[number / 8] = (byte) (bitmap[number / 8] | on); // Turns on bits one at a time.

        }

        for(y = 0; y < 1000000; y++) {

            mask = (byte)0x80; // Resets mask

            for(x = 0; x < 8; x++) {

                if ((bitmap[y] & mask) != 0) {
                    outFile.println((y * 8) + x + 2000000);
                }

                mask = (byte)((mask & 0xff) >>> 1);

            }

        }

        inFile.close();
        outFile.close();

    }
