#include "helpers.h"
#include <math.h>

// Convert image to grayscale
// In fact, to ensure each pixel of the new image still has the same general brightness or darkness as the old image, we can take the average of the red, green, and blue values to determine what shade of grey to make the new pixel.

// If you apply that to each pixel in the image, the result will be an image converted to grayscale.
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    float avg;
    for (int i=0; i< height; i++ ){
        for (int j=0; j < width; j++)
        {
            avg = round((float)(image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed)/3);
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // Swap pixels
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sumRed = 0, sumGreen = 0, sumBlue = 0;
            int count = 0;

            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di;
                    int nj = j + dj;

                    if (ni >= 0 && ni < height && nj >= 0 && nj < width)
                    {
                        sumRed += image[ni][nj].rgbtRed;
                        sumGreen += image[ni][nj].rgbtGreen;
                        sumBlue += image[ni][nj].rgbtBlue;
                        count++;
                    }
                }
            }

            temp[i][j].rgbtRed = round((float)sumRed / count);
            temp[i][j].rgbtGreen = round((float)sumGreen / count);
            temp[i][j].rgbtBlue = round((float)sumBlue / count);
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
}

// Detect edges
    int cap(int value)
    {
        return value < 0 ? 0 : (value > 255 ? 255 : value);
    }

void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int GxRed = 0, GxGreen = 0, GxBlue = 0;
            int GyRed = 0, GyGreen = 0, GyBlue = 0;

            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di;
                    int nj = j + dj;

                    if (ni >= 0 && ni < height && nj >= 0 && nj < width)
                    {
                        GxRed += image[ni][nj].rgbtRed * Gx[di+1][dj+1];
                        GxGreen += image[ni][nj].rgbtGreen * Gx[di+1][dj+1];
                        GxBlue += image[ni][nj].rgbtBlue * Gx[di+1][dj+1];
                        GyRed += image[ni][nj].rgbtRed * Gy[di+1][dj+1];
                        GyGreen += image[ni][nj].rgbtGreen * Gy[di+1][dj+1];
                        GyBlue += image[ni][nj].rgbtBlue * Gy[di+1][dj+1];

                    }
                }
            }

            temp[i][j].rgbtRed = cap(round(sqrt(GxRed*GxRed + GyRed*GyRed)));
            temp[i][j].rgbtGreen = cap(round(sqrt(GxGreen*GxGreen + GyGreen*GyGreen)));
            temp[i][j].rgbtBlue = cap(round(sqrt(GxBlue*GxBlue + GyBlue*GyBlue)));
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
}
