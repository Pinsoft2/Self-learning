#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
// If your program is not executed with exactly one command-line argument, it should remind the user of correct usage, and main should return 1.
   if (argc != 2)
    {
        printf("Please provide the correct jpeg name");
        return 1;
    }

// If the forensic image cannot be opened for reading, your program should inform the user as much, and main should return 1.
    FILE *inptr = fopen(argv[1], "r");

    if (inptr == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 1;
    }

    uint8_t buffer[512];
    int jpeg_count = 0;
    FILE *outptr = NULL;
    char filename[8];

    while (fread(buffer, 1, 512, inptr) == 512)
        {

        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
             if (outptr != NULL)
            {
                fclose(outptr);
            }

        //use sprintf to create a location

         sprintf(filename, "%03i.jpg", jpeg_count);

        outptr = fopen(filename, "w");

        jpeg_count ++;


        }
        if (outptr != NULL){
        fwrite(buffer, 1, 512, outptr);}

        }

    fclose(inptr);
    if (outptr != NULL){
    fclose(outptr);}
    return 0;

}